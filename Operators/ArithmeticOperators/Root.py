'''
write a program which will calculates n root of m.
'''
num=int(input("Enter the number : "))
root=int(input("Enter the root : "))
print("-"*30,"\nResult\n","-"*30)
print("The result of {} root of {} = {} ".format(num,root,round(num**(1/root),2)))
'''
Enter the number : 16
Enter the root : 2
------------------------------ 
Result
 ------------------------------
The result of 16 root of 2 = 4.0
'''