def sum(x,y,z,m):
    print("a={}, b={} c={} d={}".format(x,y,z,m))
    return x+y+z+m

a,b,c,d=int(input("Enter the first number : ")),int(input("Enter a secound number : ")),int(input("Enter a third number : ")),int(input("Enter a fourth number : "))
sum(a,b,d,m=c)