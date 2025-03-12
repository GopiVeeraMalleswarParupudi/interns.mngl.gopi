'''
write a program which generates the numners from 1 to n where n is positive number
'''

num=int(input("Enter the number : "))
incr=1
l=list()
if(num>0):
    while(incr<=num):
        l.append(incr)
        incr+=1
    else:
        print(l)