'''
write a program which takes integral numerical value as input and print whether the number is prime 
number or not
'''
num=int(input("Enter a number : "))
b=False
for i in range(2,num):
    if(num%i==0):
        b=True
        print("Given number is not a prime number")
        break
if(not b):
    print("Given number is a prime number")
