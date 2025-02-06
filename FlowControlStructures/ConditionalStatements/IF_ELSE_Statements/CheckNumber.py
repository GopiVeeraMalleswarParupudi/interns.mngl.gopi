num=int(input("Enter a number : "))
if(num>=0):
    if(num==0):
        print("Given number '{}' is zero".format(num))
    else:
        print("Given number '{}' is positive number".format(num))
else:
    print("Given number '{}' is negative number".format(num))