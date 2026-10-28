# Settings

A user can access the "Settings" tab from the application’s "More" menu in order to manage "Defaults" and "Confirmations".

#### Defaults

In "Defaults" settings section you can adjust the following:

<figure><img src="../../.gitbook/assets/settings1 (3).png" alt="" width="375"><figcaption></figcaption></figure>

* Order quantity – displays amount of lots for opening an order;
* Validity – allows specifying order validity by selecting among the following time frames: Day, GTC, IOC, GTD, FOK, GTS;
* SL/TP validity - allows to select the default validity for SL/TP orders from the available validity values for Stop, Stop limit, and Trailing stop orders;
* Select SL/TP validity in OE - if checked, allows to select the validity for Stop loss and Take profit orders directly in the Order Entry panel;
* Order type – allows to select one of the following orders: Market, Limit, Stop, Stop limit, Tr. Stop, OCO;
* Quantity in lots - if checked, quantity is displayed in lots, if unchecked – in units;
* Set SL/TP values in offset – if checked, the SL/TP prices are in offset, if unchecked they are in absolute values;
* Show offset in – allows to select one of the available modes for offset displaying:
  * Ticks - displays the offset in price ticks;
  * Ticks (fractional ticks for Forex) - fractional ticks for Forex instruments;
  * Points - displays the offset as an absolute value in points;
  * Percent - displays the offset as a percentage of the order price.
* Use stop limit instead of stop – check to place stop limit orders instead of stop orders. When checked, it activates the "Limit offset, ticks" field;
* Use stop limit for SL - check to place Stop limit orders instead of Stop orders for Stop loss. When checked, activates the 'Limit offset, ticks' field;
* Buy TP trigger price - allows selecting price type for Buy Take profit order trigger;
* Sell TP trigger price - allows selecting price type for Sell Take profit order trigger;
* Buy SL trigger price - allows selecting price type for Buy Stop loss order trigger;
* Sell SL trigger price - allows selecting price type for Sell Stop loss order trigger;
* Select SL/TP trigger price in OE - if active, user will have a possibility to select SL/TP trigger price in Order entry panel;
* Overnight execution by default - if active, all new orders will be eligible for overnight execution automatically. Read more [here](overnight-trading.md).

#### Confirmations

‘Confirmations’ settings section allows to enable double-checking of the following actions by marking them as checked, after what the application will ask you to confirm these actions:

<figure><img src="../../.gitbook/assets/image (229).png" alt="" width="375"><figcaption></figcaption></figure>

* Order sending;
* Order modifying;
* Order executing;
* Order cancelling;
* Position modifying;
* Position closing;
* Alert removing.

#### Other

<figure><img src="../../.gitbook/assets/image (1741).png" alt="" width="375"><figcaption></figcaption></figure>

The "Other" settings section cannot be displayed in the application settings if the biometric authentication is not checked in the system settings of the device or it is blocked.

* Show information message about subscribe/unsubscribe - adjusts the displaying of the information screen during Subscribe and Unsubscribe processes. True by default.
* Show message if order is submitted off-market - adjusts the displaying of the information screen when an order is submitted outside market hours.

#### Navigation

This section is used to configure the app navigation. It consists of the following settings:

* Show Chart insted of Order Entry - if checked, the Order Entry button in the bottom navigation menu will be replaced with Chart.

Biometric authentication enables a user to log in to the mobile application more securely by using the Fingerprint or FaceID features.

<figure><img src="../../.gitbook/assets/image (1459).png" alt="" width="375"><figcaption></figcaption></figure>

To apply Fingerprint in the application for subsequent logins, a user should put his finger on the sensor.

And to enable Biometric in the iOS application, a user should tap on the “Use Face ID” button.

After this, the checkbox More -> Settings -> Other -> Biometric authentication becomes True.

A user should enter his password to confirm biometrics:

<figure><img src="../../.gitbook/assets/image (1460).png" alt="" width="375"><figcaption></figcaption></figure>

On subsequent calls of the Login screen form, if the Biometric authentication setting is checked in the application, the appropriate dialog box will be automatically displayed.

The user authentication occurs after putting a finger on the sensor and successful fingerprint recognition.

In case the FaceID feature is available and activated on the user device, it can be used as an additional application login option instead of the Fingerprint.

To deactivate Biometric authentication, uncheck the corresponding setting and then tap the "OK" button on the undermentioned screen:

<figure><img src="../../.gitbook/assets/image (1461).png" alt="" width="375"><figcaption></figcaption></figure>

#### Push notifications

Velocity Trader app provides the ability to receive push notifications on numerous events such as the daily loss limit warning, margin warning, receiving a new trading idea, etc. Upon receiving a push notification, the user can tap on it and thus open the application. Sending push notifications to the device is regulated by your broker, i.e. you cannot activate this function by yourself. If the user wants to disable receiving push notifications, he can do it in the settings of his device.

#### Alerts

This section allows to configure the alerts, the following settings are available:

<figure><img src="../../.gitbook/assets/image (1462).png" alt="" width="375"><figcaption></figcaption></figure>

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
