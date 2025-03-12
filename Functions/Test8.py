def display(a,b,c):
    print("a={},b={}, c={}".format(a,b,c))
display(10,20,30)

def display(a,b):
    print("a={},b={}".format(a,b))
display(10,20)

def display(a):
    print("a={}".format(a))
display(1)

def display(a,b,*c):
    print("a={}, b={}, c={}".format(a,b,c),type(c))

display(10,20,30,40,50,60,70,80,90)

display(7,8,1,2,3,4,5,6)

def display(d,*e,f):
    print("d={}, e={}, f={}".format(d,e,f))

display(1,2,3,4,5,6,f=7)

def stdReport(*marks):
    sno,sname=input("Enter the roll number : "),input("Enter name : ")
    print("*"*50)
    print("Student Report")
    print("*"*50)
    print("Roll number : {}".format(sno))
    print("Name : {}".format(sname))
    print("Marks")
    print("-"*20)
    for i in range(0,len(marks)):
        print(marks[i])
    print("*"*50)
stdReport(10,30,40,30)