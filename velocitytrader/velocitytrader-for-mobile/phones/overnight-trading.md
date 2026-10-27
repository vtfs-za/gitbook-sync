# Overnight trading

Overnight trading allows user to place and execute orders outside of regular market hours. This feature gives you access to extended trading opportunities, but it is available only for instruments and accounts that support overnight trading.

#### How to setup overnight trading?

**1) Enable overnight trading by default**

You can manage your overnight trading preference in **Settings →** [**Defaults**](settings.md). Turn on **“Overnight execution by default”** if you want all new orders to be eligible for overnight execution automatically:

<figure><img src="../../.gitbook/assets/image (108).png" alt="" width="375"><figcaption></figcaption></figure>

If this option is disabled, orders will be placed only during regular market hours unless you enable it manually in the Order Entry panel.

{% hint style="warning" %}
This setting is visible only if at least one of your accounts supports overnight trading.
{% endhint %}

**2) Order Entry panel**

In the[ **Order Entry**](order-entry/) window, you will see the **Overnight execution** switch (if available for the selected account and instrument):

<figure><img src="../../.gitbook/assets/image (37).png" alt="" width="375"><figcaption></figcaption></figure>

Enable it if you want your order to be executed during overnight hours. Stop Loss and Take Profit orders will automatically inherit this setting. If the switch is not shown, overnight trading is not supported for the current instrument or account.

Orders placed with enabled _Overnight execution_ option will be marked with the following icon in the [Working orders](orders.md) panel:

<figure><img src="../../.gitbook/assets/image (110).png" alt=""><figcaption></figcaption></figure>

**3) Placing from Chart**

When placing orders directly from the chart, you will see additional option:

<figure><img src="../../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

When opening order from the Chart using the Visual trading feature, the following icon will be displayed on the order - <img src="../../.gitbook/assets/image (112).png" alt="" data-size="line">.

Tooltips will show whether the order will be executed during or outside regular trading hours.

**4) Other places**

Note that same options are also available when:

* Creating [Alerts](alerts.md);
* Placing orders via [Market depth](market-depth.md);
* Modifying [Positions](positions.md).

**5) Confirmation screens and event log**

The **confirmation window** and **event log** include information about whether the order is set for overnight execution.

**Summary**

To trade during overnight hours:

1. Your account and the selected instrument must support overnight trading.
2. Enable **Overnight execution** in the Order Entry panel or activate **Overnight execution by default** in settings.
3. Confirm that the option is displayed before placing the order — if it’s visible, overnight trading is available for you.

> Once enabled, the orders — including SL/TP — can be placed and executed even when the regular market session is closed.
