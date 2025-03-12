def sum(a=0,b=0,c=0):
    return a+b+c

def display(a,c,b=3):
    print("a={}, b={}, c={}".format(a,b,c))

x=int(input("Enter the first number : "))
y=int(input("Enter the secound number : "))
z=int(input("Enter the third number : "))

result=sum(x,y,z)
print("sum = {}".format(result))

result=sum()
print("sum = {}".format(result))

result=sum(10,20)
print("sum = {}".format(result))

result=sum(30)
print("sum = {}".format(result))

result=sum(c=40,a=60,b=50)
print("sum = {}".format(result))

display(1,2,5)

display(c=1,b=2,a=3)

display(1,c=3,b=2)