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
def change_direction(p1, p2, p3):
    if(p2-p1 >= 0 and p3-p2 >= 0):
        return True
    elif p2-p1 < 0 and p3-p2 < 0:
        return True
    else:
        return False 
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
positive_stretches, negative_stretches = [], []
positive_stretches, negative_stretches = create_stretches(closing_prices)
negative_price_avg,negative_time_avg = 0.0,0.0
positive_price_avg,positive_time_avg = 0.0,0.0
for price,time in positive_stretches:
    positive_price_avg += price
    positive_time_avg += time
positive_price_avg = positive_price_avg / len(positive_stretches)
positive_time_avg = positive_time_avg / len(positive_stretches)
for time,price in positive_stretches:
    positive_price_avg += price
    positive_time_avg += time
positive_price_avg = positive_price_avg / len(positive_stretches)
positive_time_avg = positive_time_avg / len(positive_stretches)
for time,price in negative_stretches:
    negative_price_avg += price
    negative_time_avg += time
negative_price_avg = negative_price_avg / len(negative_stretches)
negative_time_avg = negative_time_avg / len(negative_stretches)
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
                    print(f'prices for stretch: {prices}')
                    return (price_list[i-1], time, direction)
            else:
                if(price_list[i-1] < price_list[i]):
                    print(f'prices for stretch: {prices}')
                    return (price_list[i-1], time, direction)

#Should be called every minute
#I guess this doesn't really work with currencies that have little price data. But maybe there are patterns across currencies
def short_or_long(price_list):
    (price, time, direction) = get_current_stretch(price_list)
    if direction == 1:
        if (price >= (positive_price_avg * .95)):
            print(f'current_price: {price}')
            print(f'positive_price_avg: {positive_price_avg}')
            print(f'time: {time}')
            return 'SHORT'
    else: #direction == -1
        if (price <= (negative_price_avg * 1.05)):
            print(f'current_price: {price}')
            print(f'negative_price_avg: {negative_price_avg}')
            print(f'time: {time}')
            return 'LONG'

short_or_long(closing_prices)
