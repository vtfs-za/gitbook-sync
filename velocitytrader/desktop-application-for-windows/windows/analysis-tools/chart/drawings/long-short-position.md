# Long/Short position

Drawings allow the user to predict what P/L will be obtained when a position is opened at a given price and the closing price will be equal to the price of the protection order.

The user's Available funds and the user's willingness to risk a certain percentage of those funds (Risk size) are taken into account to calculate the amount of the bought/sold asset, P/L, and the balance after closing the position (Amount). The user can set the Risk size in the "Drawing settings".

<figure><img src="../../../../../.gitbook/assets/1 (3).png" alt=""><figcaption></figcaption></figure>

Drawing can be placed in the historical data or in the real-time chart area. When you place a drawing in the historical chart area, then you can analyse what the P/L would have been if the position had been closed. By placing a drawing with similar parameters in the real-time area, you can estimate your P/L in real time, because the P/L will be recalculated as the last price changes. Note that when you switch between aggregations or change Available funds, the calculated drawing parameters are recalculated.&#x20;

Let's look at what parameters are displayed on the drawing.

<figure><img src="../../../../../.gitbook/assets/2 (3).png" alt=""><figcaption></figcaption></figure>

The width of the drawing shows the period on the chart, which will be analysed for the possibility of closing the position at the price of a protective order.

The drawing is divided by a horizontal line - the line shows the opening price of the position.

The Profit/Stop parameters show the prices of the protective orders that can be placed.&#x20;

An arrow may be drawn on the drawing when the price reaches the level of the protective order on the selected time frame that covers the drawing. Depending on where the arrowhead points, the position may be closed at that price.&#x20;

If the arrow is not drawn, it means that the price has not reached the price of the protective order within the time period covered by the drawing. Therefore P/L will be calculated using the Close price of the last bar in the selected time frame covered by the drawing.

Let's calculate the number of assets to buy/sell:

_**Qty = (AvailableFunds x (RiskValue/100) x crossPrice / (SL-OpenPrice))/LotSize**_

where:

* AvailableFunds - the current value of AvailableFunds&#x20;
* RiskValue - the value is taken from the “Risk value” parameter of the drawing settings
* OpenPrice - open price of the position
* SL - SL price in absolute value
* LotSize - Lot size of the instrument
* crossPrice - cross price in the instrument quote currency

The value is displayed considering the "Display quantity in lots" setting.

Risk/Reward shows the ratio of risk to profit using the formula:

_**Risk/Reward = (TP - OpenPrice)/(OpenPrice - SL))**_&#x20;

where:&#x20;

* OpenPrice - position opening price. &#x20;
* SL - SL price in absolute value.&#x20;
* TP - the TP price in absolute value.

Parameters above the level of the protective order are the following:

* current price of the protective order;
* how much the price of the protective order differs from the open price relative to the open price in percent;
* offset taking into account the "Show offset in" setting;
* account balance after closing the position at the protective order price taking into account the calculated Qty.

Please, note that the P/L and Amount parameters are calculated in the account currency.

To configure the drawing settings, evoke the context menu and click on the "Settings" button. The following menu will be opened:

<figure><img src="../../../../../.gitbook/assets/3 (3).png" alt=""><figcaption></figcaption></figure>

If "Show Place order button" checkbox is True, OE button will be available for activation and for setting the order parameters from the drawing.

If "Show prices on Price scale" checkbox is True, Open/SL/TP drawing parameters will be displayed on the price scale.
