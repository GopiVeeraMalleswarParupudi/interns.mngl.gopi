'''
write a program which will accept the list of values and find the highest and lowest elements 
from a given list of elements.
'''
def min(a,b):
    if a<b:
        return a
    else:
        return b
    
    
import functools
lst=[int(val) for val in input().split()]
sortLst = list(functools.reduce(min,lst))
print(sortLst)