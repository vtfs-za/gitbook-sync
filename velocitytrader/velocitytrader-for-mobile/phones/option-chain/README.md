# Option chain

The Option chain screen shows detailed information about a specific option contract and allows a user to trade from this panel.

<figure><img src="../../../.gitbook/assets/image (1697).png" alt="" width="375"><figcaption></figcaption></figure>

Swipe left the instrument at the Watchlist screen and select the corresponding item to open the Option chain panel.

<figure><img src="../../../.gitbook/assets/image (1516).png" alt="" width="375"><figcaption></figcaption></figure>

{% hint style="warning" %}
To call the Context menu, press and hold (Long tap) on the needed item.
{% endhint %}

Actions available in the Context menu:

* Chart - by tapping, the Chart with the selected symbol will be opened;
* Symbol info - tap and detailed description of the symbol will be opened;
* Add to watchlist - allows adding selected symbol to the Watchlist;
* Remove - deletes the item from the Option chain.

Under the header of the Option chain screen a user can see the Info bar which displays the following data:

* Last - last price by underlier;
* Change, % - change in percentage by underlier;
* Volume - volume by underlier;
* Previous close - the previous day's close price.

The Option chain table contains 3 columns:

* Calls - this column shows the cards of Call strikes that display the following information: Ask, Bid, IV, OI (Open interest), Change. Other parameters can be configured in the Panel settings;
* Strike - the Strike price;
* Puts - this column shows the cards of Put strikes that display the following information: Ask, Bid, IV, OI, (Open interest), Change. Other parameters can be configured in the Panel settings.

In Option chain panel the coloring method “By difference” is used. Depending on what type of price change comes at a certain strike to buy or sell, it is highlighted in green or red.

IV (Implied volatility) column shows the expected volatility of the option which characterizes the degree of underlier price volatility. If IV is high, strong fluctuations of underlier price are expected.

The Open interest column shows the total amount of open positions.

{% hint style="warning" %}
![](<../../../.gitbook/assets/image (17).png>) - Indicates that multiple option contracts with the same strike price exist within the series. When hovered, displays additional information about the strike version, including the Underlier and Version (if specified).
{% endhint %}

The undermentioned screenshot shows the filter by the number of displayed strikes:

<figure><img src="../../../.gitbook/assets/image (1519).png" alt="" width="375"><figcaption></figcaption></figure>

Tap Ask or Bid button on the Option chain screen to select the strike (Leg). It is possible to select several strikes. Tap one more time to delete the Leg from selected ones. Orders can be added to the strategy from different option series for a given underlier.

<figure><img src="../../../.gitbook/assets/image (1520).png" alt="" width="375"><figcaption></figcaption></figure>

At the bottom of the screen there is a panel <img src="../../../.gitbook/assets/image (1521).png" alt="" data-size="line"> that gives the opportunity to select different option strategies. Learn more about each available strategy in the following [Option strategies](option-strategies.md) article.

Also there is a information about the number of selected strikes:

<figure><img src="../../../.gitbook/assets/image (1522).png" alt=""><figcaption></figcaption></figure>

The following buttons are also available here:\
<img src="../../../.gitbook/assets/image (1523).png" alt="" data-size="line"> - allows removing all selected Legs;

<img src="../../../.gitbook/assets/image (1525).png" alt="" data-size="line"> - allows opening the Order entry screen;

<img src="../../../.gitbook/assets/image (1524).png" alt="" data-size="line"> - allows opening the Analyzer screen.

### Analyzer

By tapping <img src="../../../.gitbook/assets/image (1524).png" alt="" data-size="line"> button, a user will get to the graphical data section:

<figure><img src="../../../.gitbook/assets/image (1526).png" alt="" width="375"><figcaption></figcaption></figure>

“Legs” section displays the list of orders. Tap <img src="../../../.gitbook/assets/image (1527).png" alt="" data-size="line"> button to show/hide this section. Tap the “Add underlier” button to add a Leg by underlier. The following parameters are available for viewing:

* Intrinsic P/L - profit calculated by the Expiration curve;
* P/L - profit calculated by the Current curve;
* What if - profit calculated by the Timeline curve;
* Potential gain - the largest positive P/L value for the total profile;
* Potential loss - minimum negative P/L value for the total profile.

Greeks are the coefficients used for the characteristics of option cost sensitivity to the changing of various values: Delta, Gamma, Vega and Theta.

* Delta – is the first derivative of the option price by the underlier price; shows how option price will be changed in points, if the underlier price changes by 1 point.
* Gamma – is the second derivative of the option price by the underlier price; shows the rapidity of the option delta change.
* Vega – is the first derivative of the option price by volatility; shows how option price will be changed in points, if the volatility changes by 1%.
* Theta – is the first derivative of the option price by time; shows how the option price will be reduced after one day.

### Order entry

To send orders from the Option chain panel, open Order entry by tapping the <img src="../../../.gitbook/assets/image (1528).png" alt="" data-size="line"> button:

<figure><img src="../../../.gitbook/assets/image (1530).png" alt="" width="375"><figcaption></figcaption></figure>

Order entry screen is divided into groups for each Leg. If a trader has several accounts, it is possible to change them, using a control displayed above the list of Legs. Tap <img src="../../../.gitbook/assets/image (1104).png" alt="" data-size="line"> button to delete the Leg from the list. Tap <img src="../../../.gitbook/assets/image (1105).png" alt="" data-size="line"> button to show/hide the details of a Leg. Tap the “Place strategy” button to send orders.

### **Settings**

In order to manage the panel settings, tap the <img src="../../../.gitbook/assets/image (1531).png" alt="" data-size="line"> button and the following screen will be opened:

<figure><img src="../../../.gitbook/assets/image (1532).png" alt="" width="375"><figcaption></figcaption></figure>

A user can configure settings in the “Column editor”, “Calculations” and “Analyzer” sections.

* Column editor - in this section a user can activate/deactivate the necessary parameters for displaying in the Call and Put options card;
* Calculations - this section contains parameters that will affect the calculations;
* Analyzer - this section contains a setting that allows a user to choose the chart type and the settings that are used to calculate the option profile.
