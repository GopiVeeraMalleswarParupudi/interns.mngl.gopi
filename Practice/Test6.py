s=input("Enter name : ")
rev=""
for i in range(len(s)-1,-1,-1):
    rev+=s[i]
print("Original : {}".format(s),"\tReverse : {}".format(rev))
