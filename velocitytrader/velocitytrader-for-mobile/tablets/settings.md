# Settings

You can access the ‘Settings’ screen from the application's main menu in order to manipulate by 'Defaults' and 'Confirmations':

### **Defaults**

In ‘Defaults’ settings section you can adjust the following:

<figure><img src="../../.gitbook/assets/image (102).png" alt=""><figcaption></figcaption></figure>

* Order quantity – displays amount of lots for opening an order;
* Validity – allows specifying order validity by selecting among the following time frames: Day, GTC, IOC, GTD, FOK, GTS;
* Order type – allows to select one of the following orders: Market, Limit, Stop, Stop limit, Trailing stop, OCO;
* Quantity in lots - if checked, quantity is displayed in lots, if unchecked – in units;
* Set SL/TP values in offset – if checked, the SL/TP prices are in offset, if unchecked they are in absolute values;
* Show offset in – allows to select one of the available modes for offset displaying:
  * Ticks - displays the offset in price ticks;
  * Ticks (fractional ticks for Forex) - fractional ticks for Forex instruments;
  * Points - displays the offset as an absolute value in points;
  * Percent - displays the offset as a percentage of the order price.
* Use stop limit instead of stop – check to place stop limit orders instead of stop orders. When checked, it activates the "Limit offset, ticks" field;
* Buy TP trigger price – allows selecting price type for Buy Take profit order trigger;
* Sell TP trigger price – allows selecting price type for Sell Take profit order trigger;
* Buy SL trigger price – allows selecting price type for Buy Stop loss order trigger;
* Sell SL trigger price – allows selecting price type for Sell Stop loss order trigger;
* Select SL/TP trigger price in OE – if active, user will have a possibility to select SL/TP trigger price in Order entry panel;
* Overnight execution by default - if active, all new orders will be eligible for overnight execution automatically. Read more [here](overnight-trading.md).

### **Confirmations**

‘Confirmations’ settings section allows to enable double-checking of the following actions by marking them as checked, after what the application will ask you to confirm these actions:

<figure><img src="../../.gitbook/assets/image (1546).png" alt=""><figcaption></figcaption></figure>

* Order sending;
* Order modifying;
* Order executing;
* Order cancelling;
* Position modifying;
* Position closing;
* Alert removing.

### Other

<figure><img src="../../.gitbook/assets/image (1547).png" alt=""><figcaption></figcaption></figure>

The **"**&#x4F;ther" settings section cannot be displayed in the application settings if the biometric authentication is not checked in the system settings of the device or it is blocked.

Biometric authentication enables a user to log in to the mobile application more securely by using the Fingerprint or FaceID features.

<figure><img src="../../.gitbook/assets/image (1548).png" alt=""><figcaption></figcaption></figure>

To apply Fingerprint in the application for subsequent logins, a user should put his finger on the sensor.

<figure><img src="../../.gitbook/assets/image (1549).png" alt=""><figcaption></figcaption></figure>

After this, the checkbox More -> Settings -> Other -> Biometric authentication becomes True.

A user should enter his password to confirm biometrics:

<figure><img src="../../.gitbook/assets/image (1550).png" alt=""><figcaption></figcaption></figure>

On subsequent calls of the Login screen form, if the Biometric authentication setting is checked in the application, the appropriate dialog box will be automatically displayed.

To deactivate Biometric authentication, uncheck the corresponding setting and then tap the "OK" button on the undermentioned screen:

<figure><img src="../../.gitbook/assets/image (1551).png" alt=""><figcaption></figcaption></figure>

### Push notifications

VelocityTrader app provides the ability to receive push notifications on numerous events such as the daily loss limit warning, margin warning, receiving a new trading idea, etc. Upon receiving a push notification, the user can tap on it and thus open the application. Sending push notifications to the device is regulated by your broker, i.e. you cannot activate this function by yourself. If the user wants to disable receiving push notifications, he can do it in the settings of his device.

### Alerts

This section allows to configure the alerts, the following settings are available:

<figure><img src="../../.gitbook/assets/image (1552).png" alt=""><figcaption></figcaption></figure>

* Notification – combobox for selecting the type of notification after alert triggering, multiselect is available:
  * Email – an alert containing the text from the ‘Alert message’ field will be sent to the user by email;
  * Push notification – an alert containing the text from the ‘Alert message’ field will be sent to the user via push notification;
  * Pop-up – an alert containing the text from the ‘Alert message’ field will be sent to the user in pop-up message;
  * Sound – a musical alert will be played to the user in the client.
* Alert type – allows to set an alert type. Available options are: Default by symbol, Ask, Bid, Last, Change%, Volume;
* Condition – allows to set an alert condition. Available values are: >,<,>=,<=;
* Importance – allows to define the alert importance, the following options are available: High, Medium, Low;
* After execute – allows to select alert behavior after execution. Available options are ‘Stop’ - alert is not active but stored in the list of alerts, and ‘Remove’ - alert is removed after execution.

{% hint style="info" %}
When there is no Internet connection, users with logging enabled are not allowed to change settings.
{% endhint %}
