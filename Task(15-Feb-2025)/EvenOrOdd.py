while(True):
    num=int(input("Enter the number : "))
    if(num>0):
        if(num%2==0):
            print("Given number '{}' is EVEN".format(num))
        else:
            print("Given number is '{}' is ODD".format(num))
    else:
        print("Please enter valid number and number must be greater than zero")