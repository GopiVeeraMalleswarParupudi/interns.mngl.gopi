limit=int(input("Enter the limit : "))
for i in range(limit,0,-1):
    for j in range(i,0,-1): 
        if(i==j or i==limit or j==1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()