'''
write a program whichh will accepts list of values both positive and negative values, now find 
the sum of positive values and negative values seperatedly
'''
import functools
print('Enter the value seperated by space : ')
lst=[int(val) for val in input().split()]
positiveVal=list(filter(lambda val:val>0,lst))
negativeVal=list(filter(lambda val:val<0,lst))
print('Sum({})= {}'.format(positiveVal,functools.reduce(lambda a,b:a+b,positiveVal)))
print('Sum({})= {}'.format(negativeVal,functools.reduce(lambda a,b:a+b,negativeVal)))