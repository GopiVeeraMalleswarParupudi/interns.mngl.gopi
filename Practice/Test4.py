size=int(input("Enter the size : "))
l=list()
for i in range(0,size):
    l.append(int(input("Enter the value-{} : ".format(i+1))))
else:
    weirdSum=0
    for i in l:
        count=0
        for j in range(0,len(l)):
            if(l[j]==i):
                count+=1
        if(count>2):
            weirdSum+=i
    print("WeirdSum = {} ".format(weirdSum))

