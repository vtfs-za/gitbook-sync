# Account details

The Account details screen is accessible through the Watchlist, Positions and Orders screens. Tap the ‘Projected balance’ section to open Account details screen. To select the account available for a user, tap the <img src="../../.gitbook/assets/image (170).png" alt="" data-size="line"> button at the top of the screen:

<figure><img src="../../.gitbook/assets/image (169).png" alt="" width="375"><figcaption></figcaption></figure>

In order to view detailed information about an account, tap its name.

<figure><img src="../../.gitbook/assets/image (171).png" alt="" width="375"><figcaption></figcaption></figure>

_P/L, %_ = _Open Gross P/L \* 100 / (Projected Balance - Open Gross P/L)_

#### **Account Summary**

* **Balance** – current realized balance of the account. If there is trading with pending valuation, balance won’t change before clearing, on which P/L will be credited by covered trades or delivery of funds will be performed by uncovered trades. Fees are charged off from the balance at the time of accrual.
* **Projected balance** – future balance which includes all accrued and not accrued profit/loss. After closing all positions, accrual of fees and assets' delivery, the balance becomes equal to a projected balance.\
  Projected balance = Balance + Unsettled cash + Loss + Profit + Blocked for Stocks + Option premium + Collateral + Blocked for Fixed Income.
* **Available funds** – amount of funds which can be used for placing a new order.\
  Available funds = Balance & All risks - Margin used.
* **Blocked balance** – balance blocked by broker or by user for withdrawal/transfer.
* **Cash balance** – current cash balance of the account.
* **Unsettled cash** – cash sum of unsettled account operations, which have not been delivered to an account yet and will be delivered in accordance with T+N settlement system.
* **Incoming funds** – the total amount of all unsettled Deposit account operations in the account currency.
* **Withdrawal available** – shows an amount of funds that you can withdraw immediately from your account.\
  Withdrawal available = Available funds – Credit value – Profit – Unsettled profit — Unsettled loss available for withdrawal + Unused unsettled negative cash for stocks – Unsettled positive cash for stocks + Unused unsettled negative premium — Unsettled positive premium + Unsettled premium from open sell — Used premium from open sell -Stocks liquidity + Withdrawable cash for stocks + Withdrawable unsettled profit/loss + Withdrawable unsettled collateral + Unused intraday initial margin — Used overnight initial margin for intraday — Accrued dividends + Withdrawable options premium- ∑Unsettled account operation(Deposit) + Unused unsettled negative cash for fixed income – Unsettled positive cash for fixed income + Withdrawable cash for fixed income + Unused unsettled negative accrued interest – Unsettled positive accrued interest.
* **Option value** – current option value in portfolio. Can be positive for a long Net position or negative for a short Net position.\
  Option value = ∑ (Current option price \* Amount \* Cross price).
* **Stocks liquidity** – a part of a total cost of assets, which is accounted in available margin if there are assets on the trader’s account.\
  Stocks liquidity = ∑ (Amount \* Price \* Cross price \* (Liquidity rate / 100)), where Amount = Qty \* Lot size.
* **Stocks value** – total cost of stocks, positions which were opened on the selected account.\
  Stocks value = ∑ (Current stock price \* Amount \* Cross price), where Amount = Qty \* Lot size.
* **Available cash** – indicates the amount of funds available for investment before utilizing leverage.\
  Available cash = Projected balance - Portfolio value, where\
  Portfolio value = sum of all position values across instruments,\
  Position value = Current price \* Quantity \* Lot size \* Cross price.
* Fixed income value - value of all open positions with the margin type Fixed income pre-paid.\
  Fixed income value = ∑(Current price × Quantity × Lot size × Cross price × (Face value / 100));

***

#### **Margin**

* **Margin available** – full margin which is available to maintain portfolio at the current moment.
* **Init. margin req.** – amount of the initial margin blocked for all positions and orders taking into account the margin crossing.
* **Init. margin req., %** – shows how much margin is used in relation to Balance & All risks.\
  Initial margin req. % = (Initial margin req. / (Balance & All risks - Stock orders req.)) \* 100%.
* **Margin warning level** – percentage value set on the account level. Defines the threshold of Maint. margin req, %, at which a Margin warning message is sent.\
  Warning margin level = (Margin warning % / 100) \* (Balance & All risks - Stock orders req).
* **Waived margin** – threshold value of Maintenance margin at which a Margin warning message is sent.
* **Blocked for stocks** – amount of funds debited from a balance in case of Equities trading. After closing such position, funds will be returned to an account.\
  Blocked for stocks = abs (∑ Stock operation).
* **Stocks order req.** – total margin blocked for Equities.
* **Option premium req.** – option premium for buy orders.
* **Warn. margin req.** – warning margin requirement for positions and orders.
* **Warn. margin req., %** – warning margin requirement in relation to Balance & All risks.
* **Maint. margin req.** – total margin used for maintenance of a current portfolio in account currency.
* **Maint. margin req., %** – shows current level of risks. When Maint. margin req=100%, stop-out triggers.
* **Margin before warning** – margin available before the warning triggering.
* **Initial margin without waived** – initial margin excluding waived margin.
* **Stop out level** – stop out threshold as a percentage.
* **Stop out value** – value that should be reached in order for stop out to be triggered.\
  Stop out value = Maint. margin req. / (Stop out level / 100).
* **Blocked for fixed income** - amount of funds currently blocked for open Fixed income pre-paid positions.
* **Fixed income orders req**. - required margin for all pending orders with Fixed income pre-paid margin type.
* **Blocked for options** - total amount of option premiums for all open positions, calculated as the sum of settled and unsettled Option premium Account operations. Debit operations are added, and credit operations are subtracted. The value can be negative if short positions are allowed.\
  Calculated as:\
  _&#x42;locked for options_ = _∑Option premium_

***

#### **Account Activity**

* **Open gross P/L** – current unrealized gross profit/loss for all open positions.\
  Open gross P/L = ∑ (Open gross P/L(i)).
* **Open net P/L** – current unrealized net profit/loss for all open positions.\
  Open net P/L = ∑ (Open net P/L(i)).
* **Open positions** – currently opened positions.
* **Working orders** – all created orders visible to a user.
* **Total position value** – the sum of all position values for an account.\
  Total position value = ∑ (Position value(i)),\
  Position value = Current price \* Quantity \* Lot size \* Cross price.

***

#### **Today Result**

* **Today’s net profit** – Net profit/loss for today.
* **Today’s gross profit** – Gross profit/loss for today.
* **Today’s fee** – amount of fees paid today.
* **Today’s volume** – total volume traded today.
* **Today’s trades** – number of trades executed today.

***

#### **Risk management**

* **Trading status** - trading status of the selected account. Can show if trading is active, suspended, closed, or disabled due to risk rules or pattern day trading rules.
* **Daily loss** - shows the current daily net loss value for the account.
* **Daily loss limit** - maximum allowed daily loss. Trading is blocked when the current daily loss reaches this value. Displayed as: **Daily loss / Daily loss limit**.
* **Weekly loss - s**hows the current weekly net loss value for the account.
* **Weekly loss limit** - maximum allowed weekly loss. Trading is blocked when the weekly loss reaches this value. Displayed as: **Weekly loss / Weekly loss limit**.
* **Current unrealized loss** - shows the current unrealized loss on open positions.
* **Unrealized loss limit** - maximum allowed unrealized loss. If this threshold is reached, trading may be disabled. Displayed as: **Current unrealized loss / Unrealized loss limit**.
* **Projected balance** - shows projected account balance, including unsettled cash, profit/loss, blocked funds, and premiums.
* **Trailing drawdown level** - maximum allowed trailing drawdown based on the projected balance. Displayed as: **Projected balance / Trailing drawdown level**.
* **Max. drawdown level** - minimum projected balance value the account can have during the day. Displayed as: **Projected balance / Max. drawdown level**.
* **Max. relative drawdown level** - minimum projected balance value allowed relative to the account balance. Displayed as: **Projected balance / Max. relative drawdown level**.
* **EOD trailing drawdown level** - minimum projected balance value that the account must maintain at the end of the day.
* **Max orders count per day** - maximum number of orders that can be placed or modified in a day. Displayed as: **Current orders count / Max orders count per day**.
* **# Max. positions** - maximum number of simultaneously open positions. Displayed as: **Current positions # / Max. positions**.
* **# Max. pending orders** - maximum number of pending (not yet executed) orders. Displayed as: **Current pending orders # / Max. pending orders**.
* **Total max position qty** - maximum total quantity (in lots) of all positions and orders. Displayed as: **Current total qty / Total max position qty**.
* **Max order amount** - maximum allowed amount for a single opening order, measured in instrument units.
* **Daily profit target** - maximum allowed daily net profit. Displayed as: **Current daily profit / Daily profit target**.
* **Loss limit per trade** - maximum allowed loss per single trade. Calculated as a percentage of the daily loss limit.
* **Total NOP limit per user** - maximum summary volume allowed across all trading accounts belonging to the user. Value is set in lots/contracts, in amount (Lots\*Lot size or Lots\*Tick cost/Tick size) or in money exposure.
* **Exposure limit** - Maximum allowed exposure for all symbols in the symbols group.\
  The values are displayed in the following format:\
  _&#x43;urrent exposure value_ / _Max position value per instrument group_

***

#### **Other Definitions**

* **Option premium** – option premium value.\
  Option premium = ∑ (Open price \* Qty \* Lot size \* Cross price).
* **Open price** – average price of a position opening.
* **Qty** – quantity of a position in lots.
* **Lot size** – Tick cost / Tick size.
* **Cross price** – average cross price for conversion into account currency.
* **Free commission** – amount available for covering trading fees. Once spent, regular fees apply.

***

### **Account actions**

Account actions - is a set of actions that are allowed to the particular account.

It is available in the Account menu <img src="https://lh7-us.googleusercontent.com/docsz/AD_4nXdEnJ91BNC7DzEGtPYXfWOj5RemODqXKK_QHNYTQXCJg5VmqTWEb9TFO68X_g4qq4B-Ona7DFiBD-ZsnUV9OpCIBmUXcWFNkjW1mdspfkNf8BD02qDEqvMcc-K9gUiDIlxFXqSu_3feTMiEw5NM1UrBdtXe?key=i34kSG4duM_DXcQbimGXZQ" alt="" data-size="line"> when it is allowed for this account:

<figure><img src="../../.gitbook/assets/image (172).png" alt="" width="375"><figcaption></figcaption></figure>

* Withdrawal - a process of taking money out of an investment account.
* Change password - an option for replacing current password with a new one.
* Close account request - an option for users to send requests to close their accounts.

**Close account**

After clicking the ‘Close account’ option, the following confirmation screen will appear:

<figure><img src="../../.gitbook/assets/image (173).png" alt="" width="375"><figcaption></figcaption></figure>

By clicking the “Send request” button the request for closing an account is created and the following screen with ability to cancel a request will appear:

<figure><img src="../../.gitbook/assets/image (174).png" alt="" width="375"><figcaption></figcaption></figure>

Important note - while the request is being processed, there are no restrictions on the use of the account.

There are 4 possible statuses of the closing account requests:

* Submitted - request has been successfully submitted;
* Accepted - the necessary actions will be completed shortly and the account will be closed;
* Rejected - request is rejected;
* Cancelled - request is cancelled.
