def sum(result=0):
    a=int(input("Enter the first number : "))
    b=int(input("Enter the secound number : "))
    result=a+b
    return result

print(sum())

result=10
def sum1():
    print(result)
def sum2():
   result= globals().get('result')
   result+=1
   print(result)
def sum3():
   global result
   result= globals().get('result')
   result+=1
   print(result)
sum1()
sum2()
print(result)
sum3()