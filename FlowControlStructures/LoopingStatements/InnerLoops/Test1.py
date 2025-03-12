'''
write a program which will accept list of numerical values and display the multiplication table for 
every value of list
'''
size=int(input("Enter the size of the list : "))
list1=list()
for i in range(size):
    list1.append(float(input("Enter the value {} : ".format(i+1))))
else:
    for i in range(size):        
        for j in range(int(input("Enter the limit : "))):
            print("{} x {} = {}".format(list1[i],j,list1[i]*j))
        print("="*10,"X","="*10)
