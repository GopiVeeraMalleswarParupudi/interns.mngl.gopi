'''
write a program which will accept a number and find the sum of the digits of the given number.
'''
num=int(input("Enter the number : "))
original=num
if(num>0):
    res=0
    while(num>0):
        res+=(num%10)
        num=num//10
    else:
        print("Sum of digits of given number({}) = {}".format(original,res))