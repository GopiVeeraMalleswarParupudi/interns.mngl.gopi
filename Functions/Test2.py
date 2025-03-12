'''
write a program which will read list of numerical values and sort nny using functions.
'''
def sortInAscendingOrder(l):
    for i in range(len(l)):
        for j in range(i,len(l)):
            if(l[i]>l[j]):
                print(l[i],"\t:\t",l[j])
                l[i],l[j]=l[j],l[i]
        print(l)

size=int(input("Enter the size of the list : "))
l=[]
for i in range(size):
    l.append(float(input("Enter the value-{} : ".format(i+1))))
print(l)
sortInAscendingOrder(l)

    