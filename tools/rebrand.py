#!/usr/bin/env python3
"""Rebuild the Velocity Trader docs from a TraderEvolution (vendor) GitBook export.

The vendor docs live on the `upstream` remote. Every vendor page is regenerated from a vendor ref with a
word-based rebrand, so taking a vendor update means: git fetch upstream, then run this script. The docs are
written to velocitytrader/, the folder the GitBook space syncs (see gitbook-docs.yaml).

    python3 tools/rebrand.py                    dry run: report what would change
    python3 tools/rebrand.py --apply            write the regenerated docs into the working tree
    python3 tools/rebrand.py --check            verify the working tree, exit 1 on any problem
    python3 tools/rebrand.py --vendor-ref upstream/main ...      use another vendor ref

Changes made to a vendor page (every other byte is kept as it is):
  - TraderEvolution -> Velocity Trader (whole word, any case); in page paths traderevolution -> velocitytrader
  - absolute links guide.traderevolution.com/{project,traderevolution}/<page> -> relative .md links
  - dead guide.traderevolution.com/~gitbook/image?url=... proxy URLs -> the direct file URL they wrap
Vendor images that a page uses and .gitbook/assets lacks are copied in. Images are never deleted or overwritten:
the folder also holds rebranded screenshots, and images set aside in .gitbook/assets/TraderEvolution/ until a
rebranded version exists are not copied back.
Pages that exist only in the Velocity Trader docs are listed in EXTRAS and are left alone.
"""
import argparse
import io
import os
import posixpath
import re
import subprocess
import sys
import tarfile
import urllib.parse
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = "velocitytrader"  # all page and asset paths below are relative to this folder
DOCS = ROOT / DOCS_DIR
DEFAULT_REF = "upstream/gitbook/export-2263722b8c2ac01760acb8afcee23ac8"
FALLBACK_HOST = "https://help.za.velocitytrade.com"
BRAND_NAME = "Velocity Trader"
ASSETS = ".gitbook/assets"
SET_ASIDE = "TraderEvolution"  # subfolder of ASSETS for images that show the vendor brand
GITBOOK_YAML = ".gitbook.yaml"  # holds the redirects for page paths the docs no longer have
# Folders left by earlier versions of the docs: brand-named folders from earlier syncs, and the old mobile
# section brought back by GitBook change request GITBOOK-8.
LEGACY_DIRS = ("traderevolution-for-mobile", "mobile-applications")

# Pages that exist only in the Velocity Trader docs. Each is kept on --apply and listed in SUMMARY.md in
# front of the entry for `before`; it only counts once its page file exists.
EXTRAS = [
    {
        "page": "desktop-application-for-windows/windows/omnibus-account-management.md",
        "title": "Omnibus account management",
        "before": "desktop-application-for-windows/windows/trading-ideas.md",
    },
]

# Vendor links that still use page paths from before the vendor reorganised its docs.
STALE_LINKS = {
    "mobile-applications/phone/tablets/products": "traderevolution-for-mobile/tablets/subscriptions",
    "mobile-applications/phone/android/products": "traderevolution-for-mobile/phones/subscriptions",
    "mobile-applications/phone/tablets/order-entry": "traderevolution-for-mobile/tablets/order-entry",
    "mobile-applications/phone/android/order-entry": "traderevolution-for-mobile/phones/order-entry",
}

VENDOR_HOST = r"https://guide\.traderevolution\.com"
PAGE_URL = re.compile(
    VENDOR_HOST + r"/(?:project|traderevolution)/(?P<path>(?!~gitbook)[^\s)\"'<>\]#]+)(?P<frag>#[^\s)\"'<>\]]*)?")
TEXT_URL_LINK = re.compile(
    r"\[\s*(?P<text>" + VENDOR_HOST + r"/[^\]\s]+)\s*\]\((?P<url>" + VENDOR_HOST + r"/[^)\s]+)\)")
PROXY_URL = re.compile(
    VENDOR_HOST + r"/(?:project/)?~gitbook/image\?url=(?P<url>[^&\\\"\s)<>]+)(?:\\?(?:&#x26;|&amp;|&)[^\"\s)<>]*)?")
# Asset paths and external URLs are never word-replaced; anything left over is reported by --check.
KEEP = r"\.gitbook/assets/[^)\"'<>\n]*|https?://[^\s)\"'<>\]]+"
BRAND = re.compile(rf"(?P<keep>{KEEP})|\btraderevolution\b", re.I)
TARGET = re.compile(r"\]\(<(?P<a>[^>\n]*)>\)|\]\((?P<b>[^)\s<>]*)\)|\b(?:href|src)=\"(?P<c>[^\"\n]*)\"")
SUMMARY_LINE = re.compile(r"^(?P<pre>\s*\* \[)(?P<title>.*)(?P<mid>\]\()(?P<target>[^)]*)(?P<post>\).*)$")
EXTERNAL = re.compile(r"[a-z][a-z0-9+.-]*:|#|//", re.I)


def git(*args):
    p = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True)
    if p.returncode:
        sys.exit(f"git {' '.join(args[:2])} failed: {p.stderr.decode(errors='replace').strip()}")
    return p.stdout


def final_path(path):
    """Vendor repo path -> path in DOCS (folders and files named after the brand)."""
    return re.sub("traderevolution", "velocitytrader", path, flags=re.I)


def brand(text, stats=None):
    def sub(m):
        if m["keep"]:
            return m[0]
        if stats is not None:
            stats["brand words replaced"] += 1
        return BRAND_NAME
    return BRAND.sub(sub, text)


def replace_targets(text, fn):
    """Apply fn to the target of every Markdown link/image and every href/src attribute."""
    out, last = [], 0
    for m in TARGET.finditer(text):
        group = next(g for g in ("a", "b", "c") if m[g] is not None)
        out += [text[last:m.start(group)], fn(m[group])]
        last = m.end(group)
    out.append(text[last:])
    return "".join(out)


def rename_target(target):
    if EXTERNAL.match(target) or ".gitbook/" in target:
        return target
    return final_path(target)


def link_candidates(path):
    yield path, "exact"
    if path in STALE_LINKS:
        yield STALE_LINKS[path], "stale mobile path"
    head, _, rest = path.partition("/")
    if head == "desktop-application-for-windows" and not rest.startswith(("windows/", "desktop-application-for-mac/")):
        yield f"{head}/windows/{rest}", "desktop path without windows/"
    if head == "desktop-application-for-mac":
        yield f"desktop-application-for-windows/{path}", "mac path without desktop prefix"


def summary_titles(summary):
    titles = {}
    for line in summary.splitlines():
        m = SUMMARY_LINE.match(line)
        if m:
            titles.setdefault(m["target"], m["title"])
    return titles


def add_extras(summary, extras):
    for extra in extras:
        lines = summary.splitlines(keepends=True)
        for i, line in enumerate(lines):
            body = line.rstrip("\r\n")
            m = SUMMARY_LINE.match(body)
            if m and m["target"] == extra["before"]:
                indent = re.match(r"\s*", body).group()
                lines.insert(i, f"{indent}* [{extra['title']}]({extra['page']}){line[len(body):] or chr(10)}")
                break
        else:
            sys.exit(f"EXTRAS: SUMMARY.md has no entry for {extra['before']}")
        summary = "".join(lines)
    return summary


class Generator:
    def __init__(self, files):
        self.files = files
        self.pages = {p for p in files if p.endswith(".md")}
        self.titles = summary_titles(files["SUMMARY.md"].decode("utf-8", "surrogateescape"))
        self.stats = Counter()
        self.fallbacks = []
        self.contexts = Counter()
        self.titles_used = {}  # final page path -> titles that replaced a raw URL used as link text

    def resolve(self, path):
        for candidate, rule in link_candidates(path):
            for page in (candidate + ".md", candidate + "/README.md"):
                if page in self.pages:
                    return page, rule
        return None, "unresolved"

    def summary(self, text):
        lines = text.splitlines(keepends=True)
        for i, line in enumerate(lines):
            body = line.rstrip("\r\n")
            m = SUMMARY_LINE.match(body)
            if m:
                body = m["pre"] + brand(m["title"], self.stats) + m["mid"] + final_path(m["target"]) + m["post"]
            else:
                body = brand(body, self.stats)
            lines[i] = body + line[len(line.rstrip("\r\n")):]
        return "".join(lines)

    def page(self, src, text):
        dst = final_path(src)
        here = posixpath.dirname(dst) or "."

        def link(path, frag):
            target, rule = self.resolve(path)
            self.stats[f"vendor links: {rule}"] += 1
            if target is None:
                self.fallbacks.append((src, path))
                return f"{FALLBACK_HOST}/{path}{frag}", None
            return posixpath.relpath(final_path(target), here) + frag, target

        def text_link(m):
            parsed = PAGE_URL.fullmatch(m["url"])
            if parsed is None:
                return m[0]
            rel, target = link(parsed["path"].rstrip("/"), parsed["frag"] or "")
            if target is None:
                return f"[{rel}]({rel})"
            title = brand(self.titles.get(target, posixpath.basename(target)))
            self.titles_used.setdefault(dst, []).append(title)
            self.stats["link texts replaced by page title"] += 1
            return f"[{title}]({rel})"

        def page_url(m):
            before = m.string[max(0, m.start() - 2):m.start()]
            self.contexts["markdown target" if before.endswith("](") else
                          "html attribute" if before.endswith('="') else "other"] += 1
            return link(m["path"].rstrip("/"), m["frag"] or "")[0]

        def proxy_url(m):
            self.stats["dead image proxy URLs repaired"] += 1
            # GitBook writes & as \& in a Markdown link target and as &#x26; inside an HTML attribute
            amp = "\\&" if m.string[max(0, m.start() - 2):m.start()] == "](" else "&#x26;"
            return urllib.parse.unquote(m["url"]).replace("&", amp)

        text = TEXT_URL_LINK.sub(text_link, text)
        text = PROXY_URL.sub(proxy_url, text)
        text = PAGE_URL.sub(page_url, text)
        text = replace_targets(text, rename_target)
        return brand(text, self.stats)

    def generate(self, extras):
        out = {}
        for src, data in self.files.items():
            if not src.endswith(".md"):
                continue
            text = data.decode("utf-8", "surrogateescape")
            text = self.summary(text) if src == "SUMMARY.md" else self.page(src, text)
            out[final_path(src)] = text.encode("utf-8", "surrogateescape")
        if extras:
            summary = add_extras(out["SUMMARY.md"].decode("utf-8", "surrogateescape"), extras)
            out["SUMMARY.md"] = summary.encode("utf-8", "surrogateescape")
        return out


def load_vendor(ref):
    sha = git("rev-parse", "--verify", f"{ref}^{{commit}}").decode().strip()
    files, other = {}, []
    with tarfile.open(fileobj=io.BytesIO(git("archive", sha, "--", ".", ":(exclude).gitbook"))) as tar:
        for member in tar:
            if not member.isfile():
                continue
            name = member.name.removeprefix("./")
            if name.endswith(".md"):
                files[name] = tar.extractfile(member).read()
            else:
                other.append(name)
    if other:
        print(f"warning: ignoring {len(other)} non-markdown vendor files, e.g. {other[:3]}", file=sys.stderr)
    listing = git("ls-tree", "-r", "-z", "--name-only", sha, "--", ASSETS).decode("utf-8", "surrogateescape")
    names = {p.removeprefix(ASSETS + "/") for p in listing.split("\0") if p}
    return sha, files, names


def read_working(dirs):
    current = {}
    for entry in os.scandir(DOCS):
        if entry.is_file() and entry.name.endswith(".md"):
            current[entry.name] = Path(entry.path).read_bytes()
    for d in dirs:
        for base, _, names in os.walk(DOCS / d):
            for name in names:
                if name.endswith(".md"):
                    f = Path(base) / name
                    current[f.relative_to(DOCS).as_posix()] = f.read_bytes()
    return current


def plan(out, current, extras):
    keep = {e["page"] for e in extras}
    return {
        "add": sorted(out.keys() - current.keys()),
        "modify": sorted(p for p in out.keys() & current.keys() if out[p] != current[p]),
        "delete": sorted(current.keys() - out.keys() - keep),
    }


def asset_state(vendor_names, out):
    """Images used by the regenerated pages: (vendor images to copy in, images set aside, files in ASSETS)."""
    adir = DOCS / ASSETS
    work = {(Path(base) / n).relative_to(adir).as_posix() for base, _, names in os.walk(adir) for n in names}
    set_aside = {posixpath.basename(n) for n in work if n.startswith(SET_ASIDE + "/")}
    used = {t.removeprefix(ASSETS + "/") for src, data in out.items()
            for t in resolved_targets(src, data.decode("utf-8", "surrogateescape")) if t.startswith(ASSETS + "/")}
    absent = used - work
    missing = sorted(n for n in absent if n in vendor_names and n not in set_aside)
    pending = sorted(n for n in absent if n in set_aside)
    return missing, pending, work


def apply(sha, out, changes, assets):
    for path in changes["delete"]:
        (DOCS / path).unlink()
    for path in changes["add"] + changes["modify"]:
        f = DOCS / path
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_bytes(out[path])
    for d in sorted({p.split("/")[0] for p in changes["delete"] if "/" in p}):
        for base, _, _ in os.walk(DOCS / d, topdown=False):
            if not os.listdir(base):
                os.rmdir(base)
    missing, _, _ = assets
    for name in missing:
        f = DOCS / ASSETS / name
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_bytes(git("cat-file", "blob", f"{sha}:{ASSETS}/{name}"))


def tokens(text):
    t = re.sub(r"<figure>.*?</figure>", " ", text, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"!\[[^\]]*\]\((?:<[^>]*>|[^)]*)\)", " ", t)
    t = re.sub(r"\[([^\]]*)\]\((?:<[^>]*>|[^)]*)\)", r"\1", t)
    t = re.sub(r"https?://\S+", " ", t)
    t = re.sub(r"\{%.*?%\}", " ", t)
    t = re.sub(r"&#x[0-9A-Fa-f]+;", " ", t)
    t = re.sub(r"(?i)traderevolution|velocity\s*trader|evolutiontrader", "brand", t)
    return re.findall(r"[a-z0-9]+", t.lower())


def resolved_targets(src, text):
    """Path (relative to DOCS) of every relative link, image or href/src in page src."""
    for m in TARGET.finditer(text):
        target = next(m[g] for g in ("a", "b", "c") if m[g] is not None)
        if not target or EXTERNAL.match(target):
            continue
        target = re.sub(r"\\([\\`*_{}\[\]()#+\-.!&|<>])", r"\1", target)
        target = urllib.parse.unquote(re.split(r"[#?]", target)[0])
        yield posixpath.normpath(posixpath.join(posixpath.dirname(src), target))


def broken_refs(texts, known):
    """(page, resolved target) for every relative link, image or href/src that points at nothing."""
    return {(src, t) for src, text in texts.items() for t in resolved_targets(src, text) if t not in known}


def read_redirects():
    """The redirects in DOCS/.gitbook.yaml as {old page path: page file}."""
    f = DOCS / GITBOOK_YAML
    redirects, inside = {}, False
    for line in (f.read_text(encoding="utf-8").splitlines() if f.is_file() else []):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not line[0].isspace():
            inside = line.rstrip() == "redirects:"
        elif inside:
            key, _, value = line.strip().partition(": ")
            redirects[key.strip("'\"")] = value.strip().strip("'\"")
    return redirects


def check(files, vendor_names, gen, current, changes, assets):
    problems = []
    for kind, paths in changes.items():
        if paths:
            problems.append(f"working tree differs from a fresh regeneration: {len(paths)} to {kind}, e.g. {paths[:3]}")

    summary = current.get("SUMMARY.md", b"").decode("utf-8", "surrogateescape")
    targets = [m["target"] for m in map(SUMMARY_LINE.match, summary.splitlines()) if m]
    pages = set(current) - {"SUMMARY.md"}
    dupes = sorted(t for t, n in Counter(targets).items() if n > 1)
    if dupes or set(targets) != pages:
        problems.append(f"SUMMARY.md and the pages differ: {len(set(targets) - pages)} entries without a file, "
                        f"{len(pages - set(targets))} pages without an entry, {len(dupes)} duplicates "
                        f"(e.g. {sorted(set(targets) ^ pages)[:3]})")

    redirects = read_redirects()
    dangling = sorted(k for k, v in redirects.items() if v not in pages)
    shadowing = sorted(k for k in redirects if f"{k}.md" in pages or f"{k}/README.md" in pages)
    if dangling or shadowing:
        problems.append(f"{GITBOOK_YAML} redirects: {len(dangling)} point at no page, {len(shadowing)} are the path "
                        f"of an existing page (e.g. {(dangling + shadowing)[:3]})")

    missing, pending, work = assets
    texts = {p: b.decode("utf-8", "surrogateescape") for p, b in current.items()}
    known = set(current) | {f"{ASSETS}/{n}" for n in work}
    vendor_texts = {p: b.decode("utf-8", "surrogateescape") for p, b in files.items()}
    vendor_known = set(files) | {f"{ASSETS}/{n}" for n in vendor_names}
    vendor_broken = {(final_path(s), final_path(t)) for s, t in broken_refs(vendor_texts, vendor_known)}
    absent = {f"{ASSETS}/{n}" for n in missing + pending}  # reported on their own below
    new_broken = {(s, final_path(t)) for s, t in broken_refs(texts, known)} - vendor_broken
    new_broken = {(s, t) for s, t in new_broken if t not in absent}
    if new_broken:
        problems.append(f"{len(new_broken)} links or images point at nothing (not broken in the vendor docs), "
                        f"e.g. {sorted(new_broken)[:3]}")
    if missing:
        problems.append(f"{len(missing)} vendor images used by pages are missing from {ASSETS} "
                        f"(--apply copies them), e.g. {missing[:3]}")

    prose = {p: re.sub(KEEP, " ", t) for p, t in texts.items()}  # without asset paths and URLs
    leaks = [
        ("vendor brand", re.compile(r"traderevolution|evolutiontrader", re.I), texts),
        ("URL prefix that 404s on the site",
         re.compile(r"help\.za\.velocitytrade\.com/(?:project|VelocityTrader)/"), texts),
        (f"brand written without the space (not {BRAND_NAME})", re.compile(r"VelocityTrader"), prose),
        ("brand glued to letters", re.compile(rf"[A-Za-z]{BRAND_NAME}|{BRAND_NAME}[A-Za-z]"), prose),
        ("repaired image URL ending in a backslash",
         re.compile(r"https://\d+-files\.gitbook\.io/[^\s)\"<>]*\\\)"), texts),
    ]
    for label, pattern, pages_text in leaks:
        hits = sorted(p for p, t in pages_text.items() if pattern.search(t))
        if hits:
            problems.append(f"{label} found in {len(hits)} pages, e.g. {hits[:3]}")

    drift = []
    for src, data in files.items():
        dst = final_path(src)
        if src == "SUMMARY.md" or dst not in texts:
            continue
        a, b = tokens(data.decode("utf-8", "surrogateescape")), tokens(texts[dst])
        if a == b:
            continue
        # a link text that was a raw URL is now the page title: the new text may gain exactly those words
        titles = Counter(w for t in gen.titles_used.get(dst, []) for w in tokens(t))
        if not titles or Counter(b) - Counter(a) != titles or Counter(a) - Counter(b):
            drift.append(dst)
    if drift:
        problems.append(f"{len(drift)} pages differ from the vendor text beyond brand and links, e.g. {drift[:3]}")
    return problems


def set_aside_note(pending):
    return f"{len(pending)} images used by pages are set aside in {ASSETS}/{SET_ASIDE}/ until a rebranded version exists"


def report(sha, gen, changes, assets, extras):
    print(f"vendor ref {sha[:7]}: {len(gen.pages)} pages (incl. README.md, SUMMARY.md); "
          f"{len(extras)} extra {BRAND_NAME}-only page(s) kept")
    for key, n in sorted(gen.stats.items()):
        print(f"  {key}: {n}")
    for key, n in sorted(gen.contexts.items()):
        print(f"  vendor links as {key}: {n}")
    if gen.fallbacks:
        print(f"  UNRESOLVED vendor links ({len(gen.fallbacks)}), pointed at {FALLBACK_HOST}:")
        for src, path in gen.fallbacks:
            print(f"    {src}: {path}")
    print("working tree:")
    for kind, paths in changes.items():
        flat = [p for p in paths if "/" not in p and p not in ("README.md", "SUMMARY.md")]
        print(f"  {kind}: {len(paths)}" + (f" ({len(flat)} of them flat root pages)" if kind == "delete" else ""))
    missing, pending, _ = assets
    print(f"{ASSETS}: {len(missing)} vendor images used by pages are missing, to copy in; {set_aside_note(pending)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--vendor-ref", default=DEFAULT_REF, help=f"vendor git ref (default {DEFAULT_REF})")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true", help="write the regenerated docs into the working tree")
    mode.add_argument("--check", action="store_true", help="verify the working tree; exit 1 on any problem")
    ap.add_argument("--force", action="store_true", help="--apply even with uncommitted changes to tracked files")
    args = ap.parse_args()

    sha, files, vendor_names = load_vendor(args.vendor_ref)
    extras = [e for e in EXTRAS if (DOCS / e["page"]).is_file()]
    gen = Generator(files)
    out = gen.generate(extras)
    dirs = sorted({p.split("/")[0] for p in out if "/" in p} | set(LEGACY_DIRS))
    current = read_working(dirs)
    changes = plan(out, current, extras)
    assets = asset_state(vendor_names, out)

    if args.check:
        problems = check(files, vendor_names, gen, current, changes, assets)
        for p in problems:
            print("FAIL:", p)
        print("note:", set_aside_note(assets[1]))
        print("check:", "FAILED" if problems else f"ok ({len(current)} pages, vendor {sha[:7]})")
        sys.exit(1 if problems else 0)

    report(sha, gen, changes, assets, extras)
    if args.apply:
        dirty = git("status", "--porcelain", "--untracked-files=no", "--", DOCS_DIR).strip()
        if dirty and not args.force:
            sys.exit("refusing to --apply: tracked docs have uncommitted changes (commit them or use --force)")
        apply(sha, out, changes, assets)
        print("applied. Run with --check to verify, then review `git status`.")
    else:
        print("dry run; nothing written. Use --apply to write.")


if __name__ == "__main__":
    main()
