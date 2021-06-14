import csv
import sys
"""
author: Adam Zakaria
inspiration: passive income, hero's journey, do something, literate programming
stretch-goal: self-expression
more:
get in a rhythm versus pushing.
use paper like you would math: must
relax vocal chords
move and dance
use left eye
imagination and fun, like Ed - computing isn't cold and cranking like they say
"""
#read in all the prices so we can iterate over them
closing_prices = []
with open('./ETHUSDT_720.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        closing_prices.append(row[4])
closing_prices = [float(i) for i in closing_prices]
def create_stretches(price_list):
    direction, price_increase, price_decrease, time_increasing, time_decreasing = '',0,0,0,0
    increases, decreases = [], []
    for i in range(0, len(price_list)-2):
        if (price_list[i+1] - price_list[i] >= 0.0):
            price_increase += price_list[i+1] - price_list[i]
            time_increasing += 1
            if (direction == 'down'):
                decreases.append((time_decreasing, price_decrease))
                time_decreasing, price_decrease = 0,0
            direction = 'up'
        if (price_list[i+1] - price_list[i] < 0.0):
            price_decrease += price_list[i+1] - price_list[i]
            time_decreasing += 1
            if (direction == 'up'):
                increases.append((time_increasing, price_increase))
                time_increasing, price_increase = 0,0
            direction = 'down'
    return increases, decreases
def get_averages(increases, decreases):
    average_price_decrease,average_time_decrease = 0.0,0.0
    average_price_increase,average_time_increase = 0.0,0.0
    for price,time in increases:
        average_price_increase += price
        average_time_increase += time
    average_price_increase = average_price_increase / len(increases)
    average_time_increase = average_time_increase / len(increases)
    for time,price in decreases:
        average_price_decrease += price
        average_time_decrease += time
    average_price_decrease = average_price_decrease / len(decreases)
    average_time_decrease = average_time_decrease / len(decreases)
    print(f'average_price_increase: {average_price_increase}')
    print(f'average_time_increase: {average_time_increase}')
    print(f'average_price_decrease: {average_price_increase}')
    print(f'average_time_decrease: {average_time_decrease}')
    return average_price_increase, average_time_decrease, average_price_decrease, average_time_decrease
def get_current_stretch(price_list):
    first = True
    direction = 0
    time = 0
    prices = []
    if(len(price_list) <= 1):
        return -1
    for i in reversed(range(0, len(price_list))):
        if first:
            if(price_list[i-1] <= price_list[i]):
                direction = 'up' 
            else:
                direction = 'down' 
            first = False
            prices.append(price_list[i])
        else:
            time += 1
            prices.append(price_list[i])
            if direction == 'up':
                if(price_list[i-1] >= price_list[i]):
                    print(f"prices for stretch: {prices[::-1]}")
                    return (price_list[-1] - price_list[i], time, direction)
            else:
                if(price_list[i-1] < price_list[i]):
                    print(f'prices for stretch: {prices[::-1]}')
                    return (price_list[i] - price_list[-1], time, direction)
#This should be called every tick
#Need to figure out what to do with a small price history
def short_or_long(price_list, average_price_increase, average_time_increase, average_price_decrease, average_time_decrease):
    (price_change, time, direction) = get_current_stretch(price_list)
    if direction == 'up':
        print('direction == up')
        if (price_change >= (average_price_increase * .95)): #The price is expected to go up
            print('short')
            return 'short'
        else:
            print('long')
            return 'long'
    else: #direction == down
        print(f'current stretch price change: {price_change}')
        print(f'average_price_decrease: {average_price_decrease}')
        print(f'average_time_decrease: {average_time_decrease}')
        print(f'length of stretch: {time}')
        print('direction == down')
        if (price_change <= (average_price_decrease * 1.05)):
            print('long')
            return 'long'
        else:
            print('short')
            return('short')
#region closing_prices
"""
print('----------------------')
print('closing_prices')
positive_stretches, negative_stretches = create_stretches(closing_prices)
average_price_increase, average_time_increase, average_price_decrease, average_time_decrease = get_averages(positive_stretches, negative_stretches)
short_or_long(closing_prices,average_price_increase, average_time_increase, average_price_decrease, average_time_decrease )
print('----------------------')
#endregion
#region test_prices2
print('----------------------')
print('test_prices2')
#test_prices1 = [1,2,3,4,3,2,3,4,5,6,7,8,7,9,10,11,12,13,14,13,12,11,10,9,10,11]
test_prices2 = [1,10, 13, 5, 22, 32, 4, 29]
increases, decreases = create_stretches(test_prices2)
average_price_increase, average_time_increase, average_price_decrease, average_time_decrease = get_averages(increases, decreases)
short_or_long(test_prices2,average_price_increase, average_time_increase, average_price_decrease, average_time_decrease)
#endregion
"""

#spends all savings to buy a coin
def buy(price, savings):
    if savings == 0:
        print('Tried to buy, but savings are $0, exiting.')
        quit()
        #sys.exit()
    num_coins = price / savings
    savings = 0
    return savings, num_coins

def sell(price, coins_holding):
    savings = coins_holding * price
    return savings 

closing_prices = [10, 13, 16, 19, 23]
first = True
holding = False
savings = 1000.0
num_coins = 0.0
for t in (range(1, len(closing_prices))): 
    if closing_prices[t] - closing_prices[t-1] > 0: #increasing
        if not holding:
            savings, num_coins = buy(closing_prices[t], savings)
            print(f'Bought {num_coins} coins at ${closing_prices[t]} at time {t} for ${num_coins * closing_prices[t]}')
    elif closing_prices[t] - closing_prices[t-1] < 0: #decreasing, if same, do nothing
        if holding:
            savings = sell(closing_prices[t], num_coins)
            print(f'Sold {num_coins} coins at ${closing_prices[t]} at time {t} for ${num_coins * closing_prices[t]}')

print(f'savings: {savings} num_coins: {num_coins}')

def get_volatility():
    return 0



"""
*Additional Notes*
~On the code~
increases and decreases do not include the last stretch because our strategy is 
to compare the latest stretch to the previous stretches to decide if we should 
buy or sell.






~For the future~
I need to test short_or_long to make sure it works as expected
I need to backtest to see if there's any sign it might work
Can I find if there are any similarities across cryptocurrencies?
Can I do something that will more clearly make money? Arbitrage check - Ebay purchases.
"""