'''
write a program which will accepts two integer values and find the biggest number among them by using 
anonymus function.
'''
biggest = lambda num1,num2 :num1 if num1>num2 else num2

print("Enter two numbers : ")
big=biggest(float(input()),float(input()))
print("Biggest : {}".format(big))