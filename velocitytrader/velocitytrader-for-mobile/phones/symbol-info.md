# Symbol info

The Symbol info screen allows displaying all information about the selected symbol. To open the Symbol info, tap the <img src="../../.gitbook/assets/image (222).png" alt="" data-size="line"> button at the top right corner of the Chart screen:

<figure><img src="../../.gitbook/assets/image (221).png" alt="" width="375"><figcaption></figcaption></figure>

Information by the symbol is divided into the following groups:

<figure><img src="../../.gitbook/assets/image (1458).png" alt="" width="375"><figcaption></figcaption></figure>

1\) General info:

* Symbol – name of a symbol selected in the lookup;
* Description – detailed information about a symbol;
* Exchange – information about exchange where a current symbol is traded;
* Symbol type – type of symbol traded on a market;
* Last trade date – date when a contract can be traded last time. Available for Forward, Options and Futures;
* Contract month – date of contract expiration. Available for Options and Futures;
* Close-out deadline – date when positions will be closed by a specific symbol. Available for Options and Futures;
* Delivery method – type of asset delivery. Available for Futures, Fixed income, Spot, Forward instruments;
* Settlement system – T+x settlement cycle;
* Asset – displays the Asset assigned to the Instrument, if available. Available for ETFs;
* Exercise style – shows the exercise style. Available for Options. Available styles:
  * European;
  * American;
* Underlier – title of asset which will be delivered. Available for Options, Futures, Spot, T-Bills;
* Maturity date – a security redemption date. Available for Fixed income, Forward, T-Bills;
* Face value – a security's nominal value defined in quoting currency. Available for Fixed income, T-Bills;
* Coupon rate, % – a nominal interest rate for a bond, which is regulated during a bond's emission. Available for Fixed income;
* Coupon cycle – periodicity of a bond yield payment to a position holder. Available for Fixed income;
* Accrued interest – value of accrued interest, which a buyer will pay when buying a Bond, and a seller will get when selling a Bond. Value is indicated for 1 lot. Measured in quotting currency. Available for Fixed income;
* ISIN – International securities identification number;
* Industry – shows the industry identification of a symbol;
* Sector – shows the sector identification of a symbol;
* Days per month - number of days in a month used for interest calculations. Available only for Fixed income. Possible values are: 30, Actual;
* Days per year - number of days in a year used for interest calculations. Available only for Fixed income. Possible values are: 360, Actual.

2\) Trading info:

* Symbol status – the instrument trading status, available values: Open, Closed, Liquidation only. With the symbol status set to Closed, the instrument trading is blocked;
* Allowed operations – New, Modification, Cancel;
* Allowed order types – Market, Limit, Stop, Stop limit, Trailing stop;
* Current session – information on the current trading session period for the instrument;
* Quoting currency – information about currency in which quote is calculated;
* Lot size – amount of base asset for one lot;
* Tick size – minimal change of a price;
* Tick cost – amount of base asset for one tick. Available for Futures CFDs and Futures;
* Minimal lot – the smallest part of lot for which trading is available;
* Maximum lot – the largest trade allowed in lots;
* Maximum lot in cash – the largest allowed trade value in quoting currency;
* Max position qty. – shows maximum quantity of positions per selected symbol;
* Exposure limit – maximum allowed exposure value. Currency is displayed next to the value;
* Lot step – step of lot changes;
* Allow short positions – this parameter shows if it is allowed or not to open short positions by a given instrument;
* High limit – maximum limit price which is set for pending orders, any price higher than the High limit is rejected. Available for Futures CFDs, Futures, Equities, Indices, Crypto and ETF (Exchange traded fund);
* Low limit – minimum limit price which is set for pending orders, any price lower than the Low limit is rejected. Available for Futures CFDs, Futures, Equities, Indices, Crypto and ETF (Exchange traded fund);
* High limit warning – the upper limit of the allowable last price range with last change %. If the value is above it, a user will receive a warning by limit orders;
* Low limit warning – the lower limit of the allowable last price range with last change %. If the value is below it, a user will receive a warning by limit orders;
* Delivery status - status of asset delivery.
* Next holiday – the name of the next holiday and its date.
* Trading blocked on session – shows whether trading is blocked on the current session.
* Easy-to-borrow – ETB means that there’s a supply of stock and generally would be available for short selling.

3\) Margin requirements:

* Margin by account – shows margin requirements based on account coefficients;
* Margin req. – shows margin requirements, which depend on the margin calculation type. When the "None" margin calculation type is selected for the instrument, the "-" is displayed. When the 'Tiered price based custom coeffieicent' margin calculation type is selected, the margin req. values are displayed for all the Tiers set. If initial and maintenance margin coefficients are the same, they will be displayed as one value in the Margin requirements section. The same is true for each Tier. Also the 'Tiered price based custom coef. by group' type can be selected and the the relevant information will be displayed;
* Buy – shows margin requirements for long positions which use different long/short margin and don’t depend on overnight margin;
* Sell – shows margin requirements for short positions which use different long/short margin and don’t depend on overnight margin;
* Day – shows day margin requirements which don’t depend on long/short margin;
* Overnight – shows overnight margin requirements which don’t depend on long/short margin;
* Initial req. – amount of margin which is necessary for trading with one lot;
* Maintenance req. – amount of margin which is necessary for keeping one lot position open;
* Overnight buy – shows coefficients of the initial and maintenance margin for the transfer of long position overnight;
* Overnight sell – shows coefficients of the initial and maintenance margin for the transfer of short position overnight.

{% hint style="warning" %}
If any Time conditions are configured for your margin plan on the server, margin requirements may be displayed separately for each condition. Rows under the default condition are shown as usual, while rows for any other time condition are shown as a separate group with the condition name in brackets next to the row title, e.g. "Tier 1 Day (Weekend Close) – 20 % / 15 % / 10 %".
{% endhint %}

4\) Fees:

The fee value for the fee types such as 'Fill per lot', 'Fill volume, %', 'Per fill', 'Order volume %' and 'Order per lot' can be set depending on quantity ranges.

* Fill per lot (Buy/Sell/Short/Open/Close) – a trader pays fee for each traded lot. Verification of Min. value withdrawal is executed for each fill;
* Per fill – a trader pays fee for each fill of an order;
* Per transaction – a trader pays fee for each transaction. Transactions: place an order, cancel an order, and modify an order;
* Per phone transaction – a trader pays fee for each transaction which was made by Phone dealer;
* VAT – a trader pays VAT from each fee operation;
* Fill volume (Buy/Sell/Short/Open/Close), % – fee calculated on base of the volume of each trade;
* Fill volume (Buy/Sell/Open/Close) with min p/d, % – commission from a volume, which ensures a day minimum in case of partial filling of an order.
* Order volume % (Buy/Sell/Open/Close) – a trader pays fee per each part of order volume that was filled;
* Long swap – shows the swap value applied to overnight long positions of an instrument;
* Short swap – shows the swap value applied to overnight short positions of an instrument;
* Order per lot – a trader pays fee for each traded lot. Verification of Min. value withdrawal is executed for a whole order;
* Custody – displays the Custodial fee measure in basis points (bp) for the Instrument, if available;
* Short position interest, % – shows the interest for short positions value for an instrument (available for Equities, Equities CFD), if available;
* Latest historical long swap – shows the long swap value for the previous day;
* Latest historical short swap – shows the short swap value for the previous day;
* Historical swap last updated on – shows the date of last historical swaps update;
* Option exercise fee (Long) – fee that will be charged on the Long option expiration date, but only if the option has status ‘in-the-money’ by that time. Commission will be charged for the early option execution as well;
* Option exercise fee (Short) – fee that will be charged on the Short option expiration date, but only if the option has status ‘in-the-money’ by that time;
* Order per lot with fixed part – trader pays a fixed fee for trading up to a predefined minimum volume. Once this volume is exceeded, an additional fee per lot is applied to the remaining traded volume.

Rebates:

The rebates value can be set for the fee types such as 'Fill per lot', 'Fill volume, %' depending on quantity ranges.

* Add/Remove liquidity rebate per lot – means that for each lot in an executed trade the fixed rebate value will be charged/returned (in plan's currency);
* Add/Remove liquidity rebate per volume, % – means that charged/returned sum will be calculated as a percent from a trade volume.

5\) Schedule

Information about settings for all trade sessions:

* Before market;
* Pre-market;
* Main;
* Post-market;
* After market.
