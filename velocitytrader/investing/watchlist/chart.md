# Chart

The Chart shows the instrument price change. The Chart screen can be accessed from the Watchlist by tapping the selected Symbol card. Also, it is possible to open a chart from the Positions, Assets and Orders panels by tapping the selected card.

This section allows a user to evoke the Order entry window and remove an instrument from the Watchlist or add it.

<figure><img src="../../.gitbook/assets/image (1219).png" alt="" width="375"><figcaption></figcaption></figure>

Select range by dragging the chart to different directions by 2 fingers.

The horizontal axis of the chart shows the date, the vertical axis shows the Last price of the instrument.

Tap a certain point on a chart to see the following information:

* Close price - Close price at the point selected by a user.
* Change price - the price change from the beginning of the chart to the specified point.

Change price = СP User - СP Start,

where:

_СP User_ - Close price at the point selected by a user.

_СP Start_ - Close price at the start point of the chart.

* Date - date of the selected point.

**Settings**

Tap the ![](<../../.gitbook/assets/image (544).png>) button at the top right corner of the chart to see the settings:

<figure><img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXfIFLA-5SwZN5cN7XhHp4K62fytKHA-Gx8LkuF1dzVvYsyHHXLJ3Eki_vcwoKNJNccwXa1qERM3yI0PJrkAQoRMSKqmsMRB0Q2r49u8x_0sZ-dNpWaHM6EzT32X1tckGy1j1hS9Ta5dwM1wx_Uxc6qIHDQ?key=i34kSG4duM_DXcQbimGXZQ" alt="" width="375"><figcaption></figcaption></figure>

* Watermark mode – drop-down list that allows to select one of the options that will be displayed as a watermark on the chart;
* Watermark color – allows selecting the watermark coloring.

**Comparison**

In order to compare the instruments on one chart in percentage, tap the![](<../../.gitbook/assets/chart (1).png>)button. After tapping this button, a user can see the Symbol lookup which is divided into 2 blocks. One of them shows the list of “Already added” instruments which a user wants to compare. A user can compare only 2 instruments. In the “Common list” block a user can see all instruments except those which will be compared.

<figure><img src="../../.gitbook/assets/image (1175).png" alt="" width="375"><figcaption></figcaption></figure>

In order to confirm selection of instruments which will be compared, click on the “Back” button at the top left corner of the screen ![](../../.gitbook/assets/back.png).

On the chart a user can see the price change in the percentage ratio for the selected period. The following time periods can be set: 1D(Day), 1W(Week), 1M(Month), 1Y(Year), 5Y(Year).

<figure><img src="../../.gitbook/assets/image (1220).png" alt="" width="375"><figcaption></figcaption></figure>

To determine a certain point on the chart, the following formula is used:

<figure><img src="../../.gitbook/assets/fo.png" alt=""><figcaption></figcaption></figure>

where:

* lastPrice(n) - for 1D,1W,1M request - Close price of first minute bar, and for 1Y, 5Y request - Close price of first day bar;
* lastPrice(n+1,2…n) - Close price - the price of the instrument in the next minutes/days after the first received price.

Tapping the chart area evokes a dotted line, that allows a user to understand which point of the chart he is currently watching.

<figure><img src="../../.gitbook/assets/image (1221).png" alt="" width="375"><figcaption></figcaption></figure>

At the top of the dotted line there is information about:\
Change,% on this day for each added instrument in the order how they were added to the “Already added” list. Date of the selected point.

The header displays a legend for the chart as cards. Each card is characterized by: the color of the line on the chart and Symbol name. A user can remove the instrument from the chart by tapping the 'X' button in the instrument card.

**Order entry**

The Order entry screen enables a user to send orders. To open the Order screen with the predefined order side, tap one of the corresponding buttons:

![](<../../.gitbook/assets/3 (84).png>)

Depending on the instrument type, two types of OE can be opened:

* OE for Share - allows a user to buy or sell a whole number of a share;
*   OE for Fractional Share - allows a user to buy or sell a part of a share.\
    <br>

    <figure><img src="../../.gitbook/assets/image (1222).png" alt="" width="375"><figcaption></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (1223).png" alt="" width="375"><figcaption></figcaption></figure>

For Stocks pre-paid & Long options with “Fully paid” margin type the following fields will be available in Order entry:

Estimated cost and Cost - estimated cost of an order in account currency that will be:

* deducted from the user’s balance, while sending Buy order;
* credited, while sending Sell order.

Estimated shares and Shares - estimated amount of shares that will be:

* Bought when sending Buy order with the cash entered in the account currency;
* Sold when sending Sell order with the cash entered in the account currency.

Estimated fees and Fees - estimated sum of fees in account currency.

The “Initial margin” field appears in the panel for instruments with the “Price based custom coef.” margin type. This field shows the estimated price of the order in the account currency, which will be frozen/unlocked in the account margin.
