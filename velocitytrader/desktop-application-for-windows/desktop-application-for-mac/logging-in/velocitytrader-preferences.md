# Preferences

To open the 'Preferences' menu, click on the button<img src="../../../.gitbook/assets/1 (101).png" alt="" data-size="original">located at the Top menu of the platform.

This menu contains such sections as:

### General:

![](<../../../.gitbook/assets/Screenshot_1 (1).jpg>)

* Allow automatic login – if checked, the application will automatically connect to the server while launching;
* Automatically reconnect application – if checked, the application will try to reconnect to the server after losing connection;
* Disable sounds – if checked, then the application will be muted.

### **View:**

![](<../../../.gitbook/assets/Screenshot_2 (49).jpg>)

* Display quantity in lots – if checked, orders quantity is shown in lots, otherwise - in units;
* Reverse buttons order – if checked, trading buttons will be reversed to Sell/Buy pattern;
* Activate deal tickets – if checked, the system will display informational deal tickets.

### **Hotkeys:**

![](<../../../.gitbook/assets/Screenshot_3 (20).jpg>)

The full information about Hotkeys preferences is represented in the article below: [Hotkeys](hotkeys.md)

### **Trading defaults:**

![](<../../../.gitbook/assets/Screenshot_4 (4).jpg>)

* Account – allows to select a default account for trading;
* Symbol – allows to select a default instrument for trading;
* Order type – allows to select a default type of order for trading:
  * Market – an order to buy or sell a security at the best available price immediately;
  * Limit – an order to buy or sell a security at specified price or better;
  * Stop – an order to buy or sell a security when its price surpasses a particular point, thus ensuring a greater probability of achieving a predetermined entry or exit price, limiting the investor's loss or locking profit;
  * Stop limit – an order to be executed at a specified price (or better) after a given stop price is reached. Once the stop price is reached, the stop-limit order becomes a limit order to buy (or sell) at the limit price or better;
  * Trailing stop:
    * Sell trailing stop order sets the stop price at a fixed amount below the market price on the trailing offset. As the market price rises, the stop price rises by the trail amount, but if the stock price falls, the stop loss price doesn't change, and a market order is submitted when the stop price is hit;
    * Buy trailing stop orders are the mirror image of sell trailing stop orders.
  * OCO (One cancels other) – an order containing two parts, if one part is executed, then the other part is automatically canceled;
* Market Validity – allows to set up a default validity of a Market order. The following types of Validity are available:
  * Day – an order will be valid for a current trading day;
  * GTC (Good till canceled) – an order will remain active until it is canceled or a contract expires;
  * IOC (Immediate or cancel) – an order or its part will be immediately executed;
  * GTD (Good till date) – an order will be cancelled on a specified date, if not executed, or will remain active until a contract expiration;
  * FOK (Fill or kill) – an order will be immediately fully executed or not executed at all.
* Limit/Stop Limit Validity – allows to set up a default validity of Limit and Stop Limit orders;
* Stop Validity – allows to set up a default validity of a Stop order;
* Default product type – allows indicating the default product type;
* Show offset in – allows to show offset in Ticks or Points;
* Use stop limit instead of stop – check to place stop limit orders instead of stop orders. When checked, it activates the 'Limit offset, ticks' field;
* Limit offset, ticks – allows specifying the limit of offset in ticks;
* Set SL/TP values in offset – if checked, order prices are shown in offset, if unchecked – in absolute values.

### **Confirmations:**

‘Confirmations’ preferences allow to activate the following confirmations:

![](<../../../.gitbook/assets/Screenshot_5 (2).jpg>)

* Confirm order placement - check if you want to confirm each order placement;
* Confirm order cancellation - check if you want to confirm each order cancellation;
* Confirm order/positions modification - check if you want to confirm each order/position modification;
* Confirm position closing - check if you want to confirm each position closing;
* Confirm position reversing - check if you want to confirm each position reversing;
* Confirm alert removing – check if you want to confirm each alert removing.

### **Warnings:**

![](<../../../.gitbook/assets/Screenshot_6 (1).jpg>)

* Warn if identical subsequent order is placed (sec) – if checked, you will get a warning message in case of placing an identical subsequent order during the specified time period.

### **RSS:**

![](<../../../.gitbook/assets/Screenshot_7 (1).jpg>)

This tab is used for adding the required RSS feeds for reading them directly in the trading terminal, the following fields are provided for this:

* Active – check/uncheck RSS feeds to be shopwn in the RSS panel;
* Name – enter the name of the added RSS feed here;
* URL – specify the URL from which the RSS feed will be received;
* Remove – contains buttons for feeds deleting.

{% hint style="info" %}
When there is no Internet connection, users with logging enabled are not allowed to make changes in Preferences screen.
{% endhint %}
