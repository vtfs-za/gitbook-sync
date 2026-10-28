# Alerts

To open the Alerts panel, click on the ![](https://lh7-us.googleusercontent.com/docsz/AD_4nXfJuv_r0mkh2na82NtvWsYUtLAZIroFrulsqivYldUMgN3GkvDwik-japuzqWX7E0YIkOcoRo8ywDsDPIQnyV9J_UGLNmcBDSsqBmMXRcdO7FhA02qpoPv454jmE1_IUYfIujtBGXl7Rg5mv585qY6Eqxv-?key=i34kSG4duM_DXcQbimGXZQ) button which is located at the sidebar of the Velocity Trader terminal. In order to create an alert, click on the <img src="../../../.gitbook/assets/2 (47).png" alt="" data-size="original">button at the bottom of the panel.

A user can see Bid, Ask, Last, Change% and Volume data by the symbol, selected in the symbol lookup of the panel.

<figure><img src="../../../.gitbook/assets/image (525).png" alt=""><figcaption></figcaption></figure>

* Account - the name of the account for which the alert will be created;
* Symbol – the symbol lookup allows to select an instrument by which the alert will be created;
* Notification – allows to select a type of notification to be sent, available values are Email, Push, Pop-up, Sound. Multiselect is available here;
* Alert type – allows to set an alert type. Available options are the following: Ask, Bid, Last, Change%, Volume;
* Condition – allows to set an alert condition. Available values are the following: >,<,>=,<=;
* Value – allows to set a value of Alert type for reaching the condition;
*   Importance – allows to define the importance of the alert. The following options are available: High, Medium, Low. After execution of the alert, a user gets a notification with the corresponding color of the indicator which depends on importance of the alert;<br>

    <figure><img src="../../../.gitbook/assets/image (1130).png" alt=""><figcaption></figcaption></figure>
* Expiration – date/time picker that allows specifying the period of alert lifetime. The expiration date is set in the corresponding calendar control:

![](<../../../.gitbook/assets/image (793).png>)

* After execute – allows to choose alert behavior after execution. Available options are the following:

&#x20;           \- Stop – after execution alert is not active but stored in the list of alerts;

&#x20;           \- Remove – after execution alert is removed.

* Action – allows to set up the action to be performed after alerts’ execution:

&#x20;          \- Place order + Notify – alert is performed according to the notification type and order placing occurs;

&#x20;          \- Notify – user is notified without placing an order, this value is set by default;

* Order parameters – becomes available only when 'Place order + Notify' option is selected in the 'Action' control. Allows to open standard Order entry panel to configure the required parameters of the order to be placed after alert triggering;
* Alert message – allows to type the text of the alert message. The text in the Message box is generated automatically but a user can customize the text of the notification;
* Overnight processing - if active, the alert will be eligible to be triggered during overnight market hours;
* Create button – allows to create an alert. The button is colored according to importance of the alert.

### **Alerts management**

A user can see created alerts and work with them – both with executed and not executed ones.

<figure><img src="../../../.gitbook/assets/image (526).png" alt=""><figcaption></figcaption></figure>

There are the following columns in the table of the Alerts panel:

* Symbol – symbol name by which the alert was created;
* Condition – the alert is executed by reaching the condition;
* Account – the name of the account for which the alert has been created;
* Controls – the set of controls for each alert:

&#x20;         \- Play – click on the button to re-start the alert. The button is visible for executed alerts;

&#x20;         \- Stop – click on the button to stop the execution of the alert. The button is visible for not executed alerts;

&#x20;         \- Edit – allows to open editing screen;

&#x20;         \- Remove – allows to remove alert. By clicking on the button, the confirmation window will appear.

![](<../../../.gitbook/assets/5 (54).png>)

If a user exceeds the limit of created alerts, then an error message will be displaye&#x64;**:**

![](<../../../.gitbook/assets/desktop, web (1).png>)

### **Alerts on chart**

The chart displays all active alerts for the symbol selected in the symbol lookup. If the alert is executed, it will not be shown on the chart, but its presence in the panel is controlled by the ‘After execute’ parameter. The chart displays all alerts for the symbol, for Ask, Bid, Last types.

To create a new alert on the chart, click on the<img src="../../../.gitbook/assets/7 (13).png" alt="" data-size="original">button which appears near the price scale at the chart while hovering the certain price level:

<figure><img src="../../../.gitbook/assets/alerts (1).gif" alt=""><figcaption></figcaption></figure>

All active alerts created by the same symbol are visible on the chart. After execution the alert is removed from the chart. The buttons which allow to edit<img src="../../../.gitbook/assets/9 (11).png" alt="" data-size="original">and remove<img src="../../../.gitbook/assets/10 (2).png" alt="" data-size="original">an alert become visible while hovering the alert’s icon.&#x20;The color of the alert’s icon depends on importance of the alert.

By clicking on the Edit control, the Editing screen is opened. Editing of the alert from the chart is also possible by using the Drag\&Drop function. While using this function, the alert is modified without additional confirmations.&#x20;
