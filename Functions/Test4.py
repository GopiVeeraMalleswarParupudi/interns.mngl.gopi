def sum1(a,b,c):
    print("sum({},{},{} : {})".format(a,b,c,a+b+c))
def sum2(a=0,b=0,c=0):
    print("sum({},{},{}) : {}".format(a,b,c,a+b+c))

#positional parameters
sum1(float(input("Enter a value : ")),float(input("Enter a value : ")),float(input("Enter a value : ")))

#default parameters
sum2()

#keyword parameters
sum1(b=float(input("Enter a value : ")),c=float(input("Enter a value : ")),a=float(input("Enter a value : ")))