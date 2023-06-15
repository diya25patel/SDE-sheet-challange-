from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    r= len(matrix)
    c= len(matrix[0])        
    dummy_r=[-1]* r        
    dummy_c=[-1]* c        
    for i in range (r):            
        for j in range (c):                
            if matrix[i][j]==0:                    
                dummy_r[i]=0                    
                dummy_c[j]=0                
    for i in range(r):            
        for j in range(c):                
            if dummy_r[i] == 0 or dummy_c[j] == 0:                    
                matrix[i][j] = 0 