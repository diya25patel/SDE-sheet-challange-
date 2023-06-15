from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    # Write your code here.
    maxpro=0
    minprice=10e10

    for i in range(len(prices)):
        minprice= min(minprice, prices[i])
        maxpro= max(maxpro, prices[i]-minprice)

    return maxpro