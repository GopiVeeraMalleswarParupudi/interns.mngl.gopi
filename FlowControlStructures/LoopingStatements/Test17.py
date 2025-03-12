'''
write a program find the sum of positive numbers and b=negative numbers seperatedly.
'''
size=int(input("Enter the size of the list : "))
l1=list()
positive=negative=0
for i in range(size):
    l1.append(float(input("Enter the value {} :".format(i))))
else:
    for i in range(size):
        if(l1[i]>0):
            positive+=l1[i]
        else:
            negative+=l1[i]
print("Sum of positive numbers of given list = {}".format(positive))
print("Sum of negative numbers of given list = {}".format(negative))