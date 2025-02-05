amt=float(input("Enter amount : "))
time=float(input("Enter the years : "))
interest=float(input("Enter the interest : "))
simpleInterest = (amt*time*interest)/100
print("="*30,"\nInterest Calculation\n","="*30,"\nAmount : {}".format(amt),"\nInterest : {}".format(interest),"\nTime : {}".format(time),"\nTotal interest : {}".format(simpleInterest),"\nTotal Amount : {}".format(amt+simpleInterest))
