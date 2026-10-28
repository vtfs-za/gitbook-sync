# Chart settings

Chart settings can be opened through the context menu of the Chart panel.&#x20;

### **Data style**

<figure><img src="../../../.gitbook/assets/image (262).png" alt=""><figcaption></figcaption></figure>

* Style - describes price movements of a symbol. Another way to choose the chart style through context menu: Style -> \[desired style].
* Data type - the way to accept data. Available types are: Bid, Ask, Last. Based on server settings Last or Bid/Ask type can be disabled.
* Color settings for all styles.

### **View**

<figure><img src="../../../.gitbook/assets/image (263).png" alt=""><figcaption></figcaption></figure>

* Back color - allows setting up the color of the chart background.
* Watermark mode - allows displaying the Symbol/Description watermark (or both) as well as hiding it.
* Watermark color - allows setting up the color of the watermark.
* Crosshair - allows activating and setting up cursor lines, as well as font color of price/time labels.
* Grid - allows activating and setting up grid on the chart.
* Time to next bar - allows activating and setting up color of figures that show remaining time to the next bar.
* Additional - allows activating Drawing toolbar, Chart toolbar.

### &#x20;**Time scale**

<figure><img src="../../../.gitbook/assets/image (264).png" alt=""><figcaption></figcaption></figure>

* Appearance - allows setting up style of time scale.
* Holes in the history - allows seeing free space on the chart if there is no history at that moment.
* Show extended session - allows seeing bars from extended sessions on chart. The peculiarities of this setting also depend on the state of the "Use session periods for Intraday chart" setting that can be found in the BackOffice. If “Use session periods for Intraday chart = true”, then the aggregation will start from the first session of the day. At the same time, sessions that belong to the Before market/After market periods will be excluded from the Extended session list.
* Highlight extended sessions - all extended sessions that were set on the server for the current symbol will be displayed in selected color.
* Highlight date - allows displaying separator lines for: Days, Weeks, Months, and Years.

### **Price scale**

<figure><img src="../../../.gitbook/assets/image (265).png" alt=""><figcaption></figcaption></figure>

* Scale type - allows selecting the price scale type. The available options are:
  * Absolute – displays price values in their original absolute units (default option);
  * Relative – represents prices as relative changes from a selected Start price. When Relative is selected, the Start price option becomes enabled, while Log base is disabled;
  * Logarithmic – applies logarithmic scaling to the price axis. When Logarithmic is selected, both Start price and Log base options become enabled, allowing customization of scaling behavior.
* Zoom - choose between Manual and Automatic Price scale. In manual mode, changes can be made to the vertical price scale. Automatic mode is based on visible prices but it also can fit Indicators, Orders/Positions, Drawings and the day's High/Low prices.
* Scale markings - allow setting up custom grid on the price scale as well as minimal grid step, highlight grid step and highlight grid color.
* Appearance - allows setting up style of price scale.
*   Highlight prices:

    * Price indicator - allows setting up active price marking as:

    &#x20;       \- Scale marker

    &#x20;       \- Scale marker with line

    &#x20;       \- None

    * Ask price color
    * Last price color
    * Bid price color
* Display Last instead of calculated Close - if checked, only the Last price is displayed on the price scale. If unchecked, both the Last price and the calculated Close value according to the selected aggregation type are displayed (available only for charts with Heiken Ashi style);
*   Spread type - allows setting up the way of spread displaying:

    * None
    * Area
    * Line (Bid and Ask)
    * Line with price (Bid and Ask)

    If spread type is None, then single price indicator will be shown, depending on chart data type (Bid, Last, Ask etc.)
* Spread area color - color of spread area (if it's chosen as spread type).
* Previous close line - type and color of the Previous close line.
* Day High/Low lines - type and color of the Day High/Low lines.

### Alerts

<figure><img src="../../../.gitbook/assets/image (267).png" alt=""><figcaption></figcaption></figure>

* Notification type – allows selecting the type of notification sent after alert triggering, the following types are available: Email, Push, Pop-up, Sound;
* Importance – allows to define the importance of the alert. The following options are available: High, Medium, Low;
* After execute – allows to select alert behavior after execution. Available options are: Stop or Remove;
* Show alerts - if checked, alerts will be shown on the Chart.

### **Visual trading**

<figure><img src="../../../.gitbook/assets/image (268).png" alt=""><figcaption></figcaption></figure>

* Open positions - allows displaying opened positions on chart and setting up style of lines.
* Working orders - allows displaying working orders on the chart and setting up the style of lines.
* Filled orders - allows displaying filled orders on chart.
* Bound active positions/orders to the left side - allows displaying active positions/orders on the left side of the Chart area.&#x20;

### **Chart Order entry**

<figure><img src="../../../.gitbook/assets/image (269).png" alt=""><figcaption></figcaption></figure>

This section allows selecting buttons and hot buttons which will be displayed in built-in Order entry.

### **Info window**

<figure><img src="../../../.gitbook/assets/image (270).png" alt=""><figcaption></figcaption></figure>

This section allows setting up contents of the Info window and style of its displaying.

### **Volume bars**

<figure><img src="../../../.gitbook/assets/image (272).png" alt=""><figcaption></figcaption></figure>

This section allows customizing the volume bars at the bottom of the Chart.
