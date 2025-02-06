'''
write a program which will caluclates the net salary of an employee based on the 
following problem statement. 
Accept employee number, employee name and basic salary.
    if basic salary is >10000/- then give
        da = 20% basicsal
        ta = 15% basicsal
        hra = 12% basicsal
        cca = 2% basicsal
        ma = 2% basicsal
        gpf = 2% basicsal  (deduction)
        lic = 1% basicsal  (deduction)
    if basic salary is <10000/- then give
        da = 25% basicsal
        ta = 20% basicsal
        hra = 16% basicsal
        cca = 3% basicsal
        ma = 2% basicsal
        gpf = 2% basicsal  (deduction)
        lic = 1% basicsal  (deduction)
'''

empNo=input("Enter employee number : ")
empName=input("Enter employee name : ")
empBasicSalary = float(input("Enter the basic salary : "))

da=ta=hra=cca=gpf=lic=ma=benefits=deduction=netSalary=None

if(empBasicSalary>0):
    if(empBasicSalary>10000):
        da=empBasicSalary*(20/100)
        ta=empBasicSalary*(15/100)
        hra=empBasicSalary*(12/100)
        cca=empBasicSalary*(2/100)
        ma=empBasicSalary*(2/100)
        gpf=empBasicSalary*(2/100)
        lic=empBasicSalary*(1/100)

    if(empBasicSalary<=10000):
        da=empBasicSalary*(25/100)
        ta=empBasicSalary*(20/100)
        hra=empBasicSalary*(16/100)
        cca=empBasicSalary*(3/100)
        ma=empBasicSalary*(2/100)
        gpf=empBasicSalary*(2/100)
        lic=empBasicSalary*(1/100)

benefits=da+ta+hra+cca+ma
deduction=gpf+lic
netSalary=empBasicSalary+benefits-deduction

print("-"*40,"\n|","\tEmployee Details\t","|\n","-"*40)
print("DA = {}".format(da))
print("DA = {}".format(ta))
print("HRA = {}".format(hra))
print("CCA = {}".format(cca))
print("MA = {}".format(ma))
print("GPF = {}".format(gpf))
print("LIC = {}".format(lic))
print("-"*60)
print("Benefits : {}".format(benefits))
print("Deductions : {}".format(deduction))
print("Net Salary : {}".format(netSalary))