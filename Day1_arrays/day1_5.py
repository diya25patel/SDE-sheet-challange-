from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def sort012(arr, n) :

	# write your code here
    # don't return anything 
    c_0=0
    c_1=0
    c_2=0

    for i in arr:
        if i==0:
            c_0+=1
        elif i==1:
            c_1+=1
        else:
            c_2+=1
        
    for j in range(c_0):
        arr[j] = 0

    for j in range(c_0, c_0 + c_1):
        arr[j] = 1

    for j in range(c_0 + c_1, len(arr)):
        arr[j] = 2



#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
