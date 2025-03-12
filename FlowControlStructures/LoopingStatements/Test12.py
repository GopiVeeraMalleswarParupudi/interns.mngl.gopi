'''
write a program which will accepts list of values anf find their sum and average.
'''
l1=[1,2,32,41,5,1,46,1324,5,112]
sum=0
for i in l1:
    sum+=i
    average=sum/len(l1)
else:
    print("sum of the list : ",sum)
    print("average of the list of values : ",average)

print("="*50)
sum=0

for i in range(0,len(l1)):
    sum+=l1[i]
    average=sum/len(l1)
else:
    print("sum of the list : ",sum)
    print("average of the list of values : ",average)

print("="*50)
sum=0

l2=list()
size=int(input("Enter the size of the list : "))
for i in range(0,size):
    l2.append(float(input("Enter the value {} : ".format(i+1))))
else:
    for j in range(0,len(l2)):
        sum+=l2[j]
        avg=sum/len(l2)
    else:
        print("sum of the list : ",sum)
        print("average of the list of values : ",avg)