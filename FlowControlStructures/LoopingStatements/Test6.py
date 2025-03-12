'''
write a program which will accepts a string and check whether the given string is palindrome or not.
'''
name=input("Enter a name : ")
reverse=name[::-1]
print(id(name),"\n",id(reverse))
if(name==reverse):
    print("Given string {} is a palindrome".format(name))
else:
    print("Given string {} is not a palindrome".format(name))

s1="uhasdhhu"
s2="uhasdhhu"
print(id(s1),"\n",id(s2))
