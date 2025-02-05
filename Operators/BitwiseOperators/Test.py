a=int(input("Enter the number : "))
r=int(input("Enter the range : "))
s=0
for i in range(r):
    s=s*10+a
    print(s,end=" ")
print(s)