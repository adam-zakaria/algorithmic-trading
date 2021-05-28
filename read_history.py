import csv
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
    last_parity, positive_sum, negative_sum, positive_time_sum, negative_time_sum = 0,0,0,0,0
    positive_stretches, negative_stretches = [], []
    for i in range(0, len(price_list)-2):
        if (price_list[i+1] - price_list[i] >= 0.0):
            positive_sum += price_list[i+1] - price_list[i]
            positive_time_sum += 1
            if (last_parity == -1):
                negative_stretches.append((negative_time_sum, negative_sum))
                negative_time_sum, negative_sum = 0,0
            last_parity = 1
        if (price_list[i+1] - price_list[i] < 0.0):
            negative_sum += price_list[i+1] - price_list[i]
            negative_time_sum += 1
            if (last_parity == 1):
                positive_stretches.append((positive_time_sum, positive_sum))
                positive_time_sum, positive_sum = 0,0
            last_parity = -1
    return positive_stretches, negative_stretches
def get_averages(positive_stretches, negative_stretches):
    negative_price_avg,negative_time_avg = 0.0,0.0
    positive_price_avg,positive_time_avg = 0.0,0.0
    for price,time in positive_stretches:
        positive_price_avg += price
        positive_time_avg += time
    positive_price_avg = positive_price_avg / len(positive_stretches)
    positive_time_avg = positive_time_avg / len(positive_stretches)
    for time,price in negative_stretches:
        negative_price_avg += price
        negative_time_avg += time
    negative_price_avg = negative_price_avg / len(negative_stretches)
    negative_time_avg = negative_time_avg / len(negative_stretches)
    return positive_price_avg, positive_time_avg, negative_price_avg, negative_time_avg
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
                direction = 1
            else:
                direction = -1
            first = False
            prices.append(price_list[i])
        else:
            time += 1
            prices.append(price_list[i])
            if direction == 1:
                if(price_list[i-1] >= price_list[i]):
                    print(f"prices for stretch: {prices[::-1]}")
                    return (price_list[-1] - price_list[i], time, direction)
            else:
                if(price_list[i-1] < price_list[i]):
                    print(f'prices for stretch: {prices[::-1]}')
                    return (price_list[i] - price_list[-1], time, direction)
def short_or_long(price_list,positive_price_avg, positive_time_avg, negative_price_avg, negative_time_avg):
    (price, time, direction) = get_current_stretch(price_list)
    if direction == 1:
        if (price >= (positive_price_avg * .95)):
            print(f'current stretch price change: {price}')
            print(f'positive_price_avg: {positive_price_avg}')
            print(f'positive_time_avg: {positive_time_avg}')
            print(f'length of stretch: {time}')
            print('direction == 1')
            print('SHORT')
            return 'SHORT'
    else: #direction == -1
        if (price <= (negative_price_avg * 1.05)):
            print(f'current stretch price change: {price}')
            print(f'negative_price_avg: {negative_price_avg}')
            print(f'negative_time_avg: {negative_time_avg}')
            print(f'length of stretch: {time}')
            print('direction == -1')
            print('LONG')
            return 'LONG'

positive_stretches, negative_stretches = create_stretches(closing_prices)
positive_price_avg, positive_time_avg, negative_price_avg, negative_time_avg = get_averages(positive_stretches, negative_stretches)
short_or_long(closing_prices,positive_price_avg, positive_time_avg, negative_price_avg, negative_time_avg )

test_prices1 = [1,2,3,4,4,3,3,5,6,7,8,7,9,10,11,12,13,14,13,12,11,10,9,10,11]

print('----------------------')
positive_stretches, negative_stretches = create_stretches(test_prices1)
positive_price_avg, positive_time_avg, negative_price_avg, negative_time_avg = get_averages(positive_stretches, negative_stretches)
short_or_long(test_prices1,positive_price_avg, positive_time_avg, negative_price_avg, negative_time_avg)

#I need to test short_or_long to make sure it works as expected
#I need to backtest to see if there's any sign it might work
#Can I find if there are any similarities across cryptocurrencies?
#Can I do something that will more clearly make money? Arbitrage check - Ebay purchases.

"""
How do I test it? I could look at the prices and see if the answers are sensible.
#get the last 10 closing prices:
closing_prices[-10:]

I kind of want more information: What is the mean, median, and mode.
Okay - so when the price goes up it tends to go up by 30 each stretch, and there's an upward trend overall.

"""