# Run:
<need to add a package installation step>
python3 momentum_trading.py

# Background
The program reads in a set of prices (a price history) that was manually retrieved from Binance and creates 'stretches' - a stretch is meant ot represent a period of time (a stretch of time) that a price is moving in a single direction (up or down, I can't remember how I handle staying constant). Average stretches are calculated: the average time of a price momvement. For instance, the average up stretch is 45 minutes, the average down is 29 minutes. The idea is that at 'the current time' I look at the current direction and how long the stretch has bene. If the average stretch is longer than tha current stretch. Then hold the asset. Once the current stretch is wthin x time of the average stretch, sell.

Currently buy max will spend all of the starting funds on a single coin. Also, sell max sells all of the coins available at once.


https://omscs.gatech.edu/cs-7646-machine-learning-trading
https://find.minlib.net/iii/encore/record/C__Rb3814960__Spython%20for%20finance__Orightresult__U__X7?lang=eng&suite=cobalt
https://www.amazon.com/Machine-Learning-Tom-M-Mitchell/dp/0070428077
https://www.amazon.com/What-Hedge-Funds-Really-Introduction/dp/1631570897/ref=pd_lpo_2?pd_rd_i=1631570897&psc=1
