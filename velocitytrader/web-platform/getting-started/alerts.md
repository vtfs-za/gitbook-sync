# Alerts

To open the Alerts panel, click on the ![](<../../.gitbook/assets/image (1398).png>) button which is located at the header of Velocity Trader Web platform. In order to create an alert, click on the ![](<../../.gitbook/assets/image (1399).png>)&#x20;button at the bottom of the panel.

A user can see Bid, Ask, Last, Change% and Volume data by the symbol, selected in the symbol lookup of the panel.

<figure><img src="../../.gitbook/assets/image (1402).png" alt="" width="428"><figcaption></figcaption></figure>

* Account - name of the account for which the alert will be created;
* Symbol – the symbol lookup allows to select an instrument by which the alert will be created;
* Notification type – combobox for selecting the type of notification sent after alert triggering. Available types are Email, Push, Pop-up, and Sound;
* Alert type – allows to set an alert type. Available options are the following: Ask, Bid, Last, Change%, Volume;
* Condition – allows to set an alert condition. Available values are the following:>,<,>=,<=;
* Value – allows to set a value of Alert type for reaching the condition;
* Importance – allows to define the importance of the alert. The following options are available: High, Medium, Low. After execution of the alert, a user gets a notification with the corresponding color (Red/Yellow/Green) of the indicator which depends on importance of the alert;
* Expiration – date/time picker that allows specifying the period of alert lifetime. The expiration date is set in the corresponding calendar control:

<figure><img src="../../.gitbook/assets/image (1404).png" alt=""><figcaption></figcaption></figure>

* After execute – allows to choose alert behavior after execution. Available options are the following:

&#x20;             \-    Stop – after execution alert is not active but stored in the list of alerts;

&#x20;             \-    Remove – after execution alert is removed.

* Action – allows to set up the notifications about alerts’ execution:

&#x20;             \-    Place order + Notify – alert is executed according to the notification type and order placement occurs;

&#x20;             \-    Notify – user is notified without placing an order, this value is set by default;

* Order parameters – becomes available only when 'Place order + Notify' option is selected in the 'Action' control. Allows to open standard Order entry panel to configure the required parameters of the order to be placed after alert triggering;
* Alert message – allows to type the text of the alert message. The text in the Message box is generated automatically but a user can customize the text of the notification;
* Overnight processing - if active, the alert will be eligible to be triggered during overnight market hours;
* Create button – allows to create an alert. The button is colored according to importance of the alert.

### **Alerts management**

A user can see created alerts and work with them – both with executed and not executed ones.

<figure><img src="../../.gitbook/assets/image (1636).png" alt=""><figcaption></figcaption></figure>

There are the following columns in the table of the Alerts panel:

* Symbol – symbol name by which the alert was created;
* Condition – the alert is executed by reaching the condition;
* Account – the name of the account for which the alert has been created;
* Controls – the set of controls for each alert:

&#x20;            \-    Play – click on the button to re-start the alert. The button is visible for executed alerts;

&#x20;            \-    Stop – click on the button to stop the execution of the alert. The button is visible for not executed alerts;

* Edit – allows to open editing screen;
* Remove – allows to remove alert. By clicking on the button, the confirmation window will appear.

<figure><img src="../../.gitbook/assets/image (1401).png" alt="" width="465"><figcaption></figcaption></figure>

{% hint style="warning" %}
If a user exceeds the limit of created alerts, the "Create new" button will be disabled.
{% endhint %}

### **Alerts on chart**

To create a new alert on the chart, click on the<img src="../../.gitbook/assets/7 (23).png" alt="" data-size="original">button which appears near the price scale at the chart while hovering the certain price level:

<figure><img src="../../.gitbook/assets/alerts (3).gif" alt=""><figcaption></figcaption></figure>

All active alerts created by the same symbol are visible on the chart. After execution the alert is removed from the chart. The buttons which allow to edit <img src="../../.gitbook/assets/9 (15).png" alt="" data-size="original"> and remove <img src="../../.gitbook/assets/10.png" alt="" data-size="original">&#x20;an alert become visible while hovering the alert’s icon. The color of the alert’s icon depends on importance of the alert.

By clicking on the Edit control, the Editing screen is opened. Editing of the alert from the chart is also possible by using the Drag\&Drop function. While using this function, the alert is modified without additional confirmations.
