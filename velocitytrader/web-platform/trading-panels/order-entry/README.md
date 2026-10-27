# Order entry

Order entry panel allows to place market or pending orders. To open the Order entry panel select Terminal -> Order entry.

<figure><img src="../../../.gitbook/assets/image (1745).png" alt=""><figcaption></figcaption></figure>

This panel contains the following settings:

* Symbol – the symbol available for the trade;
* Side – allows to activate Buy or Sell side;
* Quantity / Cash – allows specifying the order's volume in either lots (Quantity) or currency (Cash), depending on the account’s permissions:
  * Quantity - the volume is set in lots. A ![](<../../../.gitbook/assets/image (1245).png>) button next to the field lets you select from preset default values in a dropdown list. The `Set defaults` option opens the Types Manager panel, where you can modify these default values;
  * Cash - when Cash is selected, the order amount is specified in account currency instead of lots. The estimated quantity (Est. Quantity) will be displayed below this field, showing the approximate number of lots, calculated using the following formula:\
    `Qty = CashOrderQty / ( Order price * Lot size * Сross price)`, where:\
    \- CashOrderQty - cash value entered in account currency;\
    \- Order price - order price depending on its type (_Market_ - current market price; _Limit_ and _Stop Limit -_ limit price; _Stop -_ stop price);\
    \- Lot size - symbol Lot size;\
    \- Cross price - conversion rate from the instrument currency to the account currency.\
    Please note that calculated Est. Quantity value is rounded down to the nearest multiple of the Lot Step (e.g., 0.01). For example if Qty = 0.07692, it will be rounded to 0.07.
* Leverage – contains leverage value, if applicable;
* Order type – defines the type of the order: Market, Limit, Stop, Stop limit, Trailing stop, Care, OCO:

1. Market order is an order to buy or sell a security at the best available price immediately;
2. Limit order is placed to buy or sell a security at specified price or better;
3. Stop order is placed to buy or sell a security when its price surpasses a particular point, thus ensuring a greater probability of achieving a predetermined entry or exit price, limiting the investor's loss or locking in his or her profit. The<img src="../../../.gitbook/assets/info web.png" alt="" data-size="original">icon informs a user that additional Limit price is available if the checkbox 'Use stop limit instead of stop' is active in General settings;
4. Stop limit order will be executed at a specified price (or better) after given stop price has been reached. Once the stop price is reached, the Stop limit order becomes a Limit order to buy (or sell) at the limit price or better;
5. OCO (One-Cancels-the-Other) is an order stipulating that if one part of the order is executed, then the other part is automatically canceled;
6. Care order is a type of Limit order with expanded customization and flexibility. With Care orders, an Order entry panel includes an additional "Comment" field of up to 128 characters, allowing the user to provide specific information to the broker. Please note that Care orders may include an additional commission, which will be transparently displayed in fee breakdowns and margin calculations;
7. ‘Sell’ trailing stop order sets the stop price at a fixed amount below the market price on the trailing offset. As the market price rises, the stop price rises by the trail amount, but if the stock price falls, the stop loss price doesn't change, and a market order is submitted when the stop price is hit. ‘Buy’ trailing stop orders are the mirror image of sell trailing stop orders;

* Validity – allows specifying order validity by selecting among the following time frames: Day, GTC, IOC, GTD, FOK, GTS. This is especially important for active traders:

1. A Day order, as the name implies, is valid for the current trading day;
2. GTC (Good till cancelled) orders, on the other hand, will remain alive until they are cancelled or the contract expires;
3. IOC (Immediate or cancel) requires the whole or part of the order to be executed immediately after it has been brought to the market;
4. FOK (Fill or kill) requires to execute the entire transaction immediately and completely or not to execute it at all;
5. GTD (Good till date) order will be cancelled on specified date if not executed or until the contract expires;
6. GTS (Good till session) order will be cancelled at the end of the trading session if not executed.

* Overnight execution - allows user to place orders that can be executed outside of regular market hours. If enabled, the order will be eligible for overnight execution. If disabled, the order will be executed only during standard trading hours. Please note that this option is shown only if overnight trading is available for your account and the selected instrument. Stop Loss and Take Profit orders will automatically inherit this setting;
* Stop price (for the ‘Stop order’ type) – allows entering the order stop price;
* Limit price (available together with Stop price for the ‘Stop order’ and ‘OCO’ order types; also available for the ‘Limit order’ type) – allows entering the order limit price;
* Tr. stop offset (for the ‘Trailing stop’ type) – allows entering the order trailing stop price.
* Comment - a field where you can provide additional details or instructions for the order. Maximum length is 128 characters. Available only for Care order type.

You can set up set the Stop loss and Take profit directly from the Order entry panel if needed.

<figure><img src="../../../.gitbook/assets/image (1746).png" alt=""><figcaption></figcaption></figure>

When icon is activated by clicking on it, and checkbox 'Use stop limit instead of stop' is true (a setting located in Trading defaults tab of General settings), the additional field 'SL limit price' will appear. It shows Limit price which is set for SL order. This field can also be displayed as 'SL limit offset', depending on the configuration in [General settings](../../getting-started/general-settings.md).

If the _Set SL/TP values in offset_ option is enabled in General settings, the SL/TP values will be displayed as offsets. The format of the offset display depends on the _Show offset in_ setting, which allows choosing between: Ticks, Ticks (fractional ticks for Forex), Points and Percents.

If the _Set SL/TP values in offset_ option is disabled, SL/TP values will be displayed as absolute prices instead.

It is always possible to manage risks by setting Trailing stop on the order by clicking on a special<img src="../../../.gitbook/assets/3 (131).png" alt="" data-size="original">button located near Stop loss. The blue color of the<img src="../../../.gitbook/assets/4 (92).png" alt="" data-size="original"> button indicates that the Trailing stop is activated.

It's also possible to set the validity separately for SL/TP if the _Select SL/TP validity in OE_ parameter is activated in the General settings.

* SL trigger/TP trigger - these settings allow a user to select Bid or Ask price for local SL/TP trigger.
* Get snapshot - this button is intended to get a snapshot of the actual quotes for the current Symbol. After clicking the button, the snapshot window will be opened. The window header displays the time when the snapshot was made, and in the window itself the user can find the following data.

1. Price - displays prices for Symbol in the context of Last/Bid/Ask;
2. Size - volumes for Symbol at the specified Price in the context of Last/Bid/Ask;
3. Change - price change, calculated by the formula _Change = Last price - Previous close_;
4. Change, % - price change as a percentage, calculated by the formula _Change,% = (Last price - Previous close) / Previous close) \* 100%_;
5. Today high - highest price of the day for the current Symbol;
6. Today low - lowest price of the day for the current Symbol;
7. Today volume - current day volume for Symbol.

The "Get snapshot" button allows to update the information in this window.

Order entry panel has the additional VWAP section which displays important information. VWAP section allows displaying VWAP prices section (Bid, Spread, Ask) in the Order entry panel.

![](<../../../.gitbook/assets/5 (49).png>)

* Margin section - allows displaying Margin section in the Order entry panel.

The **Margin** section is divided into two parts: Risks and Fees.

Risks details section shows all values in account currency:

* Balance - an account's balance;
* Available funds – amount of funds for placing new orders;
* Margin available – available margin for trading;
* Incoming funds – the total amount of all unsettled Deposit account operations in the account currency;
* Impact on funds – shows the impact of the order fill on Available funds, considering all existing positions/orders. Calculated as:\
  Impact on funds = After trade funds – Available funds + Total fee;
* Impact on margin – shows the impact of the order fill on Margin available, considering all existing positions/orders. Calculated as:\
  Impact on margin = After trade margin – Margin available + Total fee;

When the 'Tiered price based custom coeffieicent' margin calculation type is selected for the symbol, the margin req. values are displayed for all the Tiers set

* After trade margin – shows the value of Margin available after the order is filled. Calculated as: After trade margin = Margin available + Impact on margin - Total fee;
* After trade funds – shows value of Available funds remaining after filling the order. Calculated as: After trade funds = Available funds + Impact on funds - Total fee;
* Blocked for stocks – amount of funds debited from the balance in the case of trading with symbols with Stocks pre-paid margin type;
* Spread initial loss – shows initial loss on the spread:

Spread initial loss = (Ask - Bid) \* Tick cost \* Qty.

* P/L per Tick – displays data for Symbols:

P/L per Tick = Tick cost \* Qty - if a Symbol type is one of these: Futures, Options, Spreadbet;

P/L per Tick = Tick size \* Lot size \* Qty \* Cross-price **-** if a Symbol type is NOT one of these: Futures, Options, Spreadbet, Index;

P/L per Tick - no information for Index;

* Allow short positions – shows whether short positions opening is allowed for the symbol;
* Est. available cash - displays the calculated cash balance after placing an order, calculated as:\
  Est. available cash = Available Cash + OE Order Value + Order fees.\
  Note that the value can be negative and is shown in red or green depending on the balance.

**Fees** part shows commission for a trade. The fees shown depend on the Commission plan settings of the User:

* Fill per lot – shows the fee paid for each traded lot.
* Total fee – shows the commission total on the trade.
* Swap buy - specifies a swap value that is applied to overnight long positions of an instrument.
* Swap sell - specifies a swap value that is applied to overnight short positions of an instrument.
* Total fee – total expected commission for the trade, aggregated from all applicable components.
* Per fill – fixed fee charged per each trade fill, regardless of volume.
* Per transaction – fixed fee charged per transaction.
* Order per lot with fixed part – fixed fee is charged for the traded volume up to a minimum threshold. If the traded quantity exceeds this volume, an additional fee is applied per each extra lot.

Information of the Margin section can be updated by clicking on the button ![](<../../../.gitbook/assets/image (1450).png>) at the right corner at the bottom of the Margin section, or by default it is updated every 30 seconds.

The "Attach" button can be found by clicking the "View more actions" button ![](<../../../.gitbook/assets/image (1451).png>) at the right side of the panel heade. It allows attaching the OE panel:

<figure><img src="../../../.gitbook/assets/image (1452).png" alt=""><figcaption></figcaption></figure>

After clicking, the panel will be attached to the right side of the screen, hover the mouse over the required tab to expand the Order entry:

<figure><img src="../../../.gitbook/assets/image (251).png" alt=""><figcaption></figcaption></figure>

A user can click and drag the border of the panel to resize it to desired width.

Each of these panels can be detached or closed by clicking the corresponding button in the panel header. The attachment is available for both locked and non-locked workspaces.

{% hint style="warning" %}
Please note, that the User can have no more then 3 panels attached to the current workspace, otherwise the "Attach' button will be unavailable.
{% endhint %}

Order entry panel can also be closed with the "Esc" hotkey when it is in focus.

{% hint style="danger" %}
Please note that if an order is sent outside market hours, a corresponding notification will appear in the panel!
{% endhint %}

### Data source

In the Order entry panel a user can see the the extended information about the source of Last, Bid and Ask prices. In order to open the table with the detailed information, click on the<img src="../../../.gitbook/assets/Screenshot_11.png" alt="" data-size="original">button and the widget will be shown:

![](<../../../.gitbook/assets/Screenshot_5 — копия.png>)
