def square_list(x):
    l=list()
    for i in x:
        l.append(i**2)
    print(l)
    odd_checker(l)

def odd_checker(x):
    l=list()
    for i in x:
        if(i%2!=0):
            l.append(i)
    print(l)

size=int(input("Enter the size of the list : "))
x=list()
for i in range(0,size):
    x.append(int(input("Enter the value-{} : ".format(i+1))))
else:
    square_list(x)