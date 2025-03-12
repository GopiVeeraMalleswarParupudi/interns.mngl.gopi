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