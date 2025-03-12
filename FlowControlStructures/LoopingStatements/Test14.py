'''
write a program which will accepts any number and obtain it's reverse.
'''
original=num=int(input("Enter the number : "))

rem=reverse=0
while(num>0):
    rem=num%10
    reverse=reverse*10+rem
    num//=10
else:
    print("Reverse of a given number '{}' is {}".format(original,reverse))
    if(original==reverse):
        print("Given number is a palindrome")
    else:
        print("Given number is noot a palindrome")