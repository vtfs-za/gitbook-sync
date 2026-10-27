# Order entry

The Order entry screen enables user to send orders. The Order entry button<img src="../../../.gitbook/assets/1 — копия.png" alt="" data-size="line"> is located at the top right corner of the Chart. Also it is accessible from the main menu of the platform or from the Symbol menu. Swipe left the Symbol name in Watchlist to open Symbol menu and tap Order Entry button:

![](<../../../.gitbook/assets/Screen Shot 2020-06-05 at 5.57.11 PM.png>)

In Order entry users can see detailed information about the traded symbol: symbol name, quantity, order type, price, Validity and information about bid and ask.

<figure><img src="../../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

* Account – the account used for an order creation;
* Symbol – the symbol available for the trade;
* Side – allows to activate Buy or Sell side;
* Quantity / Cash – allows specifying the order's volume in either lots (Quantity) or currency (Cash), depending on the account’s permissions:
  * Quantity - an amount of lots in which an order is placed. Tap the value in order to edit it;
  * Cash - when Cash is selected, the order amount is specified in account currency instead of lots. The estimated quantity (Est. Quantity) will be displayed below this field, showing the approximate number of lots, calculated using the following formula:\
    `Qty = CashOrderQty / ( Order price * Lot size * Сross price)`, where:\
    \- CashOrderQty - cash value entered in account currency;\
    \- Order price - order price depending on its type (_Market_ - current market price; _Limit_ and _Stop Limit -_ limit price; _Stop -_ stop price);\
    \- Lot size - symbol Lot size;\
    \- Cross price - conversion rate from the instrument currency to the account currency.\
    Please note that calculated Est. Quantity value is rounded down to the nearest multiple of the Lot Step (e.g., 0.01). For example if Qty = 0.07692, it will be rounded to 0.07.

**Order type:**

Order type defines the type of the order – Market, Limit, Stop, Stop limit, Trailing stop, OCO:

1\. Market order guarantees execution at a market price.

2\. Limit order is placed with a brokerage to buy or sell a set number of shares at a specified price or better.

3\. Stop order is placed to buy or sell a security when its price surpasses a particular point, thus ensuring a greater probability of achieving a predetermined entry or exit price, limiting the investor's loss or locking in his or her profit.

4\. Stop limit order will be executed at a specified price (or better) after a given stop price has been reached. Once the stop price is reached, the stop-limit order becomes a limit order to buy (or sell) at the limit price or better.

5\. "Sell" trailing stop order sets the stop price at a fixed amount below the market price on the trailing offset. As the market price rises, the stop price rises by the trail amount, but if the stock price falls, the stop loss price doesn't change, and a market order is submitted when the stop price is hit. "Buy" trailing stop orders are the mirror image of sell trailing stop orders.

6\. OCO order is a combined order, where the execution of one automatically cancels the other, allowing to define both a profit-taking target and a protection against loss within a single order. OCO is available only when Stop/Stop Limit and Limit orders are allowed for the selected account and symbol. If Cash mode is selected, the order submission is disabled. By default, the Limit price uses the current Ask for Buy or the current Bid for Sell (otherwise the minimum tick), while the Stop price follows standard Stop price logic.

**Validity:**

Validity – allows specifying order validity by selecting among the following time frames: Day, GTC, IOC, GTD, FOK, GTS. This is especially important for active traders:

1\. Day order, as the name implies, is valid for the current trading day.

2\. GTC (Good till cancelled) orders, on the other hand, will remain alive until they are cancelled.

3\. IOC (Immediate or Cancel Order) requires that all or part of the order be executed immediately after it has been brought to the market.

4\. FOK (Fill or kill) – requires to execute the entire transaction immediately and completely or not to execute it at all.

5\. GTD (Good till date) allows input date until which the order will be cancelled if not executed.

* Overnight execution - if active, the order will be eligible to be placed during overnight market hours. More details can be found [here](../overnight-trading.md).
* SL/TP price – allows to set Stop loss and Take profit prices.

<figure><img src="../../../.gitbook/assets/image (375).png" alt="" width="302"><figcaption></figcaption></figure>

This field can also be displayed as 'SL limit offset', depending on the configuration in [Settings](../settings.md).

If the _Set SL/TP values in offset_ option is enabled in Settings, the SL/TP values will be displayed as offsets. The format of the offset display depends on the _Show offset in_ setting, which allows choosing between: Ticks, Ticks (fractional ticks for Forex), Points and Percents.

If the _Set SL/TP values in offset_ option is disabled, SL/TP values will be displayed as absolute prices instead.

* Trailing SL offset – allows entering the order trailing stop price.

{% hint style="warning" %}
SL price and Trailing SL offset cannot be checked together.
{% endhint %}

* SL trigger/TP trigger - these settings allow a user to select Bid or Ask price for local SL/TP trigger.

<figure><img src="../../../.gitbook/assets/image (1695).png" alt=""><figcaption></figcaption></figure>

6\. GTS (Good till session) order will be cancelled at the end of the trading session if not executed.

**Margin**

Swiping down the "Margin" shade located under the Order entry menu header opens the info menu with the following account parameters:

* Balance – the account's realized balance.
* Available funds – funds available for placing new orders.
* Margin available – margin currently available for trading.
* Incoming funds – total amount of all unsettled deposit operations.
* Impact on funds = After trade funds – Available funds + Total fee;
* Impact on margin – shows the impact of the order fill on Margin available, considering all existing positions/orders. Calculated as:\
  Impact on margin = After trade margin – Margin available + Total fee;
* After trade margin – shows the value of Margin available after the order is filled. Calculated as: After trade margin = Margin available + Impact on margin - Total fee;
* After trade funds – shows value of Available funds remaining after filling the order. Calculated as: After trade funds = Available funds + Impact on funds - Total fee;
* Blocked for stocks – amount reserved from the balance for pre-paid stock margin type instruments.
* Spread initial loss – estimated initial loss on the spread:\
  `(Ask - Bid) * Tick cost * Qty`
* P/L per Tick – displays potential profit/loss per tick:
  * For Futures, Options, Spreadbet: `Tick cost * Qty`
  * For other instruments (except Index): `Tick size * Lot size * Qty * Cross-price`
  * No data for Index instruments.
* Allow short positions – indicates whether short selling is allowed for the instrument.

***

**Fees** section – shows commissions based on the User's commission plan:

* Fill per lot – fee charged for each traded lot.
* Order per lot – fee applied to each lot in the order.
* Fill volume – commission based on the trade’s volume.
* Order volume – fee based on order volume share.
* Per fill – fixed fee per each fill.
* Per transaction – fee applied once per transaction.
* Order per lot with fixed part – fixed fee is charged for the traded volume up to a minimum threshold. If the traded quantity exceeds this volume, an additional fee is applied per each extra lot.
* Fill volume percent with minimum per day – volume-based fee with a guaranteed daily minimum.
* Swap buy – swap value for overnight long positions.
* Swap sell – swap value for overnight short positions.
* Free commission – remaining free commission allowance for the account.
* Total fee – total expected commission for the order.

***

After setting all required parameters, tap the "Send order" button to submit the trade.

**Get snapshot**

This button is intended to get a snapshot of the actual quotes for the current Symbol. After clicking the button, the snapshot window will be opened. The window header displays the time when the snapshot was made, and in the window itself the user can find the following data:

1. Price - displays prices for Symbol in the context of Last/Bid/Ask;
2. Size - volumes for Symbol at the specified Price in the context of Last/Bid/Ask;
3. Change - price change, calculated by the formula _Change = Last price - Previous close_;
4. Change, % - price change as a percentage, calculated by the formula _Change,% = (Last price - Previous close) / Previous close) \* 100%_;
5. Today high - highest price of the day for the current Symbol;
6. Today low - lowest price of the day for the current Symbol;
7. Today volume - current day volume for Symbol.

The "Get snapshot" button allows to update the information in this window.

{% hint style="danger" %}
Please note that if an order is sent outside market hours, a corresponding notification will appear in the panel!
{% endhint %}

### Data source <a href="#data-source" id="data-source"></a>

In the Order entry panel a user can see the the extended information about the source of Last, Bid and Ask prices. In order to open the table with the detailed information, tap the![](<../../../.gitbook/assets/image (547) (1).png>)button and the widget will be shown:

<figure><img src="../../../.gitbook/assets/image (1556).png" alt=""><figcaption></figcaption></figure>
