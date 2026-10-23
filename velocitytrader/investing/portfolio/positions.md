# Positions

The Positions tab displays a list of opened positions with short information about every position: a symbol by which a position was opened, quantity and Net P/L. Quantity of long positions is green, quantity of short positions is red. Every new opened position appears at this tab immediately.

<figure><img src="../../.gitbook/assets/portfolio positions 1.png" alt="" width="375"><figcaption></figcaption></figure>

Swipe left the card of the selected position and the following buttons will become available:

<figure><img src="../../.gitbook/assets/portfolio positions 2.png" alt="" width="375"><figcaption></figcaption></figure>

To see the details of a certain position, just tap the corresponding ![](<../../.gitbook/assets/image (538).png>) icon.

![](<../../.gitbook/assets/3 (3).jpg>)

The ![](<../../.gitbook/assets/image (539).png>) button is available only if the Option exercise style is American. Tapping the Exercise button evokes the following confirmation screen:

![](<../../.gitbook/assets/9 (2).png>)

Tap the “Exercise position” button, if you need to send a request for early expiration of the Option.&#x20;

Tap the "Exercise position" button to open the Order entry window with the same side of the order, as the position (for Long->Buy, for Short->Sell). In the opened OE window a user has to go through the following steps to place an order:&#x20;

**Step 1:**&#x20;

* Select the order type - 3 order types are available for selection: Market, Limit and Stop;

<figure><img src="../../.gitbook/assets/image (1237).png" alt="" width="375"><figcaption></figcaption></figure>

* Set quantity - set the order's volume in either lots (Quantity), currency (Cash) or shares (Shares), depending on the account’s permissions:

<figure><img src="../../.gitbook/assets/image (35).png" alt="" width="319"><figcaption></figcaption></figure>

**Step 2 (for Limit orders):**&#x20;

Set limit price.

<figure><img src="../../.gitbook/assets/image (36).png" alt="" width="322"><figcaption></figcaption></figure>

**Step 3:**&#x20;

See the information about the order before sending.

<figure><img src="../../.gitbook/assets/image (339).png" alt="" width="325"><figcaption></figcaption></figure>

After that a user can send the order. The confirmation screen will be shown in case, if it is configured in settings.

<figure><img src="../../.gitbook/assets/image (1634).png" alt="" width="295"><figcaption></figcaption></figure>

{% hint style="info" %}
Note that broker can prohibit American-style options from being exercised if the strike price is out of the money.
{% endhint %}

Overnight execution - if active, the order will be eligible to be placed during overnight market hours.

The <img src="../../.gitbook/assets/image (1204).png" alt="" data-size="line"> button evokes the confirmation screen for Position closing:

<figure><img src="../../.gitbook/assets/image (1205).png" alt="" width="375"><figcaption></figcaption></figure>

### Mutual closing

The user can mutually close two positions one by another if this feature is available to him. In order to do this, the user should swipe the first position and select the Mutual close option:

<figure><img src="../../.gitbook/assets/image (1080).png" alt=""><figcaption></figcaption></figure>

After this is done, all positions available for mutual closing in a pair with the selected position will be highlighted:

<figure><img src="../../.gitbook/assets/image (1081).png" alt=""><figcaption></figcaption></figure>

Please note that Mutual closing can be carried out when two positions for the same instrument are selected. The following conditions must be met in order for a mutual closing to be available:

* Positions to close must be selected for the same instrument;
* These positions must be oppositely directed (i.e. both Long and Short positions must be selected);
* In case the partial close is forbidden for this account, then the amount on both sides (Long and Short) must be equal;
* Only two positions can be selected;
* All positions must belong to the same account.

To call the Context menu, press and hold (Long tap) on the needed item: &#x20;

<figure><img src="../../.gitbook/assets/image (474).png" alt=""><figcaption></figcaption></figure>

Actions available in the Context menu:

* Chart/Info - by tapping, the Chart with the position symbol will be opened;
* Details - tap and detailed description of the position will be opened;
* Increase - opens the position modifying window;
* Close - closes the selected position.
