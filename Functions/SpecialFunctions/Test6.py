def sortedList(a,b):
    l=[]
    if(a<b):
        l.append(a)
    return l


import functools
print('Enter the values split by space : ')
lst=[int(val) for val in input().split()]


sorted = functools.reduce(sortedList,lst)
print(sorted)