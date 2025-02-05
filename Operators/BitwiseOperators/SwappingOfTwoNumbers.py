a=int(input("Enter first number : "))
b=int(input("Enter secound number : "))
print("Before swaping a={}, b={}".format(a,b))
a=a^b
print(a)
b=a^b
print(b)
a=a^b
print(a)
print("After swaping a={}, b={}".format(a,b))