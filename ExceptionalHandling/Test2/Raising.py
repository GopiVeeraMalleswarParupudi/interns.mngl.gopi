from Develoment import NonZeroError,NegativeNumberError
def printTable(a,b):
    if(a==0 or b==0):
        raise NonZeroError
    elif(a<0 or b<0):
        raise NegativeNumberError
    elif(a>0 and b>0):
        for i in range(1,b+1):
            print('{} x {} = {}'.format(a,i,a*i))