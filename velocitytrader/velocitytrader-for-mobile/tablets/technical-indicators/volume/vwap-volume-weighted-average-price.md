# VWAP (volume weighted average price)

Volume weighted average price (VWAP) is a technical analysis tool used to measure the average price weighted by volume. VWAP is typically used with intraday charts as a way to determine the general direction of intraday prices. VWAP is similar to a moving average in that when the price is above VWAP, prices are rising and when the price is below VWAP, prices are falling. VWAP is primarily used by technical analysts to identify the market trend.VWAP is used to identify liquidity points. As a volume weighted price measure, VWAP reflects price levels weighted by volume. This can help institutions with large orders. The idea is not to disrupt the market when entering large buy or sell orders. VWAP helps these institutions determine the liquid and illiquid price points for a specific security over a very short time period.VWAP can also be used to measure trading efficiency. After buying or selling a security, institutions or individuals can compare their price to VWAP values. A buy order executed below the VWAP value would be considered a good fill because the security was bought at a below average price. Conversely, a sell order executed above the VWAP would be deemed a good fill because it was sold at an above average price.

#### Calculation <a href="#calculation" id="calculation"></a>

Volume weighted average price (VWAP) is exactly what it sounds like: the average price weighted by volume. VWAP is calculated using a defined calculation cycle, based on a number of bars displayed in the chart, rather than being tied to a single trading day.**Calculation logic:**

1. **Cycle setup:**
   * A cycle consists of a set number of bars, defined by the user (minimum = 2, default = 10).
   * Within the cycle, VWAP values are calculated cumulatively. When the cycle ends, a new cycle starts.
2. **Price and volume per bar:**
   * For each bar iii in the cycle: ​\
     ![](<../../../../.gitbook/assets/image (93).png>)
   * If the VWAP for a bar equals 0, this bar is excluded from the cycle calculation.
3. **VWAP calculation per cycle:**\
   ![](<../../../../.gitbook/assets/image (94).png>)​

#### Main parameters <a href="#main-parameters" id="main-parameters"></a>

* Bars number in cycle - the number of bars for calculating the values of the volume analysis;
* Line style.

The indicator looks as follows on the chart:

<figure><img src="../../../../.gitbook/assets/image (99).png" alt=""><figcaption></figcaption></figure>
