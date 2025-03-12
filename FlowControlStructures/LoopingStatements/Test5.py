'''
write a program which will accept a string and print it's reverse order of a string.
'''
s1=input("Enter a name : ")
s2=str()
for i in s1[::-1] :
    print(i)
    s2+=i
else:
    print(s2)