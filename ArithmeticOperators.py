'''
write a program which demonstrates the functionality of arithmetic operators.
'''
a=float(input("Enter the first value : "))
b=float(input("Enter the secound value : "))
print("-"*40,"\nArithmetic Operators\n","-"*40)
print("Additional operator : {}+{} = {}".format(a,b,(a+b)))
print("Subtraction operator : {}-{} = {}".format(a,b,(a-b)))
print("Multiplication operator : {}*{} = {}".format(a,b,(a*b)))
print("Division operator : {}/{} = {}".format(a,b,(a/b)))
print("Floor division operator : {}//{} = {}".format(a,b,(a//b)))
print("Modulo division operator : {}%{} = {}".format(a,b,(a%b)))
print("Exponentiation operator : {}**{} = {}".format(a,b,(a**b)))