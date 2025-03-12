import functools
print('Enter the values seperated by space : ')
lst=[int(val) for val in input().split()]
positiveSum=functools.reduce(lambda val1,val2:val1+val2,filter(lambda val:val>0,lst))
negativeSum=functools.reduce(lambda val1,val2:val1+val2,filter(lambda val:val<0,lst))
print('Sum of positive numbers : {}\nSum of negative numbers : {}'.format(positiveSum,negativeSum))