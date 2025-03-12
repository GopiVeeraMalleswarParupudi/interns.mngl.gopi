'''
write a program which will accept list of values form keyborad and find their product.
'''
import functools
print("Enter the sequence of inputs which are seperated by space : ")
lst=[int(val) for val in input().split()]
prod = functools.reduce(lambda a,b :a*b,lst)
print(prod)