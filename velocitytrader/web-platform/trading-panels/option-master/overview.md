# Overview

The Option master panel shows detailed information about options, allows to analyze it and then to trade with selected option contracts.

To open a new Option master panel go to Terminal - > Option master.

<figure><img src="../../../.gitbook/assets/image (1430).png" alt=""><figcaption></figcaption></figure>

**Level 1 symbol data:**

Level 1 data information of the symbol that underlies the option contract was gathered in this block. This block can be easily customized through the Context menu.

**Symbol lookup:**

Here user can select an instrument that underlies the option which user is going to analyze.

**Settings:**

Clicking on the button ![](<../../../.gitbook/assets/image (1431).png>) calls the dialog window Option master – settings. This block allows specifying general settings of the Option master panel. General settings tab is divided into five sections: General, Option chain, Analyzer, Volatility lab and Info window.

**General:**

<figure><img src="../../../.gitbook/assets/image (1432).png" alt=""><figcaption></figcaption></figure>

The section General has the following options:

* Interest rate, % – allows selecting interest rate.
* IV calculation price – allows selecting price for IV value calculation from the drop-down list. The following values are available here: Ask, Bid and Last.

**Option chain:**

<figure><img src="../../../.gitbook/assets/image (1433).png" alt=""><figcaption></figcaption></figure>

* Strikes aggregation style – allows selecting style of strikes count from the drop-down list. There are two available styles:
  * From ATM strike – strikes are counted from the ATM strike, this is the default style of strikes aggregation;
  * Custom underlier price – allows choosing custom underlier price.
* Coloring method – allows selecting coloring scheme for Option chain tab: Classic or Historical volatility.

If coloring method is Classic, the following options can be selected:

In-the-money color – allows selecting 'In the money' color.

Out-the-money-color – allows selecting 'Out the money' color.

<figure><img src="../../../.gitbook/assets/image (1434).png" alt=""><figcaption></figcaption></figure>

If coloring method is Historical volatility, the following options can be selected:

* Current HV, % – shows current level of the historical volatility for the underlier (Min = 0, Max = 1000, Step = 0.1). Pressing the button ![](<../../../.gitbook/assets/image (1435).png>) allows to reset custom value of the historical volatility to the calculated value from the symbol chart by the selected price type (described below).
* Price – allows specifying the underlier price from which sought values Std. and 2\*Std. will be plotted. The following prices are available here: Last, (Bid + Ask)/2, OHLC/4 and OHL/3.
* ATM strike color, Std. color, 2\* Std. color – standard setting for color selection.

**Coloring logic**

ATM strike color – it is a strike or 2 strikes, which are more closely located to the Last price of the underlier.

Std.1 = Price \* (1-HV/SQRT(365)\*SQRT(T);

Std.2 = Price \* (1+HV/SQRT(365)\*SQRT(T)), where T is quantity of days remaining before the contract expiration.

All strikes inclusively, which fall within the range from Std.1 to Std.2, should be painted in the Std. color.

2Std.1 = Price \* (1-2\*(HV/SQRT(365)\*SQRT(T));

2Std.2 = Price \* (1+2\*(HV/SQRT(365)\*SQRT(T))), where T is quantity of days remaining before the contract expiration.

All strikes inclusively, which fall within the range from 2Std.1 to 2Std.2, should be painted in the 2\*Std. color. Coloring of Std.color occurs over 2\*Std.coloring.

**Analyzer:**

<figure><img src="../../../.gitbook/assets/image (1436).png" alt=""><figcaption></figcaption></figure>

Contains only one Appearance section which allows specifying colors and style for displaying the main lines of the option position profile:

* Intrinsic – color, shape and thickness of the option intrinsic value line;
* Time line - color, shape and thickness of the option time line;
* Zero line - color, shape and thickness of the zero line;
* Underlier price – color, shape and thickness of the line that indicates the underlier price.

**Volatility lab:**

<figure><img src="../../../.gitbook/assets/image (1437).png" alt=""><figcaption></figcaption></figure>

The section Volatility lab allows to set up Basis parameter of the Volatility lab tab of the Option master panel:

* Basis – allows selecting Strike prices or Delta from the drop-down list.

**Info Window:**

<figure><img src="../../../.gitbook/assets/image (1438).png" alt=""><figcaption></figcaption></figure>

Visibility:

Show Info window - allows to define whether the Info window will be shown or not.

View:

The following options can be activated: Intrinsic P/L, P/L, Delta, Gamma, Vega, Theta, Rho, What if.

Colors:

The style of a font can be selected.

**Positions/Orders information:** this block shows all information about positions, orders and 'test on paper' results.

**Panel navigation:** use this block in order to manage tabs of Option master panel.

**Info panel:** click on the button ![](https://1243456536-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LMCqxhh2XAdWPUjcvxR%2F-LNAtqF0AI5bOZBLWnuU%2F-LNAxBiExMjEcjSx_8kL%2Finfo%20panel.png?alt=media\&token=21e8850a-4f8f-475e-88f3-6f457c00ad04) to enable/disable the information panel displaying.

This panel consists of a Greek logical block that shows total "greeks" value by current portfolio.

Greeks – are the coefficients which used for the characteristics of option cost (premium) sensitivity to the changing of various values: Delta, Gamma, Vega and Theta.

* Delta – is the first derivative of the option price by the underlier price; shows how option price will be changed in points, if the underlier price changes by 1 point.
* Gamma – is the second derivative of the option price by the underlier price; shows the rapidity of the option delta change.
* Vega – is the first derivative of the option price by volatility; shows how option price will be changed in points, if the volatility changes by 1%.
* Theta – is the first derivative of the option price by time; shows how the option price will be reduced after one day.
