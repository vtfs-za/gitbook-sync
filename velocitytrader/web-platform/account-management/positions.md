# Positions

Positions panel lists all currently opened positions. When a new position is opened, it will appear in this panel immediately. To open Positions panel, select Terminal -> Positions:

<figure><img src="../../.gitbook/assets/image (1364).png" alt=""><figcaption></figcaption></figure>

The following columns are available in the panel:

* Symbol – a traded symbol;
* Account – login name of an account that opened a position;
* Login – login of a user;
* Symbol description – comments to an instrument;
* Symbol type – a symbol's market category (CFD, spot, stocks, etc.);
* Position ID – a unique number that the trading system assigns to each position;
* Side – type of trade (Long or Short);
* Open price – price at which a position was opened;
* Current price – a market price obtainable from a broker;
* Quantity – amount of a position, either in lots or in units, depending on what is selected in the Settings dialog box;
* Date/Time – date and time when a position was opened;
* Gross P/L – profit/loss in account currency, calculated on base of price difference:

For Long position: Gross P/L = Qty. \* Lot size \* Cross price \* (Current price - Open price)

For Short position: Gross P/L = Qty. \* Lot size \* Cross price \* (Open price - Current price)

* P/L, offset – profit/losses in ticks;
* Net P/L – profit/loss for a position excluding fee:

Net P/L = Gross P/L - Fee - Swaps

* Position exposure – exposure of a position, in the account currency. Calculated on base of an open price:

Position exposure = Price \* Quantity \* Lot size \* Cross price (quoting CCY > account currency) – calculation for Forex

Position exposure = Price \* Quantity \* (Tick cost/Tick size) \* Cross price (quoting CCY > account currency) – calculation for Futures

In all cases Cross price (quoting CCY > account currency) is a current cross price.

* Net P/L % – displays the percentage of Net P/L relative to the Position exposure calculated in the following way:

Net P/L % = (Net P/L / Position exposure) \* 100%

* Position value – current value of a position. Calculated on base of a current market price:

For Long position: Position value = Position exposure + P/L

For Short position: Position value = Position exposure – P/L

* Fee – shows total commission amount taken for a position;
* Swaps – amounts collected/paid out by a broker when a position is rolled over to a new value date;
* Expiry date – date of contract expiration;
* Strike price – price of option contract performance;
* SL validity - shows the validity (TIF) selected for the order's Stop loss;
* TP validity - shows the validity (TIF) selected for the order's Take profit;
* Route – name of a route;
* SL price – Stop loss price set for a position;
* TP price – Take profit price set for a position;
* SL limit price – Limit price set for SL order;
* Leverage - contains leverage value, if applicable;
* Close – allows to close a selected position;
* Accrued interest - interest accrued on position. Note that the value is rounded to account currency accuracy;
* Strategy ID – identifier of an execution strategy that opened position.

**Displaying totals considering account currency**

The totals are calculated taking into account the account currency according to the filtering results:

* If the filtered entries belong to accounts with the same currency, then the totals are displayed in the account currency.
* If the filtered entries belong to accounts with different currencies, then the totals are displayed in the server currency.

### **Buttons toolbar**

The most important functions related to Positions can be viewed as buttons in the toolbar of the panel.

<figure><img src="../../.gitbook/assets/image (1365).png" alt=""><figcaption></figcaption></figure>

* Close all – closes all opened positions;
* CLX all – closes all opened positions and cancels all orders;
* Close negative – closes the positions with negative P/L;
* Close positive – closes the positions with positive P/L;
* Close – closes all positions by selected symbol and account;
* Close selected – closes all selected positions;
* CLX – closes opened positions and cancels orders by selected symbol and account;
* Close long – closes the positions with Side = Long;
* Close short – closes the positions with Side = Short.

To select the buttons to be displayed, simply right-click on the toolbar of the panel and select the needed buttons from the menu.

{% hint style="warning" %}
Clicking these buttons doesn't evoke confirmation screens, even if confirmations are enabled in the 'General settings'.
{% endhint %}

Also note that user can disable position closing on double-click in the [General settings](../getting-started/general-settings.md) panel.

### **Context menu**

The following functions can be realized through context menu:

<figure><img src="../../.gitbook/assets/image (1742).png" alt=""><figcaption></figcaption></figure>

* Modify position – allows adding SL/TP orders to selected position manually;

{% hint style="warning" %}
Can be disabled in case the volume of the opened position exceeds the Maximum lot set by the admin, i.e. the Max lot has been reached.
{% endhint %}

* Close position by Mkt – allows closing selected positions by Market price;
* Close position via OE - opens Order Entry panel to close the selected position;
* Symbol info - opens the Symbol Info window for the instrument of the selected position;
* View – allows to show toolbar;
* Group by – allows to group positions by account, login, symbol, symbol description, symbol type, side, expiry date, strike price;
*   Exercise options – sends an exercise request for the Option position. Available for single positions opened for Options with Exercise style=American, inactive for multiple selected positions.

    After clicking this menu item, a confirmation dialog box is displayed with the Position ID, Symbol, Side, Quantity to close, Open price, Current price, Gross P/L to close, Account, Date/Time position parameters.

    Clicking the "Exercise" button in the confirmation box, creates a request for the Option exercise, which switches the position to Pending exercise status and prevents performing the following operations for the position: **Close position, Close by(ID), Reverse, Reverse by (ID).**

    The mentioned actions are reenabled for the position after the "Cancel exercise" action is performed.\
    Note that broker can prohibit American-style options from being exercised if the strike price is out of the money.
*   Cancel exercise – cancels an exercise request for the selected Option position with Pending exercise status. Available for single positions opened for Options with Exercise style=American, inactive for multiple selected positions.

    After clicking this menu item, a confirmation dialog box is displayed, which requires a confirmation of canceling an Option exercise request. After the exercise Option request is canceled, the **Close position, Close by(ID), Reverse, Reverse by (ID)** operations become allowed for the position.
* Modify product type – this tab allows adding SL/TP orders to the selected position manually as well as modify quantity and change the target product type.

{% hint style="warning" %}
The tab is available only when both _Intraday_ and _Delivery_ trading modes are available for the Instrument/Account pair. Also for Positions with "Net by average price" netting type. Product type modification should also be allowed for this user.

The user can also have _Positions close only_ or _Liquidation only_ status depending on his plan. In this case, product type can not be modified and an appropriate reject message is sent to the user.
{% endhint %}

* Target product type – drop-down list for selecting the new target product type;
* Modify quantity – switchable numeric for indicating the Qty to be modified. The default value is _Modify quantity = Quantity - Start of day qty_, please note that this value cannot be greater than _Today traded qty_. In case this numeric is enabled, SL/TP price controls are automatically disabled;
* SL/TP price – Stop loss and Take profit prices that are available for modification. These controls are disabled in case the “Modify quantity” control is active.

{% hint style="warning" %}
When changing the Product type, all SL/TP orders will be canceled and the corresponding error will be displayed.
{% endhint %}

If _Quantity > Maximum lot_ set by the admin, the user will receive the following warning:

{% hint style="warning" %}
Quantity is greater than Maximum lot. Orders will be created to close the position.
{% endhint %}

In case a commission is charged for closing a position, it will be charged for each order into which the position was split.

### Mutual closing

The user can mutually close two positions one by another if this feature is available to him. In order to do this, the user should select two positions (with a pressed Shift button), then right-click on one of them to open the context menu and select the "Mutual close" option.

Please note that Mutual closing can be carried out when two positions for the same instrument are selected. The following conditions must be met in order for a mutual closing to be available:

* Positions to close must be selected for the same instrument;
* These positions must be oppositely directed (i.e. both Long and Short positions must be selected);
* In case the partial close is forbidden for this account, then the amount on both sides (Long and Short) must be equal;
* Only two positions can be selected;
* All positions must belong to the same account.
