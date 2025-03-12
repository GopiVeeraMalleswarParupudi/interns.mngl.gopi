'''
write a program which will accepts list of employees whose salary are ranges from 0 to 1000.
Give 10% hike to those employees whose salary ranges from 0 to 500.
Give 20% hike to those employees whose salary ranges from 501 to 1000.
Find the total salary of those employees whose salries are ranges from 0 to 500.
Find the total salary of those employees whose salries are ranges from 501 to 1000.
Find the total salary for all the employees
'''
import functools
empDetails={
            input('Enter the employee name : '):float(input('Enter the salary : '))
            for _ in range(int(input('Enter the number of employees details you want to register : ')))
            }
print(empDetails)
tier1EmpDetails= {name:salary+salary*10/100 for name,salary in empDetails.items() if 0<=salary<=500}
tier2EmpDetails={name:salary+salary*20/100 for name,salary in empDetails.items() if 501<=salary<=1000}
print(tier1EmpDetails,'\n',tier2EmpDetails)
totalSalary1 = functools.reduce(lambda sal1,sal2:sal1+sal2,tier1EmpDetails.values())
totalSalary2 = functools.reduce(lambda sal1,sal2:sal1+sal2,tier2EmpDetails.values())
print(totalSalary1,',',totalSalary2)