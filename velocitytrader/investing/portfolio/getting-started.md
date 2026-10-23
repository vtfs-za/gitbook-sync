# Getting started

The Portfolio functionality allows an Investor to monitor and control profit and risks in his portfolio to get subsequent income. The Portfolio screen is shown immediately after opening the Investing application.

<figure><img src="../../.gitbook/assets/image (81).png" alt="" width="375"><figcaption></figcaption></figure>

At the top of the screen a user can see the informational card that displays info about the account selected in the Account lookup.

<figure><img src="../../.gitbook/assets/image (1200).png" alt="" width="531"><figcaption></figcaption></figure>

* **Pending cash** shows Projected balance(Balance+ unrealized P/L).&#x20;
* **Today return** value is located next to Pending cash. It shows the percentage of growth/drawdown of Pending cash compared to the last trading day. Calculations:

![](<../../.gitbook/assets/2 (168).png>)

where:&#x20;

_**CurrentProjectedBalance**_ - current value of Projected balance by the account;&#x20;

_**Deposit**_ - the sum of all Deposit transactions by the account performed after the time when the last value of the Projected balance was saved.&#x20;

_**Balance credit**_ - the sum of all Balance credit transactions by the account performed after the time when the last value of the Projected balance was saved.&#x20;

_**|Withdrawals|**_ - modulus of the sum of all Withdrawal transactions by the account performed after the time when the last value of the Projected balance was saved.&#x20;

_**|Balance debit|**_ - modulus of the sum of all Balance debit transactions by the account performed after the time when the last value of the Projected balance was saved.&#x20;

_**Transfers**_ - the sum of all Transfer transactions by the account performed after the time when the last value of the Projected balance was saved.&#x20;

_**Adjustment**_ - the sum of all Adjustment transactions by the account performed after the time when the last value of the Projected balance was saved.&#x20;

_**|TransferAndWithdrawal fees|**_ - the sum of all Transfer fee and Withdrawal fee transactions by the account performed after the time when the last value of the Projected balance was saved.&#x20;

_**LastProjectedBalance**_ - the last value of the Projected balance saved to the database for the account by the Investing maintenance scheduler task. If the LastProjectedBalance value = 0, then use the following formula to calculate the Today return value:

![](<../../.gitbook/assets/3 (57).png>)

where:&#x20;

II - investment income for the current day can be calculated by the following formula:&#x20;

II = CurrentProjectedBalance + (|Withdrawals|+|Balance debit| - Transfers -Adjustment + |TransferAndWithdrawal fees| - Deposit-Balance credit)

* **Open P/L** - Net profit or loss for all open positions and assets.&#x20;
* **Available cash (Available funds)** - the amount of funds to place new orders.&#x20;
* ![](<../../.gitbook/assets/image (535).png>) **button** allows hiding the following values: Pending cash, Open PnL, Available funds.
*   ![](<../../.gitbook/assets/image (536).png>) **button** allows opening a chart that shows the growth/drawdown of Pending cash. Tap the<img src="../../.gitbook/assets/image (537).png" alt="" data-size="original">**button** to close the chart.<br>

    <figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXc1tqVdGz0Qvl8LqXgps3qclIJZkrk9BbVmyRhrSGmMV8Bc_XHGzNJMGpT6oRTefVt4jSd2uzvAV3agwt0FQF2BNY0-erg4TsjWJgMYCxHoj2qC169EkG5NeHATbUl-Sx8redCZ3rjz8ZE2i06A9G9aSsw?key=i34kSG4duM_DXcQbimGXZQ" alt="" width="375"><figcaption></figcaption></figure>

The horizontal axis shows the date, the vertical axis shows the percentage change of the Cumulative daily return value.

**Pie chart**\
The pie chart displays the percentage ratio of all open positions by instrument types.

![](<../../.gitbook/assets/3 (11).png>)

The number of chart sectors corresponds to the number of instrument types included in the portfolio, as well as Cash. The percentage of each instrument type in the portfolio is calculated by the following formula:

![](<../../.gitbook/assets/4 (32).png>)



where:

-i - instruments of the same type in the investor's portfolio, i = 1...n, n - number of instruments of the same type in the portfolio&#x20;

-∑Position value(i) - total value of all positions of the same instrument type in the portfolio.&#x20;

-Projected balance - future, estimated balance of the account with accrued and unaccrued profits/losses. Percentage of Cash in the portfolio:

![](<../../.gitbook/assets/5 (44).png>)

In the center of the diagram a user can see the value of the largest share of the instrument type in the portfolio in percentage, and the instrument type. Next to the pie chart a user can see the list of instrument types included in the portfolio. The colors of the instrument types correspond to the colors of chart sectors.

Under the diagram a user can find the following tabs: Positions, Positions balance, Assets, Orders, Operations.

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdeSXVM0yoTp0TYIt4t0aHtoVqY4Ljwj5kYvrv_2mG4oGF8wl2FdeUNFQFp9AMI9xfSYqvvQHpssvUOGNq3twgAxZzPTGpF_pCEQiUlHCbB-ZjAd7ATEHUpjxglp7U-o39PijlI-LWPrOTRszv0NDKW8Q?key=i34kSG4duM_DXcQbimGXZQ" alt="" width="375"><figcaption></figcaption></figure>
