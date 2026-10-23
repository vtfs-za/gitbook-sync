# Option strategies

Option strategies are combinations of buying and selling options contracts that aim to achieve specific risk-return profiles.

In the Option chain and the Analyzer at the bottom of the screen there is a combo box that provides an opportunity to choose an option strategy.

<figure><img src="../../../.gitbook/assets/image (1600).png" alt=""><figcaption></figcaption></figure>

By tapping on the <img src="../../../.gitbook/assets/image (1601).png" alt="" data-size="line"> icon on the right of the strategy name, the full list of strategies will appear:

<figure><img src="../../../.gitbook/assets/image (1602).png" alt="" width="292"><figcaption></figcaption></figure>

And by tapping on the <img src="../../../.gitbook/assets/image (1603).png" alt="" data-size="line"> icon the description of each strategy will be shown. Also there are two additional options:&#x20;

* Type - specifies the type of strategy(Call/Put).
* Side - specifies the side of the strategy(Sell/Buy).

<figure><img src="../../../.gitbook/assets/image (1604).png" alt="" width="375"><figcaption></figcaption></figure>

By tapping on the Order Entry button, the following screen with the Order settings will appear:

<figure><img src="../../../.gitbook/assets/image (1605).png" alt=""><figcaption></figcaption></figure>

By pressing the Place strategy button the orders will be sent according to the chosen strategy.

{% hint style="info" %}
When the user switches between the Analyzer and the Option chain, the user’s settings for the selected strategy are retained.
{% endhint %}

#### Single option&#x20;

A single-leg option is a basic strategy to buy or sell a Call/Put option. Depending on the side of a trade, there are four types of single-leg options:&#x20;

* Long call - gives the right to buy the underlying stock at strike price;
* Long put - gives the right to sell the underlying stock at strike price;
* Short call - obligates to sell stock at strike price if the option is assigned;
* Short put - obligates to buy stock at strike price if the option is assigned.

Long calls and short puts are bullish strategies, whereas long puts and short calls are bearish strategies.

<figure><img src="https://lh7-us.googleusercontent.com/y9Hc3EgmRZH4igKsROP9FHoBHg12AzuAGcVw1DlxRuibj-KBVyHLTUUqcTjl-FXW7Yw2J1wFOW-pY3M1YWh0Y6LRT77BAZOIhQHcTAeZpBQ39TKLRIbR_0LUfkC50skGAAph8sI6XMX3tw31xkGVhA4" alt="" width="375"><figcaption></figcaption></figure>

#### Covered stock&#x20;

The covered stock strategy combines a stock position with a corresponding option contract. An owner of the underlying stock sells call options on that stock. The ownership of the stock “covers” the obligation of the call options.

Strategy is often used by neutral to slightly bullish stock owners.

Note: Additional options Type and Side are available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/PAGMhu1uY3UcUif0ATvOrY_aPOqcU230xJJ3H3UBg-tbTVEkTWeyaNymm1xdJGHoQh-jF7BVc8VgoQCObAfp9aiN8OiVmhAJVsXK3NGOwwv9FsfUoGWnp_qhxwrp1ZHOtVsDxLWExovfX7O7xEdbgjk" alt="" width="375"><figcaption></figcaption></figure>

#### Vertical spread&#x20;

The vertical strategy refers to buying and selling two options with different strike prices at the same time, both of which have the same underlying stock, option type(Call/Put), and expiry date. The difference between the two options' strike prices is called the spread width.

Note: Additional options Type and Side are available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/b4BSxjLkwPEcxxGXyTVzYKsZUNI3imvYJL10ZN1yvU_K1HxwkvZZh74SpnfGq23ea_F5pKR4YAdWXjkMdi2OWZp0XGuEn1PBUc_EEQjPOnFqPzAm0_RvtqDnzWeqUGxOynnljRH16d9T_Cqs_2G75y0" alt="" width="375"><figcaption></figcaption></figure>

#### Straddle&#x20;

The straddle strategy refers to holding both a call and a put with the same strike price, expiry date, and underlying stock. This strategy is often used when a significant price movement in the underlying asset is expected, but the direction of the movement is uncertain.&#x20;

Note: Additional option Side is available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/ehl7a3T9S5JwjTmdmYlIpZc2EEZ3pAuVvkHSXvfPjd9fviC4X2uYs2LuUYJR2yzwtlZeLaYKzaMlmQhaV_xJC-A7UJTtsIGY3fo8o4V1MO8g4ARsWoCGwYZlnqOWf4wO4vUCIRf2jUjRdYOAEQmaqDQ" alt="" width="375"><figcaption></figcaption></figure>

#### Strangle&#x20;

The strangle strategy refers to holding both a call and a put with different strike prices but the same expiry date and underlying stock. When an investor is anticipating a swing in stock price (either a substantial rise or fall), he can profit from a long strangle if his judgment proves to be true. When he judges that the price of the underlying stock will experience little or no fluctuations, he can profit from short strangle.

Note: Additional option Side is available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/wUnKL-Bazw0kTjHm5nrHj6TOWnIUO2e0-tD6xhPu4iuJFce8ifrTPUA7xTXsIuBSJ-JyVdtg3Z-7nf6K3ysSs5A5kMhyFf8zauuacVbBAnM0iJgzks401uvcfMj-4raqT0kn63E0wHZK2Y0ABItcOgM" alt="" width="375"><figcaption></figcaption></figure>

#### Butterfly&#x20;

The butterfly strategy refers to holding either three calls or three puts at the same time. The option number ratio is 1:2:1, and the corresponding strike price spreads are equal. The three options have the same underlying stocks and expiry date. The butterfly strategy profits from predicting stock price fluctuations. When an investor has a neutral view on the underlying stock, he can profit from long butterfly if his judgment proves to be true. When an investor is anticipating a swing in stock price (either a substantial rise or fall), he can profit from short butterfly.

Note: Additional options Type and Side are available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/0rYknvayUmXwFvskabvXH-c9ixBJIDToDv2I5cOrsPUFT5KVBG_QQLCYRV8--MbbkANYJHEJgq-tOgqkNgO4c4JLaml6Cp1LR-wGkNOmfiKVCAelXdXf46_2BZD-_Bl1YGx6aWtY-Mlf8wmAAFcYH3M" alt="" width="375"><figcaption></figcaption></figure>

#### Condor&#x20;

The condor strategy refers to holding either four calls or four puts at the same time. The option number ratio is 1:1:1:1, and the corresponding strike price spreads are equal. The four options have the same underlying stocks and expiry date.&#x20;

The condor strategy profits from predicting stock price fluctuations.&#x20;

Note: Additional options Type and Side are available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/vj7gbvTEe7fk6YSQt5sq6iqqEczwiSNpYokGLsvloiirOJKdHxAwA-JQOC8uH8UlQfEbIuag2jL005o92WvWfIkSaZe-q7I5DIH2uFx5bocHOW5x99zdTXDtH3ySb1KP_JDB27c4_5gLLvdtoYhUK3s" alt="" width="375"><figcaption></figcaption></figure>

#### Collar

The collar strategy, also called a hedge wrapper, is an options strategy implemented to limit both large gains and losses.

The strategy can help protect gains against downside moves in stock price. A collar should be used when  you have substantial unrealized gains on the long stock position or if you are bullish on the stock over the long term, but are unsure of its shorter-term prospects.

Note: Additional option Type is not available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/qZzG-_n1SLiR3nyYUZTwnH-4qe7WZItyZ6QuwJN159zmR0CAHt0KUxW78xPsswtXrLWcjTeaxS_75amTXNS57Z6ma_ccxYGPIAdVaDFYa4UXTBm2TYQPYSlcxmXXP7l0Pey9dXTfDbU3MLnSsXNNpas" alt="" width="375"><figcaption></figcaption></figure>

#### Iron Butterfly

An iron butterfly strategy is to simultaneously hold two call options and two put options of the same underlying stock, same expiration date, and same strike distance, with a ratio of 1:1:1:1. An iron butterfly strategy aims to make a profit by predicting price volatility. When an investor is neutral on a stock, he may profit from a short iron butterfly strategy.

Conversely, if he expects huge swings in stock, he can use a long iron butterfly strategy to make a profit.

Note: Additional option Type is not available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/q9nKhY6tm6c5TvbgenIjFWmeP7iu3kn_LFDulNNrMUOEcqoi8uIWHw_wm5_QXkEfb56iiaNdM3J5dJ0FMfTiYs-fxpc6WcyTMrz6wwN6BHiOxqD-CERfQrXYWywVDKcfpr_UI10sR9fP_N1SUcxekcY" alt="" width="375"><figcaption></figcaption></figure>

#### Iron condor

An iron condor strategy is to simultaneously hold two call options and two put options of the same underlying stock, same expiration date, and same strike distance, with a ratio of 1:1:1:1. An iron condor strategy aims to make a profit by predicting price volatility. When an investor is neutral on a stock, he may profit from a short iron condor strategy.

Conversely, if he expects huge swings in stock, he can use a long iron condor strategy to make a profit.

Note: Additional option Type is not available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/VRufgNMer4BQdqwExsJbZ9Nk2Vay19EhR-C8Vir9hWhB3wJGXwUTFof6WL6D33caH7cb4I0vkF8U1x25Cn9TB01W4kTXMyh-9PaGGQy74dH99um0eNidvTubVZFm9ed3hFrtV4EG4-RCJQwMQ50ffT4" alt="" width="375"><figcaption></figcaption></figure>

#### Calendar&#x20;

The calendar options strategy consists of purchasing a call option long-term and selling a call option short-term derived from the same financial instrument with the same exercise price but a different expiration date.

Note: Additional options Type and Side are available for this strategy.

<figure><img src="https://lh7-us.googleusercontent.com/ef4YWsHGdY9AfyqQjSArHFLPIuRV57JpdeM5az8dUjVRkvfrCcEdYp5DPo2pNTjolPXx_KJ6NB3wgIt4z9t0yYjSaMBSNJtBkJOSzeJJrxbaoUGiUHeCWUC6OJKzABFHmF453qYoGp2nO3atUBQ_hao" alt="" width="375"><figcaption></figcaption></figure>

#### Custom

A custom strategy means the availability to  choose any options with different expiration dates to form a multi-Leg options strategy.

Note: Additional options Type and Side are not available for this strategy.

The 'Add Underlier' button is available for this strategy.

<figure><img src="../../../.gitbook/assets/image (1097).png" alt="" width="424"><figcaption></figcaption></figure>
