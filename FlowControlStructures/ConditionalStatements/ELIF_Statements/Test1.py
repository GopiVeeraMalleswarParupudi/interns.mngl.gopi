'''
write a program which will accepts three integer values and find the biggest amongt them.
'''
a=int(input("Enter first number : "))
b=int(input("Enter secound number : "))
c=int(input("Enter third number : "))
if a>b and a>c :
    print("{} is the biggest among three numbers {},{},{}".format(a,a,b,c))
elif b>a and b>c :
    print("{} is the biggest among three numbers {},{},{}".format(b,a,b,c))
elif c>a and c>b:
    print("{} is the biggest among three numbers {},{},{}".format(c,a,b,c))
else:
    print("All the three numbers {},{},{} are equal".format(a,a,b,c))