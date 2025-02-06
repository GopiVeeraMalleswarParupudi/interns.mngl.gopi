'''
write a program which will accepts an alphabet from keyboard and decide whether it is 
an owel or consonent.
'''
s1={'a','e','i','o','u','A','E','I','O','U'}
s2=set()
for i in range(65,91):
    s2.add(chr(i))
for i in range(97,123):
    s2.add(chr(i))
s3=s2.symmetric_difference(s1)
print(s3)
alphabet= input("Enter the alphabet : ")
if(alphabet in s1):
    print("Given alphabet '{}' is owel".format(alphabet))
else:
    if(alphabet in s3):
        print("Given alphabet '{}' is consonent".format(alphabet))
    else:
        print("Please enter an alphabet. Alphabet must be in between [(a-z), (A-Z)]")