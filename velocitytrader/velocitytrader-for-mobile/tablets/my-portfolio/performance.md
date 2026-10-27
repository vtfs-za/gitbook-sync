# Performance

The Performance screen is accessible by default after opening the “My Portfolio” functionality.

![](<../../../.gitbook/assets/1 (129).png>)

### Account lookup

If a user has several Investor accounts, he can choose a certain account by tapping the Account lookup which is displayed instead of the “My Portfolio” header, and select the preferred account from the list.

![](<../../../.gitbook/assets/image 3.png>)

### Diagrams

The following types of diagrams are displayed:

* Pie chart - shows the amount of funds that were invested into the Portfolio considering “Portfolio balance” as well as “Holding period rate of return” from the moment of investment.
* Doughnut chart - shows the “Portfolio allocation” values. The number of chart sectors corresponds to the number of assets in the portfolio as well as Cash. If there is no portfolio (positions) at the account, the chart will be plain and Cash will be displayed. The allocation will be dynamic as it will be built by the current investor’s portfolio.

### Cards

Under the diagram a user can find cards that show assets/cash included in the portfolio.

![](<../../../.gitbook/assets/image 7.png>)

The following information is displayed on each card:

* asset name;
* instrument description;
* money equivalent of the asset share in the portfolio (Stock value);
* money equivalent of the Cash share in the portfolio is calculated by the formula:

_Cash value in portfolio,$ = ProjectedBalance - sum(StockValue)_

To open full information by the asset/Cash, tap the corresponding card.

![](<../../../.gitbook/assets/3 (8).png>)

* Holding period rate of return, % - chart shows the rate of return by a single asset/Cash since the moment of investment by days.

**Calculations:**

Daily instrument returns/Daily cash return – daily profitability for the instrument and free cash, respectively. The following formulas are used to calculate the these values:

**Daily Cash return:**

_Daily Cash return(i),% = ((EODNetCash(i) - Deposits(i) + Withdrawals(i) + Transfers(i) + TransferAndWithdrawal fees(i) + StockOperation(i) - EODNetCash(i-1))/EODNetCash(i-1))\*100%_

where:

* i - current day;
* EODNetCash(i) - the net Cash value at the end of the current day;
* Deposits - the sum of all Deposit transactions by the account performed since the moment of the last entry of the Projected balance value in the database;
* Withdrawals - the sum of all Withdrawal operations by the account performed since the moment of the last entry of the Projected balance value in the database;
* Transfers - the sum of all Transfer operations by the account performed since the moment of the last entry of the Projected balance value in the database;
* TransferAndWithdrawal fees - the sum of all Transfer fee and Withdrawal fee operations by the account performed since the moment of the last entry of the Projected balance value in the database;
* StockOperation(i) - the sum of all Stock operations by the account performed since the moment of the last entry of the Projected balance value in the database;
* EODNetCash(i-1) - the net Cash value at the end of the day that precedes the current day.

**Daily instrument return:**

_Daily instrument return(i) = ((EODLastPrice(i) - EODLastPrice(i-1))/EODSLastPrice(i-1))\*100%,_

where:

* i - current day;
* EODLastPrice (i) - Last price value at the end of the current day;
* EODLastPrice (i-1) - Last price value for the last day before the current date.

If there is no previous value, then for the first day of investment, the formula will be the following:

_Daily instrument return(i) = ((EODLastPrice(i) - OpenPrice(i))/OpenPrice(i))\*100%_

* Symbol type - shows the type of the traded symbol.
* Trading exchange - shows a trading exchange where the instrument is traded.
* Target allocation - shows a target allocation. The allocation is taken from the model which is assigned to the account.
* Current price - shows a current market price.
* Quantity - shows quantity in lots.

The colors of the cards correspond to the colors of chart sectors. Tap a certain card to see the share of the asset/Cash in the portfolio on the diagram.
