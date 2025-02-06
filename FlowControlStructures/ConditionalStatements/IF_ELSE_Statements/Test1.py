'''
write a program which accepts a mobile number and verify the given number contains 
10 digits or not.
'''
num=input("Enter the number : ")
if(len(num)==10): 
    print("Given number contains exactly 10 digits")
else:
    print("Given number does not contains exactly 10 digits")