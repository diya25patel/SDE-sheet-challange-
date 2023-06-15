from os import *
from sys import *
from collections import *
from math import *

def nextPermutation(num, n):
    i=len(num)-1
    while i>0 and num[i-1]>=num[i]:
        i=i-1
    if i<1:
        num[:]=num[::-1]
    else:
        j=len(num)-1
        while num[j]<=num[i-1]:
            j=j-1
        num[i-1], num[j]= num[j], num[i-1]
        num[i:]=reversed(num[i:])
    return num
