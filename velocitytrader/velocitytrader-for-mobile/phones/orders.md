# Orders

The Orders screen allows to view three lists of orders:

<figure><img src="../../.gitbook/assets/image (1577).png" alt="" width="375"><figcaption></figcaption></figure>

* Working orders – shows orders that are waiting for execution.
* Filled orders – shows executed orders.
* Orders history – each row displays info regarding creation, modification, execution or cancelling of orders.

Buy orders are displayed in the list with blue arrow, sell orders – with red.

{% hint style="warning" %}
Note that <img src="../../.gitbook/assets/image (1578).png" alt="" data-size="line"> icon means that order is eligible to be executed during overnight market hours. Read about overnight trading in more details [here](overnight-trading.md).
{% endhint %}

Each section consists of the cards list with short information about the orders: for Working orders – symbol name, quantity, open price, order type; for Filled orders – symbol name, order type, Net P/L, quantity. In order to get full information about the symbol on which the order was created, tap the symbol name.

<figure><img src="../../.gitbook/assets/image (203).png" alt="" width="375"><figcaption></figcaption></figure>

* Current price – market price obtainable from broker.
* Validity – allows specifying order validity by selecting among the following time frames: Day, GTC, IOC, GTD, FOK, GTS.
* Stop loss – stop loss price set for the order.
* Take profit – take profit price set for the order.
* Qty. remaining – difference between quantity and executed quantity when only part of the order was executed.
* Bound to – ID of the order which another order is bound to; if the former is executed, system will cancel the latter.
* Date/Time – date and time when the order was placed (executed, filled, modified, or cancelled).
* Account – login name of the account that opened the order.
* Order ID – unique number that the trading system assigns to each order. If a position is opened based on an order, the position will have the same number.
* Qty. filled - executed quantity of the order when only part of the order was executed.
* SL/TP offset - shows the order offset in ticks, fractional ticks, points or percentage (depending on the current configuration of the Trading defaults section of the General settings);
* Strategy ID – identifier of an execution strategy that placed order;
* Avg. price – shows the average execution price calculated across all fills of the order;
* Status - status of the current order. It can have the following values: Pending new, Pending execution, Pending cancel, Pending modification, Created, Accepted, Partially filled, Waiting for market, Waiting cancellation, Off market, Unplaced;
* Trading exchange – shows the exchange name which is set on a server for the order;
* SL/TP validity - shows the validity (TIF) selected for the order's Stop loss/Take profit;

Additional columns for Filled orders section:

* Trade ID – unique number of the trade.
* Exposure – quantity recalculated in account currency.
* Fee – shows commission connected with the trade.
* Gross P/L – total profit/loss of the trade.
* Bought – if Side = Buy, then this column shows the value of Price \* Lot size \* Qty in base currency; if Side = Sell, then this column shows the value of Price \* Lot size \* Qty in quoting currency.
* Sold – if Side = Sell, then this column shows the value of Price \* Lot size \* Qty in base currency; if Side = Buy, then this column shows the value of Price \* Lot size \* Qty in quoting currency.
* Trade volume – shows total volume of the trade.
* Price – shows price for Market and Limit orders, and Limit price for Stop limit orders.&#x20;

{% hint style="info" %}
Note that the following icon ![](<../../.gitbook/assets/image (92).png>) will be displayed near the Linked order.&#x20;
{% endhint %}

If the user needs to quickly switch to the Chart, modify the order or close it altogether when viewing a Working order, then it is necessary to swipe left the card of this order and the following buttons will become available:

<figure><img src="../../.gitbook/assets/image (1579).png" alt="" width="375"><figcaption></figcaption></figure>

To call the Context menu, press and hold (Long tap) on the needed item:&#x20;

<figure><img src="../../.gitbook/assets/image (205).png" alt="" width="375"><figcaption></figcaption></figure>

Actions available in the Context menu:

* Chart - by tapping, the Chart with the selected symbol will be opened;
* Symbol info - tap and detailed description of the symbol will be opened;
* Modify - this option allows Modifying needed Order;
* Cancel - allows canceling selected Order.

All orders can be canceled at once with a special button that is disabled in the app by default. This feature can be useful for managers or admins, in case there is a need to cancel all currently working orders. The "Cancel all" button is securely hidden in the Account menu to prevent accidental pressing. In order to enable this feature, please contact our support.

To quickly go to the chart, modify, or cancel the order just tap the corresponding icon. To return back to the order, tap the ‘Back’ button depicted as an arrow<img src="https://lh5.googleusercontent.com/FeoB164MubEhRzjZI288O316A51qKXagx2sSMaReRPOJ5NDeC1l862wWctT_U2Wkbuni-qTC-7pAzYNKFJxG5Z_SP7h57i4K3CKTGGyWTnOqE0msvOjWah_NT_36eIuww74QtXeI" alt="" data-size="line">in the upper left part of the chart.

Filled orders and Orders history sections can be viewed by selected date range, available values here are: daily, two days to date, week to date, month to date. To choose the date range, tap the button <img src="../../.gitbook/assets/image (207).png" alt="" data-size="line">.

<figure><img src="../../.gitbook/assets/image (206).png" alt="" width="375"><figcaption></figcaption></figure>

In order to modify active order, tap the ‘Modify’ button and the following screen will be opened:

<figure><img src="../../.gitbook/assets/image (208).png" alt="" width="375"><figcaption></figcaption></figure>

Here user can modify price, quantity, Validity, Stop loss, Trailing, and Take profit. In addition, order can be executed at a market price.

{% hint style="warning" %}
If Stop limit order is activated, the Stop price field will be disabled in Modify screen. Thus, only Limit price can be modified. The same is true for closing Stop loss limit orders.
{% endhint %}

Bound to - allows linking one order to another so they function as a connected pair (OCO order). User can select an existing order on the same instrument and attach the modified order to it, creating a dependency between them. Linking is only available for orders that match in type and side (Buy/Sell). Orders from other accounts, market orders, and SL/TP orders cannot be linked.

In order to cancel the order, tap the 'Cancel' button.
