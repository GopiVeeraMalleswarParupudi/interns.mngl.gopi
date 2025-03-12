'''
write a program which will accept list of names and sort in both ascending and descending order 
by using functions.
'''
print("Enter the names and seperated by space : ")
lst=[str(val) for val in input().split()]
for i in range(len(lst)):
    for j in range(len(lst)):
        if(lst[i]>lst[j]):
            lst[i],lst[j]=lst[j],lst[i]
desLst=lst.copy()
for i in range(len(lst)):
    for j in range(i,len(lst)):
        if(lst[i]>lst[j]):
            lst[i],lst[j]=lst[j],lst[i]
ascLst=lst.copy()
print(lst,"\n",ascLst,"\n",desLst)