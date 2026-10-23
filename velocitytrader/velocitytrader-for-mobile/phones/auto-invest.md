# Auto-invest

Auto-Invest is a feature that allows users to automate their investment strategy by setting up predefined investment plans. Instead of manually placing orders, users can schedule recurring investments in selected instruments based on a fixed schedule and funds allocation. With this feature users can build long-term investment strategies without needing to place each order manually, making investing more efficient and stress-free.

In order to open the Auto-invest panel please proceed to the More tab and select the according option.&#x20;

The panel itself displays all active and inactive Auto-Invest plans as cards:

<figure><img src="../../.gitbook/assets/image (184).png" alt="" width="375"><figcaption></figcaption></figure>

Each plan card shows:

* Plan name.
* Status (_Active_ / _Stopped_).
* Execution Scheme (schedule name).
* Investment amount.
* Instrument Allocation (logos of selected instruments).
* Buttons for managing the plan (from left to right):
  * Execute now - immediately places investment orders based on the plan’s settings.
  * Status (Pause/Activate) - toggles the plan between _Active_ and _Stopped_.
  * Edit - opens the plan settings for modification.
  * Remove - deletes the plan permanently.

In order to create a new auto-invest plan, tap on the "+" icon in the right bottom part of the panel., the following screen will be opened:

<figure><img src="../../.gitbook/assets/image (185).png" alt="" width="375"><figcaption></figcaption></figure>

* Name **-** enter a custom name for the plan (default: _Auto-invest Plan #_).
* Instrument allocation:
  * Click “+ Add” to select investment instruments.
  * Assign a percentage to each instrument (total must be 100%).
  * A maximum of 5 instruments can be selected.
* Investment amount - enter the total amount to invest. This amount of funds will be allocated between the instruments in accordance with the selected percentage.&#x20;
* Schedule - select an Execution scheme from the dropdown list. These schemes are created by the admin user.&#x20;
* End date - set the expiration date for the plan. After expiration, the plan will automatically stop executing. Default value is 365 days from today.&#x20;
* Check the Funds allocation preview to see estimated order amounts.
* Click “Create” to save the plan.

🚨 Plan Creation Restrictions:

* The total allocation must equal 100%.
* The investment amount must be greater than 0.
* You cannot create more than the allowed number of plans (default: 3).

The plan editing is performed in the same way as creating, to edit the currently existing plan, tap the Edit button on its card.&#x20;

Please note that you can execute your plan manually if there is such a need. Find the plan in the Auto-invest panel and tap the "Execute now" button on its card. The system will place orders immediately based on the set allocation.

Tap on the plan card to open the full details:

<figure><img src="../../.gitbook/assets/image (187).png" alt="" width="375"><figcaption></figcaption></figure>

* Plan name - the name of the Auto-invest plan.
* Plan status - displays whether the plan is _Active_ or _Stopped_.
* The pie chart visually represents how funds are allocated across different instruments. Each segment of the chart corresponds to an instrument, the **size** of each segment reflects the allocation percentage.&#x20;
* Below the pie chart, the investment breakdown is also displayed in table format.&#x20;
* Available actions are the same as on the card: Execute now, Stop, Edit, and Remove.&#x20;

💡 The Event log contains entries associated with auto-invest plans like Created, Executed, Expired, etc.
