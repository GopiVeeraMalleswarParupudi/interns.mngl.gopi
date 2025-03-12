'''
write a program which will accepts a list of values and find their sum by using reduce function.
'''
import functools
print('Enter sequence of values which are sepearated by space : ')
lst=[int(val) for val in input().split()]
res = functools.reduce(lambda x,y : x+y,lst)
print('sum({}) = {}'.format(lst,res))