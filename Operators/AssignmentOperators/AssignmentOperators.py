a=int(input("Enter the number : "))
print("-"*30,"\nAssignment Operators\n","-"*30)
b=a
a+=a
print("{}+={}-->{}".format(b,b,a))
a-=b
print("{}-={}-->{}".format(a+b,b,a))
a/=2
print("{}/={}-->{}".format((a*2),2,a))
a//=2
print("{}//={}-->{}".format(a*2,2,a))
a%=a
print("{}".format(a))
a=2
a**=a
print("{}".format(a))
