# Backtesting Types/Setup

### **Backtesting Types**

There are two types of backtesting available in EvoCode:

* Quick backtesting
* Visualize backtesting

&#x20;Select Backtesting mode on the top menu of EvoCode window by clicking on the<img src="../../.gitbook/assets/3 (127).png" alt="" data-size="original"> button.

The Quick backtesting allows users rapidly testing strategies on historical data without the chart visualization during backtesting. In this mode, the chart with all details about opened and closed positions will only appear after the backtesting is finished.

The Visualize backtesting option allows users to see what is happening on the chart while the backtest is taking place.

### **Backtesting Setup**&#x20;

Before start of backtesting user can setup all required properties. Click on the<img src="../../.gitbook/assets/1 (175).png" alt="" data-size="original">button to evoke the Backtesting Setup window.

![](<../../.gitbook/assets/2 (51).png>)

* Main symbol – evokes the lookup for selection of the main symbol for backtesting.
* Additional symbols – evokes the lookup for selection of additional symbols for backtesting.
* Aggregation – allows to select the type of aggregation (time) of historical data.
* Range – allows selecting time interval during which the module backtesting will be conducted. It is also available to select custom range by selecting ‘Custom’ option in the drop-down menu.
* Modelling scheme – the following schemes are available:

&#x20;        \-  1m - Close – one minute bars close price are used for generation.

&#x20;        \-  1m - Open – one minute bars open price are used for generation.

&#x20;        \-  1m - OHLC – one minute bars: Open, High, Low, Close, prices are used for generation.

&#x20;        \-  1 D - Close – one day bars close price are used for generation.

&#x20;        \-  1 D - Open – one day bars open price are used for generation.

&#x20;        \-  1 D - OHLC – one day bars: Open, High, Low, Close, prices are used for generation.

* Balance – initial deposit amount.
* Latency – time latency during backtesting process which emulates the slippage that occurs during a real trade.
* Trade session – allows to set the scope of a trading session when it starts and when it ends.
* Execution by – allows to select which type of historical data will be played for backtesting.&#x20;
* Cancel Day Orders Time – allows to select time when all user’s daily orders will be closed.
