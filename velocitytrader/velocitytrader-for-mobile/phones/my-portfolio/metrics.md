# Metrics

The Metrics screen shows the Portfolio statistics. A user can see here the invested amount of funds, arithmetic mean income for different time periods, the best year result, the worst year result (considering profit), etc.

The statistics data is displayed as cards with a metric name and its value.   &#x20;

<figure><img src="../../../.gitbook/assets/image (565).png" alt=""><figcaption></figcaption></figure>

The default list of metrics includes the following:

* Invested amount - invested amount of funds;
* Portfolio balance - future settlement account balance considering accrued and non-accrued profits and losses;
* Holding period rate of return - portfolio return since the moment of investment;&#x20;
* Max drawdown - the maximum drawdown value. The drawdown value is calculated by the formula:

_**Drawdown(i),% = (EODPortfolioBalance(i) — max(PortfolioBalance)/max(PortfolioBalance))\*100%**_

where:

* i - current day;
* EODPortfolioBalance(i) - the Projected balance value at the end of the current day;
* max(PortfolioBalance) - the maximum Projected balance value for the corresponding account.

The drawdown value can be calculated by the above-mentioned formula if:

_**EODPortfolioBalance(i) < max(PortfolioBalance)**_

Otherwise, the PortfolioBalance value grows, and the drawdown is equal to 0.00%.

If you don’t need any metric, you can remove it by swiping the card left and tapping the “Remove” button.&#x20;

<figure><img src="../../../.gitbook/assets/image (566).png" alt=""><figcaption></figcaption></figure>

Other metrics can be added optionally. To add a metric, tap the<img src="https://lh3.googleusercontent.com/mwLy9VITx37fqqx78IPkbg8LIQm7NW12PU4iTYLnj9BRRvbg9mIKTgHkaE696gb-rnKmAtYrZslF1KoooqA3nC8nw6ub6ZLx98eo26km1amPtLXbNVm1gztMX_osUSY3v7q-98yC" alt="" data-size="line">button located above the metrics list and select preferred metrics.&#x20;

<figure><img src="../../../.gitbook/assets/image (567).png" alt=""><figcaption></figcaption></figure>

“Best month” and “Worst month” metrics are the maximum and the minimum values of Monthly return which is calculated by the following formulas:

_**Monthly return(i),% = ((EOMPortfolioBalance(i) - Deposits(i) + Withdrawals(i) + Transfers(i) + TransferAndWithdrawal fees(i)  - EOMPortfolioBalance(i-1))/EOMPortfolioBalance(i-1))\*100%**_

_**Monthly return(i),$ = EOMPortfolioBalance(i) - Deposits(i) + Withdrawals(i) + Transfers(i) + TransferAndWithdrawal fees(i)  - EOMPortfolioBalance(i-1)**_

where:

* i - current month;
* EOMPortfolioBalance(i) - the Projected balance value at the end of the current month;
* Deposits - the sum of all Deposit transactions by the account performed since the moment of saving the Projected balance value per month (i-1);
* Withdrawals - the sum of all Withdrawal operations by the account performed since the moment of saving the Projected balance value per month (i-1);
* Transfers - the sum of all Transfer operations by the account performed since the moment of saving the Projected balance value per month (i-1);
* TransferAndWithdrawal fees - the sum of all Transfer fee and Withdrawal fee operations by the account performed since the moment of saving the Projected balance value per month (i-1);
* EOMPortfolioBalance(i-1) - the Projected balance value for the last date of the month that precedes the specified month.

On the list of cards you can see total metrics by the Portfolio. Tap the certain card to watch data by each asset.

<figure><img src="../../../.gitbook/assets/image (568).png" alt=""><figcaption></figcaption></figure>
