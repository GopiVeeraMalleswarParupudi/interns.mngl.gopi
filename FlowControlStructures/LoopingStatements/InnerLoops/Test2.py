'''
write a program which will accept list of numerical values and display the multiplication table for 
every value of list
'''
list1=list()
size = int(input("Enter the size of the list : "))
for i in range(size):
    list1.append(int(input("Enter the value-{} : ".format(i+1))))
else:
    for i in range(size):
        b=True
        for j in range(2,list1[i]):
            if(list1[i]%j==0):
                b=False
                break
        if(b):
            print(list1[i])
                
    
