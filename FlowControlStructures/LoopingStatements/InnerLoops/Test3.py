'''
write a program which will accepts age of the citizen and decide whether the citizen is
eligible to vote or not?
'''
while(True):
    age=int(input("Enter the age in years : "))
    if(age>18):
        print("U R elgible for applying to vote")
    else:
        print("U R not elgible for applying to vote")
