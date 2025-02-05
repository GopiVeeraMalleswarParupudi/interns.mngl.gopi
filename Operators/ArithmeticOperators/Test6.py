'''
write a program which will calculates (a+b) to the power n.
'''
firstNumber=int(input("Enter the first number : "))
secoundNumber=int(input("Enter the secound number : "))
power=int(input("Enter the power : "))
print("-"*30,"\nResult\n","-"*30)
print("The result of ({}+{})^{}={}".format(firstNumber,secoundNumber,power,(firstNumber+secoundNumber)**power))
'''
Enter the first number : 2
Enter the secound number : 3
Enter the power : 10
------------------------------ 
Result
 ------------------------------
The result of (2+3)^10=9765625
'''