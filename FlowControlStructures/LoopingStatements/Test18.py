'''
write a program which accepts a line of textvand displays the vowels
'''
l1=['a','e','i','o','u']
s=(input("Enter the text : ")).lower()
for i in s :
    if i in l1:
        print("vowles present in the given text : ")