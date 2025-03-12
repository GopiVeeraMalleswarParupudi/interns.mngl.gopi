'''
write a program which accepts any integer value and generates the even numbers and 
odd numbers seperatedly
'''
num=int(input("Enter the limit : "))
even=set()
odd=set()
for i in range(1,num+1):
    if i%2==0:
        even.add(i)
    else :
        odd.add(i)
else:
    print("Even numbers : ",even)
    print("Odd numbers : ",odd)