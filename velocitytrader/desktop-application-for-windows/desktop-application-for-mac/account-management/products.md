# Subscriptions

The Subscriptions panel lists all products currently available to the User, products the User has subscribed to, and requests that he has submitted. In order to open the panel select it from the Account drop-down list that is located in the main menu of the terminal. The panel contains two tabs:

* Subscriptions – this tab contains a list of Products that are available to the User for subscription, as well as Products to which the user has already subscribed i.e. those subscription requests which are confirmed by the Admin or automatically;&#x20;
* Requests – contains subscribe/unsubscribe requests sent by the user.

### Subscriptions tab

![](<../../../.gitbook/assets/Screenshot_5 (1) (1).jpg>)

This tab displays cards of products to which the user is subscribed, as well as available to the User for subscription.&#x20;

The upper part of the panel offers the drop-down list <img src="../../../.gitbook/assets/image (989).png" alt="" data-size="line"> which allows filtering product cards currently shown in the tab. It contains the following available options:

* All – displays all products;
* Subscribed – displays products that the user is subscribed to;
* Available for subscription – displays products available for subscription to this user;
* Processing – displays products which are awaiting processing by the admin.

All Product cards are grouped into specific categories, which are assigned by the Admin in the Product settings. Each category can be collapsed/expanded by pressing on it. Product cards contain the name of the Product, its logo, price, and the ‘Subscribe’ button. Note that this button can have two states depending on the product status,so it can be shown as the "Subscribed".&#x20;

In case the logo was not received from the server,<img src="../../../.gitbook/assets/Screenshot_6 (11).jpg" alt="" data-size="original">will be displayed instead. In the upper right corner of each Product card there is the ![](https://lh4.googleusercontent.com/wEkGlYW5qSeJGHTfyYQ96E205vVVvX6eswwVSDiOvyIqiCWYDMiZO2C1vohXpdkVT2EocJhTeZqUkXKP588MgCx4qBNH7unwz8yPzCq6tFHxD6setKlOMPpkztGfxpuJlrM5ko-t) button, upon hovering on which the information about the Product is displayed:

![](<../../../.gitbook/assets/image (924).png>)

If the Product already has an active request awaiting processing by the admin, the button for its canceling is displayed instead of the "Subscribe/Subscribed" buttons. Hovering over the "Cancel request" button will evoke an info pop-up that contains date/time of request creation:

![](<../../../.gitbook/assets/image (816).png>)

Cards of Products, that the User has already subscribed to, have a corresponding button, but when hovering over, it changes the appearance to ‘Unsubscribe’ and respectively serves to unsubscribe from the required Product:

![](<../../../.gitbook/assets/image (909).png>)

Depending on the Market data subscriber status the product card displays the Pro price or Non-pro price or _FREE_ (if there is no charge for using the product). If Market data subscriber status is not defined, then both prices separated by a slash are displayed at once on the product card, the display format is \<non-pro price> / \<pro price> \<currency>.

{% hint style="warning" %}
In order for the system to determine the Market data subscriber status, the user must first go through the appropriate procedure.
{% endhint %}

#### Subscribing

Subscription to the Product of interest is carried out by clicking the "Subscribe" button. This will send a request for subscription which should be approved by admin or the subscription can be performed automatically without his participation. If the Product already has an active request awaiting processing by the admin, the "Cancel request" button is displayed instead of the "Subscribe" button. This allows the user to quickly and easily cancel a subscription request without switching to the Requests tab.

After applying the subscription, the User is shown with the following info screen:

![](<../../../.gitbook/assets/image (879).png>)

Please note that the display of the confirmation screen is controlled in the terminal settings, namely Preferences -> Confirmations section. This message will only be shown if the "Show information message..." setting is enabled.

{% hint style="warning" %}
If the User does not have enough funds to pay the fee, or if there are no available User accounts to be charged for using the Product, then the corresponding reject will be displayed. This is only valid in the case of automatic request confirmation/charging. The reject comes in the form of deal ticket.
{% endhint %}

There are two subscription options - if the User does not need to sign additional documents or if there is a need to sign them.&#x20;

If the documents are not required to be signed, then the subscription request will be created immediately after clicking the appropriate button. This request will await verification by the admin and after its confirming the User will be subscribed to the Product.

In case it is required to sign documents in order to subscribe to the Product, then an additional screen that allows to take the necessary actions will be shown to the User:

![](<../../../.gitbook/assets/new2 (1).jpg>)

This screen contains the following elements:

* The name of the document, which is displayed in the upper part of the screen;
* The content of the document displayed in the main part of the screen;
* Next/Back buttons allow the User to move to the next document or return to the previous one. When acquaintance with the documents is finished, the ‘Next’ button will change its appearance to ‘Done’;
* Progress bar, which is utilized to indicate the progress made when signing documents;
* In case the required fields are missing on the current page, the system will display a corresponding message and will not allow the User to move to the next page.

#### Unsubscribing

In order to unsubscribe from Product, simply hover over the "Subscribed" button and it will change the appearance to ‘Unsubscribe’ button, which respectively serves for unsubscribing from the required Product:

![](<../../../.gitbook/assets/image (909).png>)

After clicking the button, the User will be asked to confirm his unsubscription which looks as follows:

![](<../../../.gitbook/assets/image (943).png>)

Please note that the display of the confirmation screen is controlled in the terminal settings, namely Preferences -> Confirmations section. This message will only be shown if the "Show information message..." setting is enabled.

{% hint style="warning" %}
After confirmation, the User will be immediately unsubscribed, without waiting for the end of the period for which the fee was charged.&#x20;
{% endhint %}

If the Product already has an active request awaiting processing by the admin, the "Cancel request" button is displayed instead of the "Subscribed" button. Thus, if the request was not processed immediately, the user can always cancel it with this button.

{% hint style="warning" %}
The availability of the "Unsubscribe" button is regulated by the administrator for each product individually.
{% endhint %}

### Requests tab

This tab displays all requests sent by the user for subscribing/unsubscribing to the Products for the selected period:

![](<../../../.gitbook/assets/new2 (17).jpg>)

The Requests tab contains the following elements:

* Period selector located in the upper part of the tab contains the Daily (set by default) and Range options, the latter enables the calendar for selecting the required time range for Product requests displaying;
* Product name column – displays the Product name;
* Request type column – displays the request type. For the User convenience Subscription requests are colored blue and Unsubscription requests are colored white;
* Request status column – displays the status of each request, statuses are also appear in different colors, namely Processing (colored white), Approved (colored green), Rejected (colored red), Canceled (colored gray);
* Date/Time column – contains the date and time when the request status was changed;
* Comment section – displays the comment left by admin when approving/rejecting the request.
* Cancel buttons – buttons for canceling the sent request. Available only for the ‘Processing’ status, provided that the request has not yet been processed by the admin, otherwise the button is not displayed.

{% hint style="warning" %}
Please note the the "Comment" section is inactive by default. In order to activate it, right-click the table header and check the appropriate option.
{% endhint %}

Pressing the ‘Cancel’ button will bring up the confirmation screen of the following look:

![](<../../../.gitbook/assets/image (976).png>)
