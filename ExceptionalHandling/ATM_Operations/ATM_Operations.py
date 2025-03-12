from ATM_Exceptions import NonZeroError,NonNegativeError
def deposit(balance,depositAmount):
    currentBalance=0.0
    if(deposit==0):
        raise NonZeroError
    elif(balance<0 or depositAmount<0):
        raise NonNegativeError
    elif(balance>=0 and depositAmount>0 ):
        currentBalance=balance+depositAmount
    print('Your current balance is {}'.format(currentBalance))
    return currentBalance


def withDraw(balance,withdrawAmount):
    currentBalance=0.0
    if(balance==0 or balance<withdrawAmount):
        print("You don't have sufficient Balance to you withdraw")
    elif(withdrawAmount==0):
        raise NonZeroError
    elif(withdrawAmount<0):
        raise NonNegativeError
    elif(balance>=withdrawAmount):
        currentBalance=balance-withdrawAmount
        return currentBalance


def balanceEnquiry(balance):
    print('Your account current balance is {}'.format(balance))


def exit():
    print('***Thanks for using the application***')