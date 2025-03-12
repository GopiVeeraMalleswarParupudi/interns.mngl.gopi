n=int(input("Enter the range : "))
l=["{} is even".format(val) if val%2==0 else "{} is odd".format(val) for val in range(1,n+1)]
print(l)