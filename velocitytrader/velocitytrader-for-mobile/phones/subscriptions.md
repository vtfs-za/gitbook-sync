# Subscriptions

The Subscriptions panel lists all products currently available to the User, products the User has subscribed to, and subscription/unsubscription requests that he has submitted. In order to open the panel select it from the More section that is located in the main menu of the mobile app. The panel contains two tabs:

* Subscriptions – this tab contains a list of Products that are available to the User for subscription, as well as Products to which the user has already subscribed, i.e. those subscription requests which are confirmed by the Admin or automatically;
* Requests – contains subscribe/unsubscribe requests sent by the user.

### **Subscriptions tab**

<figure><img src="../../.gitbook/assets/image (1678).png" alt="" width="375"><figcaption></figcaption></figure>

This tab displays cards of products to which the user is subscribed, as well as available to the User for subscription.&#x20;

The upper part of the panel contains filtering drop-down with the following available values:

* All – displays all products;
* Subscribed – displays products that the user is subscribed to;
* Available for subscription – displays products available for subscription to this user;
* Processing – displays products which are awaiting processing by the admin.

All Product cards are grouped into specific categories, which are assigned by the Admin in the Product settings. Each category can be collapsed/expanded by pressing on it. Product cards contain the name of the Product, its logo, price, and the ‘Subscribe’ button. Note that this button can have two states depending on the product status,so it can be shown as the "Unsubscribe" To scroll through a category, simply swipe it to the left.

In case the logo was not received from the server, <img src="../../.gitbook/assets/image (549).png" alt="" data-size="line"> will be displayed instead. In the upper right corner of each Product card there is the ![](https://lh4.googleusercontent.com/wEkGlYW5qSeJGHTfyYQ96E205vVVvX6eswwVSDiOvyIqiCWYDMiZO2C1vohXpdkVT2EocJhTeZqUkXKP588MgCx4qBNH7unwz8yPzCq6tFHxD6setKlOMPpkztGfxpuJlrM5ko-t) button, tap it to open the detailed  information about the Product.

If the Product already has an active request awaiting processing by the admin, the button for its canceling is displayed instead of the "Subscribe/Unsubscribe" buttons:

<figure><img src="../../.gitbook/assets/image (1680).png" alt="" width="375"><figcaption></figcaption></figure>

Cards of Products, that the User has already subscribed to, have the corresponding ‘Unsubscribe’ button which respectively serves to unsubscribe from the required Product:

<figure><img src="../../.gitbook/assets/image (1679).png" alt="" width="231"><figcaption></figcaption></figure>

Depending on the Market data subscriber status the product card displays the Pro price or Non-pro price or _FREE_ (if there is no charge for using the product). If Market data subscriber status is not defined, then both prices separated by a slash are displayed at once on the product card, the display format is \<non-pro price> / \<pro price> \<currency>.

{% hint style="warning" %}
In order for the system to determine the Market data subscriber status, the user must first go through the appropriate procedure.
{% endhint %}

#### Subscribing

Subscription to the Product of interest is carried out by clicking the "Subscribe" button. This will send a request for subscription which should be approved by admin or the subscription can be performed automatically without his participation. If the Product already has an active request awaiting processing by the admin, the "Cancel request" button is displayed instead of the "Subscribe" button. This allows the user to quickly and easily cancel a subscription request without switching to the Requests tab.

After applying the subscription, the User is shown with the following info screen:

<figure><img src="../../.gitbook/assets/image (1681).png" alt="" width="375"><figcaption></figcaption></figure>

{% hint style="warning" %}
If the User does not have enough funds to pay the fee, or if there are no available User accounts to be charged for using the Product, then he will receive a corresponding reject. This is only valid in the case of automatic request confirmation/charging.&#x20;
{% endhint %}

There are two subscription options - if the User does not need to sign additional documents or if there is a need to sign them.&#x20;

If the documents are not required to be signed, then the subscription request will be created immediately after clicking the appropriate button. This request will await verification by the admin and after its confirmation the User will be subscribed to the Product.

In case it is required to sign documents in order to subscribe to the Product, then an additional ‘Sign documents’ screen that allows to take the necessary actions will be shown to the User:

<figure><img src="../../.gitbook/assets/image (1682).png" alt="" width="375"><figcaption></figcaption></figure>

This screen contains the following elements:

* The name of the document, which is displayed in the upper part of the screen;
* The content of the document displayed in the main part of the screen;
* When acquaintance with the documents is finished, the ‘Done’ will become active;
* Number of pages in the document displayed  in the lower part of the screen and is utilized to indicate the progress made when signing documents;
* In case the required fields are missing on the current page, the system will display a corresponding message and will not allow the User to move to the next page.

#### Unsubscribing

When tapping the "Unsubscribe" button, the mechanism for unsubscribing from the required Product is launched and the User will be asked to confirm his unsubscription:

<figure><img src="../../.gitbook/assets/image (1683).png" alt="" width="375"><figcaption></figcaption></figure>

{% hint style="warning" %}
Please note that after confirmation, the User will be immediately unsubscribed, without waiting for the end of the period for which the fee was charged.&#x20;
{% endhint %}

If the Product already has an active request awaiting processing by the admin, the "Cancel request" button is displayed instead of the "Subscribed" button. Thus, if the request was not processed immediately, the user can always cancel it with this button.

{% hint style="warning" %}
The availability of the "Unsubscribe" button is regulated by the administrator for each product individually.
{% endhint %}

### **Requests tab**

This tab displays all requests sent by the User for subscribing/unsubscribing to the Products for the selected period:

<figure><img src="../../.gitbook/assets/image (1684).png" alt="" width="375"><figcaption></figcaption></figure>

The Requests tab contains the following elements:

* Period selector located under the tab’s name contains the Daily (set by default), Two day to date, Week to date, and Month to date options for selecting the required time range for Product requests displaying;
* Subscription – displays the Product name;
* Request type – displays the request type. For the User convenience Subscription requests are colored blue and Unsubscription requests are colored white;
* Request status – displays the status of each request, statuses also appear in different colors, namely Processing (colored white), Approved (colored green), Rejected (colored red), Canceled (colored gray). The second line under the status displays Date/Time when this status was assigned.

When approving/rejecting a request, the Admin can leave a comment that will explain the reason of the current request status. If such a comment has been left, it will be displayed as the![](https://lh5.googleusercontent.com/uHiq4X3YJeDTiuu2NJ_Oe3X2WnclIilIvrzbPCWmtHLtt-_L7GyCb4jnDzI_ow6roI7jN9P4EI3kjWR7BY65ktxmJujblsU3MZteIsfd5uxPc_ke2RY5Aod9ihHgMW4-JUw5aUPV)icon next to the status. To expand a comment, simply tap on its icon.

Tapping any request line will initiate request cancelling and bring up the appropriate confirmation screen.&#x20;

{% hint style="warning" %}
Please note that only those requests that have the ‘Processing’ status can be canceled.
{% endhint %}
