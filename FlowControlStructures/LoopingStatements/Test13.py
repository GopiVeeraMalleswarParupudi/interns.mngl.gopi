'''
write a program which will accept the list of values and sort them in ascending order.
'''
l1=list()
size=int(input("Enter the size of the list : "))
for i in range(0,size):
    l1.append(int(input("Enter the value {} : ".format(i+1))))
else:
    #print("Original List : ",l1)
    for j in range(0,size):
        for k in range(j,size):
            if(l1[j]>l1[k]):
                l1[j],l1[k]=l1[k],l1[j]
        print(l1)
        print("="*50)
#print("Sorted list : ",l1)