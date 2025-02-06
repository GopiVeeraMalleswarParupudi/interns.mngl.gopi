'''
write a program which will accepts three integer values and find the smallest amongt them.
'''
a=int(input("Enter first number : "))
b=int(input("Enter secound number : "))
c=int(input("Enter third number : "))

if(a<b) and (a<c):
    print("smallest({},{},{}) : {}".format(a,b,c,a))
elif b<a and b<c :
    print("smallest({},{},{}) : {}".format(a,b,c,b))
elif c<a and c<b :
    print("smallest({},{},{}) : {}".format(a,b,c,c))
else:
    print("Given three numbers {},{},{} are equal".format(a,b,c))