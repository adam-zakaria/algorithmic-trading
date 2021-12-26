# Introduction
If you make millions of dollars with this algorithm don't blame me! This was merely meant as an exercise, to feel like I've dabbled in the exciting world of trading. It was fun to think about strategies and price graphs. This runs, though I cannot vouch for its correctness. Please contact me if you want to discuss :)


# Run
<need to add a package installation step>
python3 momentum_trading.py

# Background
The program reads in a set of prices (a price history) that was manually retrieved from Binance and creates 'stretches' - a stretch is meant ot represent a period of time (a stretch of time) that a price is moving in a single direction (up or down, I can't remember how I handle staying constant). Average stretches are calculated: the average time of a price momvement. For instance, the average up stretch is 45 minutes, the average down is 29 minutes. The idea is that at 'the current time' I look at the current direction and how long the stretch has been. If the average stretch is longer than the current stretch, then hold the asset. Once the current stretch is wthin x time of the average stretch, sell.

Currently buy max will spend all of the starting funds on a single coin. Also, sell max sells all of the coins available at once.
  
![algorithmic trading graphs back](https://user-images.githubusercontent.com/5415505/147415490-dfda7d2f-fd94-4784-a00c-b084d8d6a9e5.png)

  
# Findings

If I started off this trading strategy at the beginning of the coin, I would've been better off just holding.
  
The tail of the program output:
```
------------------------
profit: $-998.2803310037507, 0.0x of initial savings
price: $1915.07
price increasing
Bought 0.0 coins at $1915.07 at time 936 for $1
savings: 0 num_coins: 0.0004266411871086535
------------------
Profits if held from first day:
14938.14
total_buys: 240
total_sells: 239
```
  
# Additional Notes
This is a very unsophisicated algorithm! get_average_stretch only considers how *long* a stretch is, not the *slope* of the stretch* - it does not consider how much a stretch is increasing or decreasing, just that it's doing one or the other. I
  
Another problem is that I train on the data I'm evaluating!
  
I think I'm also realizing I didn't implement a short. 
  
I'm also realizing there are probably a million more of these algorithms on quantopian like sites :)
  

  
# Additional Resources:
https://omscs.gatech.edu/cs-7646-machine-learning-trading
https://find.minlib.net/iii/encore/record/C__Rb3814960__Spython%20for%20finance__Orightresult__U__X7?lang=eng&suite=cobalt
https://www.amazon.com/Machine-Learning-Tom-M-Mitchell/dp/0070428077
https://www.amazon.com/What-Hedge-Funds-Really-Introduction/dp/1631570897/ref=pd_lpo_2?pd_rd_i=1631570897&psc=1
