'''
write a program which calcultes the a to power of m.
'''
base=int(input("Enter the base value: "))
power=int(input("Enter the power value: "))
print("-"*20,"\nResult\n","-"*20)
print("The result of {} to the power of {} is {}".format(base,power,base**power))
'''
PS D:\PythonFullStack\CorePython> & "C:/Program Files/Python313/python.exe" d:/PythonFullStack/CorePython/ExponentiationProgram.py
Enter the base value: 10
Enter the power value: 4
-------------------- 
Result
 --------------------
The result of 10 to the power of 4 is 10000
'''