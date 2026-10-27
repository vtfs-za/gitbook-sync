# Option master

The Option chain screen shows detailed information about a specific option contract and allows a user to trade from this panel.

<figure><img src="https://lh7-us.googleusercontent.com/cy1ixIwOfoNFby1ckXWcyZGDQhGAFMRW1LdUa4TgwfYEaMKnEgMyGv5iM1i6iMC0zErJ4nKsj9jTdE1fIMUvmxiRW_cwaozNGSNtjsbxf7qpnKFOaYwVLVTfjaiYb5R9PqDC7C8qBqIODItMR3KtG6c" alt=""><figcaption></figcaption></figure>

Swipe left the instrument at the Watchlist screen and select the corresponding item to open the Option chain panel.

<figure><img src="../../../.gitbook/assets/2 (1).JPEG" alt="" width="355"><figcaption></figcaption></figure>

To call the Context menu, press and hold (Long tap) on the needed item:

<figure><img src="../../../.gitbook/assets/image (476).png" alt=""><figcaption></figcaption></figure>

Actions available in the Context menu:

* Chart/Info - by tapping, the Chart with the selected symbol will be opened;
* Add to watchlist - this option allows adding selected item to Watchlist;
* Remove - deletes the symbol from the Option panel.

Under the header of the Option chain screen a user can see the Info bar which displays the following data:

* Last - last price by underlier;
* Change, % - change in percentage by underlier;
* Volume - volume by underlier;
* Previous close - the previous day's close price.

The Option chain table contains 3 columns:

* Calls - this column shows the cards of Call strikes that display the following information: Ask, Bid, IV, OI (Open interest), Change. Other parameters can be configured in the Panel settings;
* Strike - the Strike price;
* Puts - this column shows the cards of Put strikes that display the following information: Ask, Bid, IV, OI, (Open interest), Change. Other parameters can be configured in the Panel settings.

In Option chain panel the coloring method “By difference” is used. Depending on what type of price change comes at a certain strike to buy or sell, it is highlighted in green or red.

IV (Implied volatility) column shows the expected volatility of the option which characterizes the degree of underlier price volatility. If IV is high, strong fluctuations of underlier price are expected.

The Open interest column shows the total amount of open positions.

Tap Ask or Bid button on the Option chain screen to select the strike (Leg). It is possible to select several strikes. Tap one more time to delete the Leg from selected ones. Orders can be added to the strategy from different option series for a given underlier.

<figure><img src="../../../.gitbook/assets/image (1122).png" alt=""><figcaption></figcaption></figure>

At the bottom of the screen there is a panel ![](<../../../.gitbook/assets/image (1121).png>) that gives the opportunity to select different option strategies. Learn more about each available strategy in the following [Option strategies](./) article.

Also there is a information about the number of selected strikes:

<figure><img src="../../../.gitbook/assets/image (1124).png" alt=""><figcaption></figcaption></figure>

The following buttons are also available here:\
![](<../../../.gitbook/assets/image (1125).png>) - allows removing all selected Legs;

![](<../../../.gitbook/assets/image (1120).png>) - allows opening the Order entry screen;

![](<../../../.gitbook/assets/image (1126).png>) - allows opening the Analyzer screen.

### Analyzer

By tapping ![](<../../../.gitbook/assets/image (1077).png>) button, a user will get to the graphical data section:

<figure><img src="https://lh7-us.googleusercontent.com/Gv-4hfI__zPQqeOycLwpPS9R5g2LQjggAb8ovl7Edy-at5rs3nK_tUaMbUBJERkmEohdifK8_Yew8pTMWXjNnP1X530wFKByOalsIkfVJddt1gAHhwY_D2NQdZLIfrT3obYZe19PBZ4k11ZWPfnknuE" alt=""><figcaption></figcaption></figure>

“Legs” section displays the list of orders. Tap the Arrow button to show/hide this section. Tap the “Add underlier” button to add a Leg by underlier. The following parameters are available for viewing:

* Intrinsic P/L - profit calculated by the Expiration curve;
* P/L - profit calculated by the Current curve;
* What if - profit calculated by the Timeline curve;
* Potential gain - the largest positive P/L value for the total profile;
* Potential loss - minimum negative P/L value for the total profile.

In addition to the standard parameters of the symbol, the screen also contains Greeks. Greeks are the coefficients used for the characteristics of option cost sensitivity to the changing of various values: Delta, Gamma, Vega and Theta.

* Delta – is the first derivative of the option price by the underlier price; shows how option price will be changed in points, if the underlier price changes by 1 point.
* Gamma – is the second derivative of the option price by the underlier price; shows the rapidity of the option delta change.
* Vega – is the first derivative of the option price by volatility; shows how option price will be changed in points, if the volatility changes by 1%.
* Theta – is the first derivative of the option price by time; shows how the option price will be reduced after one day.

### Order entry

To send orders from the Option chain panel, open Order entry by tapping the ![](<../../../.gitbook/assets/image (1075).png>)button:

<figure><img src="../../../.gitbook/assets/image (1109).png" alt=""><figcaption></figcaption></figure>

Order entry screen is divided into groups for each Leg. If a trader has several accounts, it is possible to change them, using a control displayed above the list of Legs. Tap ![](<../../../.gitbook/assets/image (1110).png>) button to delete the Leg from the list. Tap ![](<../../../.gitbook/assets/image (1111).png>) button to show/hide the details of a Leg. Tap the “Place strategy” button to send orders.

**Settings**

In order to manage the panel settings, tap the ![](<../../../.gitbook/assets/image (1108).png>) button.

A user can configure settings in the “Field editor” section. A user can activate/deactivate the necessary parameters for displaying in the Call and Put option card.

![](<../../../.gitbook/assets/2 3.png>)

![](<../../../.gitbook/assets/1 5.png>)
