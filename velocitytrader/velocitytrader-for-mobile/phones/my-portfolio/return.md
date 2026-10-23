# Return

The “Return, %” tab shows statistics by the portfolio as well as by a single asset/Cash.

<figure><img src="../../../.gitbook/assets/image (570).png" alt=""><figcaption></figcaption></figure>

A user can see two charts which are displayed in one coordinate system:

* chart with markers - shows the “Portfolio monthly return” value since the moment of investment.&#x20;
* histogram (bar chart) - shows Monthly instrument return and Monthly Cash return since the moment of investment.&#x20;

A table with the monthly returns is also available on the Return screen. The following data is displayed in the table:

* Date - the values are displayed for the specified month.
* Portfolio return, % - shows the total Portfolio return in the corresponding month.

Tap the selected number of bars on the histogram to change the data in the table according to the selected month and detailed information about returns by each asset/Cash will be displayed. Selected bars will be highlighted on the histogram.

Above the table a user can see the chosen month and the total Portfolio return. The color scheme of instruments in the table corresponds with the colors of bars on the histogram. The Month return of each instrument is shown next to the instrument name.

In order to go back to the previous model of data display, tap the empty space on the diagram or tap the "X" button near the Portfolio return at the active period.

<figure><img src="../../../.gitbook/assets/image (571).png" alt=""><figcaption></figcaption></figure>

### Calculations

**Monthly portfolio return:**

_Monthly return(i),% = ((EOMPortfolioBalance(i) - Deposits(i) + Withdrawals(i) + Transfers(i) + TransferAndWithdrawal fees(i)  - EOMPortfolioBalance(i-1))/EOMPortfolioBalance(i-1))\*100%_

_Monthly return(i),$ = EOMPortfolioBalance(i) - Deposits(i) + Withdrawals(i) + Transfers(i) + TransferAndWithdrawal fees(i)  - EOMPortfolioBalance(i-1)_

where:

* i - current month;
* EOMPortfolioBalance(i) - the Projected balance value at the end of the current month;
* Deposits - the sum of all Deposit transactions by the account performed since the moment of saving the Projected balance value per month (i-1);
* Withdrawals - the sum of all Withdrawal operations by the account performed since the moment of saving the Projected balance value per month (i-1);
* Transfers - the sum of all Transfer operations by the account performed since the moment of saving the Projected balance value per month (i-1);
* TransferAndWithdrawal fees - the sum of all Transfer fee and Withdrawal fee operations by the account performed since the moment of saving the Projected balance value per month (i-1);
* EOMPortfolioBalance(i-1) - the Projected balance value for the last date of the month that precedes the specified month.

**Monthly instrument return:**

_Monthly instrument return(i) = ((EOMLastPrice(i) - EOMLastPrice(i-1))/EOMLastPrice(i-1))\*100%_

where:

* i - current month;
* EOMLastPrice(i) - the Last price value at the end of the current month;
* EOMLastPrice(i-1) - the Last price at the end of the month that precedes the specified month. If there is no such value, then during the first month the Monthly instrument return will be calculated by the formula:

_Monthly instrument return(i) = ((EOMLastPrice(i) - OpenPrice(i))/OpenPrice(i))\*100%_

**Monthly Cash return:**

_Monthly Cash return(i),% = ((EOMNetCash(i) - Deposits(i) + Withdrawals(i) + Transfers(i) + TransferAndWithdrawal fees(i) + StockOperation(i) - EOMNetCash(i-1))/EOMNetCash(i-1))\*100%_

where:

* i - current month;
* EOMNetCash(i) - the net Cash value at the end of the current month;
* Deposits - the sum of all Deposit transactions by the account performed since the moment of saving the Projected balance value per month (i-1);
* Withdrawals - the sum of all Withdrawal operations by the account performed since the moment of saving the Projected balance value per month (i-1);
* Transfers - the sum of all Transfer operations by the account performed since the moment of saving the Projected balance value per month (i-1);
* TransferAndWithdrawal fees - the sum of all Transfer fee and Withdrawal fee operations by the account performed since the moment of saving the Projected balance value per month (i-1); &#x20;
* StockOperation(i) - the sum of all Stock operations by the account performed since the moment of saving the Projected balance value per month (i-1);
* EOMNetCash(i-1) - the net Cash value at the end of the month that precedes the specified month.
