"""limit=int(input("Enter the limit : "))
for i in range(0,limit):
    for j in range(0,i+1):
        if(i==j or j==0 or i==limit-1):    
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()"""
limit=int(input("Enter the limit : "))
for i in range(0,limit):
    for j in range(0,i+1):   
        print("*",end=" ")
    print()