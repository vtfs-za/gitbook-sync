# Metrics

The Metrics screen shows the Portfolio statistics. A user can see here the invested amount of funds, arithmetic mean income for different time periods, the best year result, the worst year result (considering profit), etc.The statistics data is displayed as cards with a metric name and its value.

<figure><img src="https://822159123-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LMCqxhh2XAdWPUjcvxR%2F-MVqbYbO0y5Qt2Lmp4uk%2F-MVqc92aqhO07CPdqkhz%2F1.png?alt=media&#x26;token=81754aae-5ed0-4355-b969-f89d03d6ac91" alt=""><figcaption></figcaption></figure>

The default list of metrics includes the following:

* Invested amount - invested amount of funds;
* Portfolio balance - future settlement account balance considering accrued and non-accrued profits and losses;
* Holding period rate of return - portfolio return since the moment of investment;
* Max drawdown - the maximum drawdown value. The drawdown value is calculated by the formula:

_**Drawdown(i),% = (EODPortfolioBalance(i) — max(PortfolioBalance)/max(PortfolioBalance))\*100%**_&#x77;here:

* i - current day;
* EODPortfolioBalance(i) - the Projected balance value at the end of the current day;
* max(PortfolioBalance) - the maximum Projected balance value for the corresponding account.

The drawdown value can be calculated by the above-mentioned formula if:_**EODPortfolioBalance(i) < max(PortfolioBalance)**_&#x4F;therwise, the PortfolioBalance value grows, and the drawdown is equal to 0.00%.If you don’t need any metric, you can remove it by swiping the card left and tapping the “Remove” button.

<figure><img src="https://822159123-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LMCqxhh2XAdWPUjcvxR%2F-MVqbYbO0y5Qt2Lmp4uk%2F-MVqcK7moih5bqnp2m0a%2F2.png?alt=media&#x26;token=054dfa89-aa90-4e40-bf41-5fe995dbb478" alt=""><figcaption></figcaption></figure>

Other metrics can be added optionally. To add a metric, tap thebutton located above the metrics list and select preferred metrics.

<figure><img src="https://822159123-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LMCqxhh2XAdWPUjcvxR%2F-MVqbYbO0y5Qt2Lmp4uk%2F-MVqcYqerNRDuZ1NtBvu%2F3.png?alt=media&#x26;token=6fc3907f-e6ad-4f96-81cb-57d74c9476d2" alt=""><figcaption></figcaption></figure>

“Best month” and “Worst month” metrics are the maximum and the minimum values of Monthly return which is calculated by the following formulas:_**Monthly return(i),% = ((EOMPortfolioBalance(i) - Deposits(i) + Withdrawals(i) + Transfers(i) + TransferAndWithdrawal fees(i) - EOMPortfolioBalance(i-1))/EOMPortfolioBalance(i-1))\*100%Monthly return(i),$ = EOMPortfolioBalance(i) - Deposits(i) + Withdrawals(i) + Transfers(i) + TransferAndWithdrawal fees(i) - EOMPortfolioBalance(i-1)**_&#x77;here:

* i - current month;
* EOMPortfolioBalance(i) - the Projected balance value at the end of the current month;
* Deposits - the sum of all Deposit transactions by the account performed since the moment of saving the Projected balance value per month (i-1);
* Withdrawals - the sum of all Withdrawal operations by the account performed since the moment of saving the Projected balance value per month (i-1);
* Transfers - the sum of all Transfer operations by the account performed since the moment of saving the Projected balance value per month (i-1);
* TransferAndWithdrawal fees - the sum of all Transfer fee and Withdrawal fee operations by the account performed since the moment of saving the Projected balance value per month (i-1);
* EOMPortfolioBalance(i-1) - the Projected balance value for the last date of the month that precedes the specified month.

On the list of cards you can see total metrics by the Portfolio. Tap the certain card to watch data by each asset.
