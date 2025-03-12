'''
write a program which will accepts a numerical integer value and prints both even and odd numbers 
seperatedly.
'''
limit=int(input("Enter the limit : "))
start=1
even=set()
odd=set()
while(start<=limit):
    if(start%2==0):
        even.add(start)
    else:
        odd.add(start)
    start+=1
else:
    print("-"*100,"\nEven Numbers : ",even,"\n","-"*100)
    print("\n\n\n")
    print("-"*100,"\nOdd Numbers : ",odd,"\n","-"*100)
