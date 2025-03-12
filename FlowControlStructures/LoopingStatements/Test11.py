'''
write a program which accepts integral value and print the sum of first integral values and the sum 
of squares of first n integral values and the sum of cubes of first n integral values
'''
limit=int(input("Enter the limit : "))
naturalSum=0
squaresSum=0
cubesSum=0
for i in range(1,limit+1):
    naturalSum+=i
    squaresSum+=i**2
    cubesSum+=i**3
else:
    print("Sum of first {} natural numbers is : {}".format(limit,naturalSum) )
    print("Sum of squares of first {} natural numbers is : {}".format(limit,squaresSum) )
    print("Sum of cubes of first {} natural numbers is : {}".format(limit,cubesSum) )