#Given number is even number or odd number
while(True):
    num=int(input("Enter the number : "))
    if(num>0):
        if(num%2==0):
            print("Given number '{}' is EVEN".format(num))
        else:
            print("Given number is '{}' is ODD".format(num))
    else:
        print("Please enter valid number and number must be greater than zero")

#Fibonacci Series
while(True):
    print("\n")
    limit=int(input("Enter range : "))
    num1,num2=0,1
    for i in range(0,limit):
        print(num1,end=" ")
        temp=num1+num2
        num1=num2
        num2=temp
    print("\n")
    print("-"*70)
