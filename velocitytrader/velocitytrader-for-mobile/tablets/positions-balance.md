# Positions balance

Positions balance tab contains the summary of all the opened positions by the chosen account(-s).

Tab can be accessed from Positions screen by moving the slider button to Positions balance:

<figure><img src="../../.gitbook/assets/image (1567).png" alt=""><figcaption></figcaption></figure>

For each position the following information is available:

* Symbol - name of the instrument traded;
* Net position qty. - the net amount of open position;
* Gross P/L - total amount of P/L for open position in the account currency.

The additional data by the chosen position can be found in the right side of the screen:

<figure><img src="../../.gitbook/assets/image (1568).png" alt=""><figcaption></figcaption></figure>

The descriptions and calculations of the parameters in the table are below:

* Current price - market price obtainable from a broker;
*   Break-even - shows the price where Profit/Loss will be zero<br>

    <figure><img src="../../.gitbook/assets/image (497).png" alt=""><figcaption></figcaption></figure>

    where:\
    _&#x4E; - the number of open positions for the selected instrument;_

    _OPi - Open price;_

    _qty i - the volume of the "i" position, taking into account the sign, for a short position the sign is “-”, for a long position the sign is “+”._
*   Gross exposure – the total exposure for open positions by symbol<br>

    <figure><img src="../../.gitbook/assets/image (498).png" alt=""><figcaption></figcaption></figure>

    where:\
    _&#x4C;ot size - lot size for the selected instrument;_\
    _&#x43;ross price - cross rate from the quote currency to the account currency._
*   Net exposure - net exposure for open positions by symbol<br>

    <figure><img src="../../.gitbook/assets/image (499).png" alt=""><figcaption></figcaption></figure>
* Long qty. - total amount of long positions by symbol;
* Short qty. – total amount of short positions by symbol;
*   Average long – average price of long positions<br>

    <figure><img src="../../.gitbook/assets/image (502).png" alt=""><figcaption></figcaption></figure>
*   Average short – average selling price of short positions<br>

    <figure><img src="../../.gitbook/assets/image (503) (1).png" alt=""><figcaption></figcaption></figure>
*   Position value – current value of the position. Calculation is based on current market price<br>

    <figure><img src="../../.gitbook/assets/image (504) (1).png" alt=""><figcaption></figcaption></figure>

    Note that Position value formula depends on the position side:\
    _&#x4C;ong position: Position value = Position exposure+Gross P/L;_\
    _&#x53;hort position Position value = Position exposure-Gross P/L._
* Product type – shows the type of the product for current position.

Also at the bottom of the Positions balance tab the Total Profit can be found. It displays the sum of Gross P/L for all positions.

To call the Context menu, press and hold (Long tap) on the needed item:

<figure><img src="../../.gitbook/assets/image (1163).png" alt=""><figcaption></figcaption></figure>

Actions available in the Context menu:

* Chart - by tapping, the Chart with the selected position will be opened;
* Symbol info - tap and detailed description of the position symbol will be opened.
