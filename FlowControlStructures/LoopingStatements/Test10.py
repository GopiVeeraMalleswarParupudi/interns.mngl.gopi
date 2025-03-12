'''
print even and odd numbers from the given range.
'''
limit=int(input("Enter the limit : "))
s1=set()
for i in range(2,limit+1,2):
    s1.add(i)
s2=set()
for i in range(1,limit+1,2):
    s2.add(i)
print("Even numbers : ",s1)
print("Odd numbers : ",s2)