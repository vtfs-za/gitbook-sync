# Symbol & Account lookups

In the platform there are two kinds of lookups – 'Account lookup' and 'Symbol lookup' which are helpful in filtering panels' data.

### Symbol lookup

The Symbol lookup window shows all symbols which are available through the broker. The Symbol lookup window can be opened in each panel which requires symbol selection through the context menu or by clicking on the button<img src="../../../.gitbook/assets/Artboard1.png" alt="" data-size="original">. Hover the symbol name<img src="../../../.gitbook/assets/regular MAC.png" alt="" data-size="line">in the toolbar of the chosen panel to see this button<img src="../../../.gitbook/assets/hover MAC.png" alt="" data-size="line">.

<figure><img src="../../../.gitbook/assets/image (450).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="warning" %}
Click the symbol icon in the lookup of the chosen panel to open the Symbol info panel.
{% endhint %}

The Symbol lookup contains two drop-down lists with exchanges<img src="../../../.gitbook/assets/all exchanges_116_22.png" alt="" data-size="original">and symbols grouped according to their types, which are used on the server and available to the user<img src="../../../.gitbook/assets/all types_116_22.png" alt="" data-size="original">. All symbols are shown in the default sequence. To filter the Symbol lookup by an exchange or symbol name, you need to select the required exchange and/or symbol type from the lists.

![](<../../../.gitbook/assets/small amex.png>)

![](<../../../.gitbook/assets/short list types - 196_202.png>)

After selecting the needed value and filtering the items all symbol tabs which don't match the filter will be hidden from the list.

Search window<img src="../../../.gitbook/assets/search add - Copy.png" alt="" data-size="original">allows to find a needed symbol quickly. Enter a symbol's name and double-click on a displayed needed symbol to select it from filtered results.

Select 'All' in the drop-down exchange and types lists in order to cancel the filtering and view all symbol tabs.

If symbol name in the symbol lookup window is entered from the keyboard, then all symbol groups containing symbols with matches in their names are expanded.

For easy management of the lookup, it has the following buttons located at the bottom of the screen:

* <img src="../../../.gitbook/assets/1 (127).png" alt="" data-size="original">Collapse all – allows to collapse all opened tabs to the form that shows only exchanges in the lookup tree.
* <img src="../../../.gitbook/assets/2 (160).png" alt="" data-size="original"> Expand exchanges – allows showing exchanges and symbol types in the lookup tree.
* <img src="../../../.gitbook/assets/3 (70).png" alt="" data-size="original"> Expand types – allows showing exchanges, symbol types and symbols in the lookup tree.
* <img src="../../../.gitbook/assets/5 (37).png" alt="" data-size="original"> 'Show additional info' icon – shows short information about the selected symbol.<br>

<figure><img src="../../../.gitbook/assets/image (451).png" alt=""><figcaption></figcaption></figure>

All symbols are grouped according to categories: Equities, Forex, Futures, etc. The Symbol lookup window displays information as follows: exchange, symbol type and icon, symbol group, symbol, contract or strike price (for Futures and Options).

{% hint style="warning" %}
You can search for symbols and filter them by their localized names if they were assigned localized names in one or several supported languages on the server. To do that you need to select the corresponding language for the application user interface and enter the localized name of the sought instrument/instruments in this language. With that, for all the symbols in the lookup, their localized names will be displayed when the corresponding interface language is selected. The same principle applies to the display of instrument names in Chart, Market depth, Order entry, Matrix, Super DOM (depth of market), Scalper, Symbol info, Aggressor balance, Saved orders panels as well as Positions, Working orders, Orders history, Filled orders, Positions balance panels.
{% endhint %}

If there is no localized name for an instrument for the current interface language, the server instrument name is displayed.

For Options the detailed symbols' information (description) is also available in the lookup:

![](<../../../.gitbook/assets/mac (3).png>)

### Account lookup

The Account lookup is available only for multi-account users. It displays all accounts available for the user. The Account lookup panel can be opened in each panel which requires account selection by clicking on the button<img src="../../../.gitbook/assets/Artboard1.png" alt="" data-size="original">next to the account scroll down menu. The account base currency is displayed next to each account name; if the user has only one account or multi-currency accounts, then the account currencies will not be displayed.

<figure><img src="../../../.gitbook/assets/Screenshot_8 (1).jpg" alt="" width="396"><figcaption></figcaption></figure>

Double-click on a needed account allows to select it.

All Accounts are sorted on base of "User group -> User" hierarchy. User can hide any accounts which belong to the specific User or User group.
