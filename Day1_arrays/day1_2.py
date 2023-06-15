from os import *
from sys import *
from collections import *
from math import *

def printPascal(n):
    # Write your code here.
    # Return a list of lists.
    n = int(n)
    output = []
    for i in range(n):
        if(i == 0):
            prev = [1]
            output.append(prev)
        else:
            curr = [1]
            j = 1
                
            while(j < i):
                curr.append(prev[j-1] + prev[j])
                j+=1
            curr.append(1)
            output.append(curr)
            prev = curr
    return output       
        