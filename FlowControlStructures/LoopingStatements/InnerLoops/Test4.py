'''
write a program which will accept student marks, student name and student marks of the three subjects[c,c++,python]
calculate total marks--> total marks=cm(c marks)+cppm(cpp marks)+pm(python marks)
calculate percentage of marks --> percentagemarks=(totalmarks/300)*100
Given grade= "Distinction" provided student total marks lies with in 300 and 250.
Given grade= "first" provided student total marks lies with in 249 and 200.
Given grade= "secound" provided student total marks lies with in 199 and 150.
Given grade= "third" provided student total marks lies with in 149 and 120.
Given grade= "fail" provided student scored less than 40 in any of the given subjects.
Display the total marks memo of the student
'''
print("-"*30)
print("Welcome to caratred")
print("-"*30)
grade=None
while(True):
    stdNumber=input("Enter the roll number : ")
    stdName=input("Enter the name : ")
    cMarks=int(input("Enter the marks of C language : "))
    cppMarks=int(input("Enter the marks of CPP language : "))
    pythonMarks=int(input("Enter the marks of python language : "))
    totalMarks=cMarks+cppMarks+pythonMarks
    percentage=(totalMarks/300)*100
    if (cMarks<=0 or cMarks>100) or (cppMarks<=0 or cppMarks>100) or (pythonMarks<=0 or pythonMarks>100):
        print("Please enter the valid marks marks must be[0 and 100]")
        continue
    elif(cMarks<=40 or cppMarks<=40 or pythonMarks<=40):
        grade="FAIL"
    elif cMarks+cppMarks+pythonMarks>=250:
        grade="DISTINCTION"
    elif cMarks+cppMarks+pythonMarks>=200:
        grade="FIRST"
    elif cMarks+cppMarks+pythonMarks>=150:
        grade="SECOUND"
    elif cMarks+cppMarks+pythonMarks>=120:
        grade="THIRD"

    print("="*50)
    print("-"*30)
    print("\t RESULT \t")
    print("-"*30)
    print("Roll Number : {}".format(stdNumber))
    print("Name: {}".format(stdName))
    print("Marks in C Language : {}".format(cMarks))
    print("Marks in CPP Language : {}".format(cppMarks))
    print("Marks in PYTHON Language : {}".format(pythonMarks))
    print("Total Marks : {}".format(totalMarks))
    print("Percentage : {}".format(percentage))
    print("-"*30)
    print("\t Grade : '{}'".format(grade.upper()))
    print("-"*30)
    break