# Positions

The Positions screen displays all opened positions. Every new opened position appears in this screen immediately.

<figure><img src="../../.gitbook/assets/image (86).png" alt="" width="375"><figcaption></figcaption></figure>

The Positions screen displays a list of opened positions with short information about a symbol on which every position was opened: quantity and open price. Quantity of long positions is blue, quantity of short positions – red.

When viewing a position, the user can quickly switch to the chart to assess its current state and return back to the selected position. In order to do this swipe left the card of the selected position and the following buttons will become available:

<figure><img src="../../.gitbook/assets/image (87).png" alt="" width="375"><figcaption></figcaption></figure>

To call the Context menu, press and hold (Long tap) on the needed item: &#x20;

<figure><img src="../../.gitbook/assets/image (1718).png" alt="" width="375"><figcaption></figcaption></figure>

Actions available in the Context menu:

* Chart - by tapping, the Chart with the selected symbol will be opened;
* Symbol info - tap and detailed description of the symbol will be opened;
* Modify - this option allows Modifying needed position;
* Close - by tapping on this button, the following options will be available, if they are allowed to the user:
  * Close via OE - opens Order Entry to close the selected position;
  * Close Mkt - closes selected Position;
  * Close all with negative/positive P\&L - closes all positions with negative or positive P\&L by sending market orders for each qualifying position;
  * Close Long/Short positions - closes all Long or Short positions;
  * Close all with negative/positive P\&L (by Symbol) - closes all positions for the selected instrument with negative or positive P\&L for each qualifying position;
  * Close Long/Short positions (by Symbol) - closes all Long or Short positions for the selected instrument;
  * Close all by Symbol - closes all positions for the selected Instrument regardless of side or P\&L.

{% hint style="warning" %}
Also the additional positions closing options are available by tapping the Account icon <img src="../../.gitbook/assets/image (1720).png" alt="" data-size="line"> from the Positions screen, if they are allowed for the user.
{% endhint %}

To quickly go to the chart, just tap the corresponding icon. To return back to the order, tap the ‘Back’ button depicted as an arrow<img src="https://lh5.googleusercontent.com/FeoB164MubEhRzjZI288O316A51qKXagx2sSMaReRPOJ5NDeC1l862wWctT_U2Wkbuni-qTC-7pAzYNKFJxG5Z_SP7h57i4K3CKTGGyWTnOqE0msvOjWah_NT_36eIuww74QtXeI" alt="" data-size="line">in the upper left part of the chart. The same actions can be performed with superpositions as well.

In order to get full information about a symbol, tap a symbol's name.

<figure><img src="../../.gitbook/assets/image (89).png" alt="" width="375"><figcaption></figcaption></figure>

* Open price – price at which the position was opened;
* Current price – market price obtainable from a broker;
* Stop loss – Stop loss price set for a position;
* Take profit – Take profit price set for a position;
* Fee – shows the total commission amount taken for a position;
* Date/time – shows date and time when a position was opened;
* Account – login name of an account that opened a position;
* Position ID – unique number that the trading system assigns to each position;
* Trading exchange - shows the exchange name which is set on a server for the order;
* Gross P/L – total profit/loss of the order;
* Position value - current value of the position. Note that the calculation is based on current market price;
* Strategy ID – identifier of an execution strategy that opened position;
* SL/TP validity - shows the validity (TIF) selected for the position Stop loss/Take profit;
*   Position exposure – exposure of a position, in the account currency. Calculated on base of an open price:

    Position exposure = Price \* Quantity \* Lot size \* Cross price (quoting CCY > account currency) – calculation for Forex

    Position exposure = Price \* Quantity \* (Tick cost/Tick size) \* Cross price (quoting CCY > account currency) – calculation for Futures

    In all cases Cross price (quoting CCY > account currency) is a current cross price.
*   Exercise – sends an exercise request for the Option position. Available for single positions opened for Options with Exercise style=American, inactive for multiple selected positions.&#x20;

    After clicking this menu item, the Position exercise request confirmation dialog box is displayed. Clicking the "Exercise" button in the confirmation box, creates a request for the Option exercise, which switches the position to Pending exercise status and prevents performing the following operations for the position: **Modify position, Close position, Close all.**

    The mentioned actions are reenabled for the position after the "Cancel exercise" action is performed.\
    Also note that broker can prohibit American-style options from being exercised if the strike price is out of the money.
*   Cancel exercise – cancels an exercise request for the selected Option position with Pending exercise status. Available for single positions opened for Options with Exercise style=American, inactive for multiple selected positions.

    After clicking this menu item, a confirmation dialog box is displayed, which requires a confirmation of canceling an Option exercise request. After the exercise Option request is canceled, the **Modify position, Close position, Close all** operations become allowed for the position.  &#x20;

In order to modify a position, tap the 'Modify' button and the following screen will be opened:

<figure><img src="../../.gitbook/assets/image (90).png" alt="" width="375"><figcaption></figcaption></figure>

Here you can modify stop loss, take profit or trailing stop. For positions with the _Net position by average price_ netting type and if both values of the trading modes (Intraday\Delivery) are available for the Instrument\Account pair, and also if the _Allow trading mode modification_ role is active for this user, this screen will have the additional controls:

* Target product type – combobox that allows selecting the target product type, contains values except the current one;
* Modify quantity – switchable numeric for indicating the modification qty. The default value is Modify quantity = Quantity - Start of day qty. Please note that this value cannot be greater than Today traded qty. In case this numeric is enabled, SL/TP price controls are automatically disabled;
* SL/TP price – Stop loss, Take profit, and Trailing stop prices available for modification. These controls are disabled in case the “Modify quantity” control is active.&#x20;

{% hint style="warning" %}
The user can also have _Positions close only_ or _Liquidation only_ status depending on his plan. In this case, product type can not be modified and an appropriate reject message is sent to the user.
{% endhint %}

In order to close a position, tap the button 'Close', and the following intuitive screen allowing a partial position closing will be opened:  &#x20;

&#x20;                                             ![](<../../.gitbook/assets/image (657).png>)

The field 'Qty. to close' allows to indicate some quantity of lots to close. This option is active, when it is allowed on the server-side with broker's settings. Also, the 'Position closing' confirmation must be activated in the ‘Settings’ menu.

All positions can be closed at once with a special button that is disabled in the app by default. This feature can be useful for managers or admins, in case there is a need to close all currently opened positions. The "Close all" button is securely hidden in the Account menu to prevent accidental pressing. In order to enable this feature, please contact our support.

### Mutual closing

The user can mutually close two positions one by another if this feature is available to him. In order to do this, the user should swipe the first position and select the Mutual close option:

<figure><img src="../../.gitbook/assets/image (658).png" alt=""><figcaption></figcaption></figure>

After this is done, all positions available for mutual closing in a pair with the selected position will be highlighted.

Please note that Mutual closing can be carried out when two positions for the same instrument are selected. The following conditions must be met in order for a mutual closing to be available:

* Positions to close must be selected for the same instrument;
* These positions must be oppositely directed (i.e. both Long and Short positions must be selected);
* In case the partial close is forbidden for this account, then the amount on both sides (Long and Short) must be equal;
* Only two positions can be selected;
* All positions must belong to the same account.
