# Managed account statistics panel

This panel shows statistics for those accounts which are under the control of the MAM manager. The panel must be activated by the admin so that the user can see it in the terminal. Also, the admin can activate the "Update MAM summary only" rule for the account, in which case the account will not have any information in the Account details section except the Balance amount. Additional source of information for such an account will be the Managed account statistics panel that shows account operations that took place.

The panel itself can be found in the Account drop-down list located in the header of the terminal, pick the corresponding option in order to open it:

<figure><img src="../../../.gitbook/assets/mam windows.jpg" alt=""><figcaption></figcaption></figure>

The panel includes account operations of three types: Trading, Deposit, and Withdrawal. Thus, the user can see the results of the trade that the MAM manager carried out on his behalf. The following columns are available in the table:

* Account - displays the name of the account on whose behalf the operation was made;
* Symbol - the name of the instrument with which the operation was performed;
* Date - date/time of the operation;
* Operation type - operation type, as it was mentioned above can be: Trading, Deposit, and Withdrawal;
* Operation ID - unique identifier of the operation stored in the database;
* Side - displays operation side: Buy or Sell;
* Amount - displays the volume of this specific operation;
* Open/Close price - price at which a position was opened/closed;
* Quantity - amount of a position, either in lots or in units, depending on what is selected in the Settings dialog box;
* Currency - operation currency;
* Period selector - can be daily or range, defines the period for which the history will be shown.

The panel context menu contains the following additional options:

* Search - launches a search box inside the panel;
* Export - when clicked, calls the Export screen (CSV, Excel, Print to...);
* Settings - opens the panel settings;
* View -> Show totals checkbox - activates the total sum for the Quantity and Amount columns.
