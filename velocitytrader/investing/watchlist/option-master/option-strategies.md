# Option strategies

Option strategies are combinations of buying and selling options contracts that aim to achieve specific risk-return profiles.

In the Option chain and the Analyzer at the bottom of the screen there is a combo box that provides an opportunity to choose an option strategy.

<figure><img src="../../../.gitbook/assets/image (530).png" alt=""><figcaption></figcaption></figure>

By tapping on the <img src="https://lh7-us.googleusercontent.com/TJSiZ3mDGw0MPWrfU7qEPNxtIAoQBe_XhM2DWFjULHoj20dH0EFeR960SsOC5L8Q9EDezxnjEKeYbHqLpUyisI8EE7C7OwECiCWvFYBq_nKp9soxVQd-WqXhY5fkByXyvcCfgh3WDSOYNuxjvqEmIcM" alt="" data-size="line"> icon the full list of strategies will appear:

<figure><img src="https://lh7-us.googleusercontent.com/CjAfDqcY934zKpl38jLpMxGKKqDWi1Fve3-SM25sqGrsrM2rremOFR_UqrJFwZqFXT_6HJsvhV6KkKGtuEB-7ZuIA-60SU9zITnK4MGuvrN8G8E3PUecN75h0izun9ohvtSg3ypmEMsBAfnsgPe13jA" alt=""><figcaption></figcaption></figure>

And by tapping on the <img src="https://lh7-us.googleusercontent.com/vki_tnBOcr07kiWObS1DTM2zO6M8ZF8nzXBVkrky8pvQP1smkx0WZjVPRd3GXqUpk-A-bLuaPhrE8loR8zX9zN46OcEzpvFEbW0MOxBhGLRsH9v8Ss2VTzByMl0EwDzIme0u1c6QGiskijhe2LEiWMg" alt="" data-size="line"> icon the description of each strategy will be shown.

Also there are two additional options:

* Type - specifies the type of strategy(Call/Put).
* Side - specifies the side of the strategy(Sell/Buy).

<figure><img src="https://lh7-us.googleusercontent.com/MogivHtvMjQjAVt9YMhAfcO9VP4H14XEJg64odlAkNbpXNPs-7Kt4LOxL1Gb3-xhCYubqG3d2PzRGF-zdU9W-ALpOc7DZBkVvThSScBLN1j6CDpV5d3wPseh2bZOqxGoct9mVgqa47JKIDuU-oQxBIY" alt=""><figcaption></figcaption></figure>

By tapping on the Order Entry button, the following screen with the Order settings will appear:

<figure><img src="https://lh7-us.googleusercontent.com/rloqIq64vzSs7hnuE4Z3wU2_QB5zlHnh2m7yN_VFQ9LUiAZDf_6qzLqc8C0Vp7A7SJlDoJ9cHRe5xJGJiaWaH_nUUAtKfTOBpACuRrrV_OdeM_KNEocA3TJagTubKXAprimYZIx362hKR0PPfjXVyM4" alt=""><figcaption></figcaption></figure>

By pressing the Place strategy button the orders will be sent according to the chosen strategy.

{% hint style="info" %}
When the user switches between the Analyzer and the Option chain, the user’s settings for the selected strategy are retained.
{% endhint %}

#### Single option

A single-leg option is a basic strategy to buy or sell a Call/Put option. Depending on the side of a trade, there are four types of single-leg options:

* Long call - gives the right to buy the underlying stock at strike price;
* Long put - gives the right to sell the underlying stock at strike price;
* Short call - obligates to sell stock at strike price if the option is assigned;
* Short put - obligates to buy stock at strike price if the option is assigned.

Long calls and short puts are bullish strategies, whereas long puts and short calls are bearish strategies.

<figure><img src="https://lh7-us.googleusercontent.com/LbN87TuVXPgswzxtrDVkbgSspjxEY2qvaTFC73Jf05-azeCiI3N37_9FmTfEnzrBnIxCLw6MKLZScfa7fAXVTXQmxdk2zNckwUWCDQh0jvehvKZreu_SNT3-LZejWTtiqIHj0gJwbzdC1VFxRJe3Rmo" alt="" width="375"><figcaption></figcaption></figure>

#### Covered stock

The covered stock strategy combines a stock position with a corresponding option contract. An owner of the underlying stock sells call options on that stock. The ownership of the stock “covers” the obligation of the call options.

Strategy is often used by neutral to slightly bullish stock owners.

Note: Additional options Type and Side are available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/LMchT2AHOf4mBTd_weBXsdYDdIoAxJ8TgR6VGSxjlw780zdk3rHz47UTF0PAQJd0ZT20cEvxKfM2pAc6jBF6lThTkiNkIo4DQar-eZwVkfECG5XjOxnhIopYSAPY-45qns6FLUUXYf9VPgDgKbF4kWU" alt="" width="375"><figcaption></figcaption></figure>

#### Vertical spread

The vertical strategy refers to buying and selling two options with different strike prices at the same time, both of which have the same underlying stock, option type(Call/Put), and expiry date. The difference between the two options' strike prices is called the spread width.

Note: Additional options Type and Side are available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/KsiSwd7lGBEVXrGkJ2jYHMb1WAtmGQYt_u0Yv-NxuZ6QLc2YFZfcSQLkYCRfPMVA_Y394pB3F3y6cnR7BhQVVB3UIoyriU0vH5kBaf0c8iM316sKEPy_mczcO8sd3PEnW10MKOqHy-Ub2RT27JC93VI" alt="" width="375"><figcaption></figcaption></figure>

#### Straddle

The straddle strategy refers to holding both a call and a put with the same strike price, expiry date, and underlying stock. This strategy is often used when a significant price movement in the underlying asset is expected, but the direction of the movement is uncertain.

Note: Additional option Side is available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/gK8IPOyLPWdBDgYvoxIb7GQFxuYjN9Fwd5iSRF5xMZdYQbISth6iCZZ6q6EwblbelfRSJB4PEXN0S4GcYy7wo8Ib5WB8FOODSD8prP8-zugI2xNxBRhjFV7cZVjOtGTS6OtvRjzanN6-D5Cj-LMXa8g" alt="" width="375"><figcaption></figcaption></figure>

#### Strangle

The strangle strategy refers to holding both a call and a put with different strike prices but the same expiry date and underlying stock. When an investor is anticipating a swing in stock price (either a substantial rise or fall), he can profit from a long strangle if his judgment proves to be true. When he judges that the price of the underlying stock will experience little or no fluctuations, he can profit from short strangle.

Note: Additional option Side is available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/RByyBG9tI8W_-b4e-_VO8-pJ-smviasLuoFM-WiN70nBcGrXR0n0vY___6TdKkojVCdaZbk7bB2OdkS3DOxDzQ_1Ydg6ADUbdcNIv-7eJpY2VlbVuHaLjyvO37H3OFQMz0gRW7C0_QweW2sCcyPkG3M" alt="" width="375"><figcaption></figcaption></figure>

#### Butterfly

The butterfly strategy refers to holding either three calls or three puts at the same time. The option number ratio is 1:2:1, and the corresponding strike price spreads are equal. The three options have the same underlying stocks and expiry date. The butterfly strategy profits from predicting stock price fluctuations. When an investor has a neutral view on the underlying stock, he can profit from long butterfly if his judgment proves to be true. When an investor is anticipating a swing in stock price (either a substantial rise or fall), he can profit from short butterfly.

Note: Additional options Type and Side are available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/A3O_9E-wOgHuN2N-LF7SnkjMci9l4KBhHohx7b74vPbTKRpo9C8eTRqKl1KopCNfpmneD8gAW5YnXGH6y1f9jSMZx9-rE9yRSfJ6FG6OxjsVXf1p_hhjHq2w9kGJ0BTu3o8PTUdn2Qgx2N8JWEzDeA0" alt="" width="375"><figcaption></figcaption></figure>

#### Condor

The condor strategy refers to holding either four calls or four puts at the same time. The option number ratio is 1:1:1:1, and the corresponding strike price spreads are equal. The four options have the same underlying stocks and expiry date.

The condor strategy profits from predicting stock price fluctuations.

Note: Additional options Type and Side are available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/xh3dd-RQh7X1GdexQ-NQOamepB9EnTmQ7eyav2UPDdzN2hmuWTcF2fs7YTLwCN6hgHM7mfAPInheIuaWrWalF7b-LUbfImkcEj_vOPsUTTGNfU-PmOnOJDzoUtzJUupvOlc4iU7pDNM9qmuFPCvE_o4" alt="" width="375"><figcaption></figcaption></figure>

#### Collar

The collar strategy, also called a hedge wrapper, is an options strategy implemented to limit both large gains and losses.

The strategy can help protect gains against downside moves in stock price. A collar should be used when you have substantial unrealized gains on the long stock position or if you are bullish on the stock over the long term, but are unsure of its shorter-term prospects.

Note: Additional option Side is available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/SKcV22xA24jFq5Q55b7uyKikvbJ75SaHYdywQId_h00Dzu5Wf6xhB6qZUQ-w_pLsUukVYBe3WfSlGxEY7Z3WArnruHxIy-es0tOHpT4zzCJ_SJCp0C1bHcvU8hgAiCsunZC_C3olZ3UJnNO1g6GyB7E" alt="" width="375"><figcaption></figcaption></figure>

#### Iron Butterfly

An iron butterfly strategy is to simultaneously hold two call options and two put options of the same underlying stock, same expiration date, and same strike distance, with a ratio of 1:1:1:1. An iron butterfly strategy aims to make a profit by predicting price volatility. When an investor is neutral on a stock, he may profit from a short iron butterfly strategy.

Conversely, if he expects huge swings in stock, he can use a long iron butterfly strategy to make a profit.

Note: Additional option Side is available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/1RR0A-qaj7Aij3M9ysbbXHOkUMnSAJiWfwdcRUfEltDVgSinLpBt24ivoCEIVGufa6IEpuxToDu6gsiGjVTOKDn_5RsFHjFCKjhIZvF6YOSa6abZL-A4WpLrkGCi7TNVJIEqbVd89qIGkLr3scF-q8M" alt="" width="375"><figcaption></figcaption></figure>

#### Iron condor

An iron condor strategy is to simultaneously hold two call options and two put options of the same underlying stock, same expiration date, and same strike distance, with a ratio of 1:1:1:1. An iron condor strategy aims to make a profit by predicting price volatility. When an investor is neutral on a stock, he may profit from a short iron condor strategy.

Conversely, if he expects huge swings in stock, he can use a long iron condor strategy to make a profit.

Note: Additional option Side is available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/WKfb47nBLgSLKQ_ewtXKxWsDQryuxtjeDxt--221YW5wV1ynp9r-18yxLSLZNv0Oc-R0AW5x15LIQ29y3lBpMM1V83mT-xXGdGX707Ho2gqxcVgLDnozuh_778Vc4KIRUAqS7U1WX1Ck4Zr6twRgoIA" alt="" width="375"><figcaption></figcaption></figure>

#### Calendar

The calendar options strategy consists of purchasing a call option long-term and selling a call option short-term derived from the same financial instrument with the same exercise price but a different expiration date.

Note: Additional options Type and Side are available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/6PUw51BgVieByah9fgVCVvwhdri4jggNwurBH-ogxEExoWIGSWF7N--r_tO9hYDpKHOkJ0t4oPf4JMSZXQfUmm9iDB-tiOr_uPEKXIsIpERDND5LzGs3IEJLhAAp2Q0O2ZkB2QEazp8STXjFPvUZFnU" alt="" width="375"><figcaption></figcaption></figure>

#### Custom

A custom strategy means the availability to choose any options with different expiration dates to form a multi-Leg options strategy.

The 'Add Underlier' button is available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/OF3AX9BpGaaQXIMStmwJ0j_kh90Ln68GTbocc46PsenQ9JM_HXAlC0wo7cxouykjojBEpPc8etlRscKkRQkFsglh0o_3WLJiATgbBNuM1shI5Oya8Cay4CZ0ze3c31rnCHKnWdDOXouplok06e0miDk" alt="" width="375"><figcaption></figcaption></figure>
