# General settings

The General settings menu is used to customize and change general properties of the Web application. To open it, click on the ![](<../../.gitbook/assets/image (250).png>) button at the side bar of the platform.

### **General**

<figure><img src="../../.gitbook/assets/image (1739).png" alt=""><figcaption></figcaption></figure>

* Language - defines the default language of the UI. To set up your preferred language simply select it from the list;
* Style - allows to select the color theme for the app;
* Display mode - allows to select the display mode of the app;
* Enable sounds - check to allow sound notifications;
* Allow positions closing by double-clicking - if checked, allows closing positions by double-clicking them in the [Positions](../account-management/positions.md) panel;
* Allow orders cancellation by double-clicking - if checked, allows cancelling orders by double-clicking them in the [Working Orders](../account-management/working-orders.md) panel.

### **View**

<figure><img src="../../.gitbook/assets/image (1377).png" alt=""><figcaption></figcaption></figure>

* Rounded average open price – check to round open price of positions in Watchlist, Positions, Filled orders, Market depth and other panels (tick size=instrument tick size);
* Display quantity in lots – check to view orders quantity in lots, uncheck to view in units;
* Reverse buttons order – check to reverse trading buttons into Sell/Buy pattern;
* Display absolute qty. for Sell/Short – if checked, quantity for sell orders and short positions with positive values are shown;
* Abbreviate volumes - if checked, large volume values are displayed in abbreviated format;
* Tooltips – check to display all tooltips in the application, uncheck to hide. The function is enabled by default.

### **Trading defaults**

<figure><img src="../../.gitbook/assets/image (1747).png" alt=""><figcaption></figcaption></figure>

* Account – specifies an account used by default, available for a multi-account user;
* Symbol – specifies a symbol used by default. This is the instrument that will be shown first when you load the Chart panel or Order entry panel;
* Set SL/TP values in offset (for new orders) – if checked, order prices are shown in offset, if unchecked – in absolute values;
* Show offset in – allows to select one of the available modes for offset displaying:
  * Ticks - displays the offset in price ticks;
  * Ticks (fractional ticks for Forex) - fractional ticks for Forex instruments;
  * Points - displays the offset as an absolute value in points;
  * Percent - displays the offset as a percentage of the order price.
* Use stop limit instead of stop – check to place stop limit orders instead of stop orders. When checked activates the 'Limit offset, ticks' field;
* Use stop limit for SL - check to place Stop limit orders instead of Stop orders for Stop loss. When checked, activates the 'Limit offset, ticks' field;
* Limit offset, ticks – use to adjust the default quantity of ticks for offset of a limit price. Active only if 'Use stop limit instead stop' is checked;
* Buy TP trigger price - allows selecting price type for Buy Take profit order trigger;
* Sell TP trigger price - allows selecting price type for Sell Take profit order trigger;
* Buy SL trigger price - allows selecting price type for Buy Stop loss order trigger;
* Sell SL trigger price - allows selecting price type for Sell Stop loss order trigger;
* Select SL/TP trigger price in OE - if active, user will have a possibility to select SL/TP trigger price in Order entry panel;
* Order type – allows specifying order type, available values: Market, Limit, Stop, Stop limit, Trailing stop, OCO;
* Market/Limit(Stop limit)/Stop Validity – allows setting up validity for market/limit (stop limit)/stop orders respectively;
* SL validity - allows to select the default validity for Stop loss orders from the available validity values for Stop, Stop limit, and Trailing stop orders;
* TP validity - allows to select the default validity for Take profit orders from the available validity values for Limit orders;
* Select SL/TP validity in OE - if checked, allows to select the validity for Stop loss and Take profit orders directly in the Order Entry panel;
* Overnight execution by default - if true, all new orders will be set for overnight execution by default (only for instruments that support overnight trading). If false, overnight execution will be disabled by default.\
  Note this option is visible only if at least one of your accounts supports overnight trading;
* Types manager – allows setting defaults.

To specify additional settings for orders you need to open 'Types manager' and select a symbol type - Forex, Futures, Equities, etc. for which you want to set up default lots values. It is also possible to override default lots values for separate symbols by adding them to the symbol types tree using "+" button. In order to apply symbol type default lots settings, just delete symbol from the tree using context menu:

<figure><img src="../../.gitbook/assets/image (1382).png" alt=""><figcaption></figcaption></figure>

* SL/TP default offset, ticks – specifies a default value of offset field for SL/TP;
* SL/TP default offset, % - defines SL/TP offset in percentage;
* User quantity coefficient – is a default increment applied to all quantity counters;
* Price increment (arrow), ticks – determines the increment value (e.g. the Limit price field in the Order entry panel) when pressing the Up Arrow (^) key;
* Default lots setup – allows enabling default lot sizes for orders of selected symbol types or specific symbols which will be available in OE section;
* Buy TP trigger price – allows selecting price type for Buy Take profit order trigger;
* Sell TP trigger price – allows selecting price type for Sell Take profit order trigger;
* Buy SL trigger price – allows selecting price type for Buy Stop loss order trigger;
* Sell SL trigger price – allows selecting price type for Sell Stop loss order trigger.

{% hint style="warning" %}
If 'Show offset in = Ticks (fractional ticks for Forex)', then options 'SL/TP default offset, ticks' in the Forex instrument type will be displayed in decimal view and in the corresponding format. For example, 10 ticks will be displayed as 1.0, and 50 ticks as 5.0, depending on which value is set in the option. If 'Show offset in' is NOT 'Ticks (fractional ticks for Forex)', values of the options 'SL/TP default offset, ticks' are displayed by default, e.g. 10 ticks, 50 ticks.
{% endhint %}

### **Confirmations**

<figure><img src="../../.gitbook/assets/image (1383).png" alt=""><figcaption></figcaption></figure>

In the Confirmations section all of the options are fairly intuitive:

* Confirm order placement - check if you want to confirm each order placement;
* Confirm order cancellation - check if you want to confirm each order cancellation;
* Confirm order/positions modification - check if you want to confirm each order/position modification;
* Confirm position closing - check if you want to confirm each position closing;
* Confirm alert remove - check if you want to confirm each alert removing;
* Open deal tickets on workspace - check if you want to confirm every opening of deal tickets on a workspace;
* Show margin deal ticket on workspace - check to display margin deal tickets directly on workspace;
* Show deal tickets in application tray - determines whether alerts are displayed in the application tray. If false, deal tickets are not shown in the tray, but remain available in the Event log;
* Show information message about start/stop copy trading - check to display a notification message when copy trading starts or stops;
* Show information message about subscribe/unsubscribe - check to display a message when subscribing or unsubscribing to strategies.

### **Warnings**

<figure><img src="../../.gitbook/assets/image (1384).png" alt=""><figcaption></figcaption></figure>

* Warn if wrong order – if checked, you will get a warning message in case of placing order with incorrect parameters;
* Warn if identical subsequent order is placed (sec) – if checked, you will get a warning message in case of placing an identical subsequent order during the specified time period;
* Warn if Quantity to close > Maximum lot – if checked, the system will display a warning message when attempting to close a position where the quantity exceeds the Maximum lot. In such cases, multiple orders will be generated to close the position;
* Warn when entering into leverage - if enabled, you will receive a warning message indicating that you are about to start using leverage (broker's funds) in every order confirmation screen when your _Available Cash_ is less then zero;
* Warn if order quantity exceeds – allows to select a quantity level at which the system will display a warning message;
* Warn if order capital exceeds – allows to select an order capital level at which the system will display a warning message;
* Warn if today's gross less – allows to get a warning message in case if a level of today gross is less than in set parameter;
* Warn if available funds less – allows to select available funds level at which the system will display a warning message;
* Warn if today's volume exceeds - allows to select today volume level at which the system will display a warning message;
* Show symbol halt warnings – if checked, you will get a warning message in case a trading halt on symbol occurs.

{% hint style="info" %}
When there is no Internet connection, users with logging enabled are not allowed to change settings.
{% endhint %}
