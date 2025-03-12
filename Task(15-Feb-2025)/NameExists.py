l1=list()
while(True):
    name=input("Enter name : ")
    l2=name.lower().split()
    l2.sort()
    if l2 in l1:
        print("NAME :\t['{}']\t ALREADY EXISTS, PLEASE ENTER ANOTHER NAME".format(name))
        print("-"*60)
    else:
        l1.append(l2)
        print(l1)