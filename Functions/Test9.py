def studentDetails(sno,sname,*hobies,state="Andhra Pradesh",**marks):
    print("*"*50)
    print("Student Report")
    print("*"*50)
    print("Roll number : {}".format(sno))
    print("Name : {}".format(sname))
    print("State : {}".format(state))
    print()
    print("-"*10)
    print("Hobies :")
    print("-"*10)
    for hobby in range(0,len(hobies)):
        print(hobies[hobby],end=",")
    print()
    print()
    print("-"*10)
    print("Marks : ")
    print("-"*10)
    for subject in marks:
        print("{} : {}".format(subject,marks.get(subject)))
    print("*"*50)

studentDetails(1,"scott","playing","surfing net",state="TS",mpmc=40,cad=30)