# Copy trading

The Copy Trading Panel allows users to manage their copy trading settings, enabling them to replicate the trading activity of a master account across selected follower accounts. This feature streamlines trading operations and ensures synchronized execution of trades across multiple accounts. The panel can be accessed from the Account drop-down menu <img src="../../.gitbook/assets/image (367).png" alt="" data-size="line"> in the terminal's Top menu.

<figure><img src="../../.gitbook/assets/image (1638).png" alt=""><figcaption></figcaption></figure>

The panel consists of the following key components:

* From account (Master Account) - displays a list of the user's accounts with an Active status that can act as master accounts;
* To accounts (Followers) - a multi-select dropdown list of the user's accounts eligible to follow the master account. Only accounts with an Active status can be added as followers;
*   Start button - use this button to initiate copy trading. Once started, trades made by the master account will be automatically copied to the selected follower accounts.\
    A confirmation screen will be displayed, asking users to confirm the start of copy trading:<br>

    <figure><img src="../../.gitbook/assets/image (1639).png" alt=""><figcaption></figcaption></figure>
* Stop button - this button stops copy trading. Once stopped, the follower accounts will no longer replicate trades from the master account. A confirmation screen will be displayed before stopping copy trading:

<figure><img src="../../.gitbook/assets/image (1640).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
* Only accounts with an **Active** status can participate in copy trading as either a master or follower.
* When the status of a master or follower account changes to something other than **Active**, it will be automatically unsubscribed from all copy trading relationships.
{% endhint %}

### Example

Let's consider the following setup:

<figure><img src="../../.gitbook/assets/image (1641).png" alt=""><figcaption></figcaption></figure>

* Master Account: Managed - this account acts as the master account, executing trades that will be copied to the follower accounts;
* Follower Account: Managed3 - this account is a follower, meaning it will replicate the trades made by the master account.

When the position is opened on the master account, the same position is automatically opened on the follower account by the copy trading mechanism:

<figure><img src="../../.gitbook/assets/image (1643).png" alt=""><figcaption></figcaption></figure>

**Trade on the Master Account**:

* **Instrument**: GBP/USD
* **Direction**: Long
* **Quantity**: 0.01
* **Price**: 1,35069

**Trade Replicated on the Follower Account**:

* **Instrument**: GBP/USD
* **Direction**: Long
* **Volume**: 0.01
* **Price**: 1,35069
