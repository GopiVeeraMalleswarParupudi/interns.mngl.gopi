'''
write a program which accepts two integer values and compute all the arithmetic operations by using multiple 
assignment operator.
'''
a=int(input("Enter the first number : "))
b=int(input("Enter the secound number : "))
print("-"*15,"\nResult\n","-"*15)
add,sub,mul,div,floorDiv,mod,exp=(a+b),(a-b),(a*b),(a/b),(a//b),(a%b),(a**b)
print("Additional operator : {}+{} = {}".format(a,b,(add)))
print("Subtraction operator : {}-{} = {}".format(a,b,(sub)))
print("Multiplication operator : {}*{} = {}".format(a,b,(mul)))
print("Division operator : {}/{} = {}".format(a,b,(div)))
print("Floor division operator : {}//{} = {}".format(a,b,(floorDiv)))
print("Modulo division operator : {}%{} = {}".format(a,b,(mod)))
print("Exponentiation operator : {}**{} = {}".format(a,b,(exp)))
'''
PS D:\PythonFullStack\CorePython> & "C:/Program Files/Python313/python.exe" d:/PythonFullStack/CorePython/MultilineAssignmentOperator.py
Enter the first number : 10
Enter the secound number : 2
--------------- 
Result
 ---------------
Additional operator : 10+2 = 12
Subtraction operator : 10-2 = 8
Multiplication operator : 10*2 = 20
Division operator : 10/2 = 5.0
Floor division operator : 10//2 = 5
Modulo division operator : 10%2 = 0
Exponentiation operator : 10**2 = 100
'''