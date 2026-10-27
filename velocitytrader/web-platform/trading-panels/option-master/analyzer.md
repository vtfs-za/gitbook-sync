# Analyzer

Analyzer tab is used for graphic analysis before starting to trade options.

Analyzer tab has the general view as follows:

<figure><img src="../../../.gitbook/assets/image (1443).png" alt=""><figcaption></figcaption></figure>

The main purpose of this tab is to describe graphically the portfolio of positions (Test on paper tab), and also to model changing of impact factors on portfolio.

<figure><img src="../../../.gitbook/assets/image (1444).png" alt=""><figcaption></figcaption></figure>

While setting the corresponding changes of time and volatility user can model changing of portfolio cost which consists of options and underlier.

* Chart type – allows setting the type of displayed information on the chart. The following types are available here: P/L, Delta, Gamma, Vega, Theta and Rho.
* 'T +' – allows modeling changes in the numbers of days remaining until expiration of option or futures contract.
* Volatility, % – allows modeling volatility change in %; volatility modeling occurs simultaneously on all positions included in the portfolio. Range of changing: -99%..∞,%. Option "1 px" controls the width of volatility lines on the analyzer chart.

**Calculator**

The Calculator in Analyzer tab allows users to calculate key option parameters such as the theoretical option price or implied volatility, along with the Greeks (Delta, Gamma, Vega, Theta, and Rho). It provides analytical calculations to help users evaluate option pricing and risk metrics and has the following view:

<figure><img src="../../../.gitbook/assets/image (462).png" alt="" width="563"><figcaption></figcaption></figure>

Calculator contains following Input parameters:

* Calculation type with two possible values:
  * OP (Theoretical option price) - calculates the theoretical option price based on input parameters like strike price and implied volatility;
  * IV (Implied volatility) - calculates the implied volatility based on the option price.
* Strike Price - the price at which the option is exercised;
* Underlying Price - the current price of the underlying asset;
* Implied Volatility - implied volatility value, available only when calculation type is OP;
* Option Price - option price value, available only when calculation type is IV;
* Interest Rate - risk-free interest rate used in the calculations;
* Days Till Expiration - the number of days remaining until the option expires. Must be a positive integer.

The following Output values will be avaialble after clicking "Calculate" button:

* Delta;
* Gamma;
* Vega;
* Implied Volatility;
* Theta;
* Rho;
* Theoretical Price.

{% hint style="warning" %}
Note that the Black-Scholes model is used to calculate theoretical option prices and the Greeks based on the input parameters provided.
{% endhint %}
