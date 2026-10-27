# Orders

The Orders screen allows to view three lists of orders:

<figure><img src="../../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>

* Working orders – shows orders that are waiting for execution.
* Filled orders – shows executed orders.
* Orders history – each row displays info regarding creation, modification, execution or cancelling of orders.

Buy orders are displayed in the list with blue arrow, sell orders – with red.

{% hint style="warning" %}
Note that <img src="https://1243456536-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMCqxhh2XAdWPUjcvxR%2Fuploads%2FgQYdawxVLHjG6VvziR8v%2Fimage.png?alt=media&#x26;token=7d92dda6-08fa-4771-8dbc-acddb2e9cfb7" alt="" data-size="line"> icon means that order is eligible to be executed during overnight market hours. Read about overnight trading in more details [here](overnight-trading.md).
{% endhint %}

All working orders can be canceled at once with a special button that is disabled in the app by default. This feature can be useful for managers or admins, in case there is a need to cancel all currently working orders. The "Cancel all" button is securely hidden in the Account menu to prevent accidental pressing. In order to enable this feature, please contact our support.

Each section consists of the cards list with short information about the orders: for Working orders – symbol name, quantity, open price, order type; for Filled orders – symbol name, order type, Net P/L, quantity. In order to get full information about the symbol on which the order was created, tap the symbol name.

* Date/Time – date and time when the order was placed (executed, filled, modified, or cancelled).
* Current price – market price obtainable from broker.
* Stop price – stop price for special Stop and Trailing stop orders.
* Validity – allows specifying order validity by selecting among the following time frames: Day, GTC, IOC, GTD, FOK, GTS.
* Order ID – unique number that the trading system assigns to each order. If a position is opened based on an order, the position will have the same number.
* Stop loss – stop loss price set for the order.
* Take profit – take profit price set for the order.
* Qty. remaining – difference between quantity and executed quantity when only part of the order was executed.
* Qty. filled - executed quantity of the order when only part of the order was executed.
* Status - status of the current order. It can have the following values: Pending new, Pending execution, Pending cancel, Pending modification, Created, Accepted, Partially filled, Waiting for market, Waiting cancellation, Off market, Unplaced;
* SL/TP offset - shows the order offset in ticks, fractional ticks, points or percentage (depending on the current configuration of the Trading defaults section of the General settings);
* Strategy ID – identifier of an execution strategy that placed order;
* Bound to – ID of the order which another order is bound to; if the former is executed, system will cancel the latter;
* Avg. price – shows the average execution price calculated across all fills of the order;
* Account – login name of the account that opened the order.

Additional columns for Filled orders section:

* Trade ID – unique number of the trade.
* Exposure – quantity recalculated in account currency.
* Fee – shows commission connected with the trade.
* Bought – if Side = Buy, then this column shows the value of Price \* Lot size \* Qty in base currency; if Side = Sell, then this column shows the value of Price \* Lot size \* Qty in quoting currency.
* Sold – if Side = Sell, then this column shows the value of Price \* Lot size \* Qty in base currency; if Side = Buy, then this column shows the value of Price \* Lot size \* Qty in quoting currency.
* Trade volume – shows total volume of the trade.
* Price – shows price for Market and Limit orders, and Limit price for Stop limit orders.
* Gross P/L – total profit/loss of the trade.

{% hint style="warning" %}
Please note, that for Filled orders you can also see Total profit in the lower part of the table.
{% endhint %}

Note that the following icon ![](<../../.gitbook/assets/image (92).png>) will be displayed near the Linked order.

Filled orders and Orders history sections can be viewed by selected date range, available values here are: daily, two days to date, week to date, month to date. To choose the date range, tap the button <img src="../../.gitbook/assets/image (1560).png" alt="" data-size="line">.

<figure><img src="../../.gitbook/assets/image (1561).png" alt=""><figcaption></figcaption></figure>

In order to modify active order, tap the ‘Modify’ button and the following screen will be opened:

<figure><img src="../../.gitbook/assets/image (1562).png" alt=""><figcaption></figcaption></figure>

Here user can modify price, quantity, Validity, Stop loss, Trailing, and Take profit. In addition, order can be executed at a market price.

{% hint style="warning" %}
If Stop limit order is activated, the Stop price field will be disabled in Modify screen. Thus, only Limit price can be modified. The same is true for closing Stop loss limit orders.
{% endhint %}

Bound to - allows linking one order to another so they function as a connected pair (OCO order). User can select an existing order on the same instrument and attach the modified order to it, creating a dependency between them. Linking is only available for orders that match in type and side (Buy/Sell). Orders from other accounts, market orders, and SL/TP orders cannot be linked.

In order to cancel the order, tap the 'Cancel' button.
