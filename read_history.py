import csv
"""
author: Adam Zakaria
inspiration: passive income, hero's journey, do something, literate programming
stretch-goal: self-expression
more:
get in a rhythm versus pushing.
use paper like you would math
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