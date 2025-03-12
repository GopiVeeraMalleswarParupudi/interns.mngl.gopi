from ATM_Menu import printMenu
from ATM_Exceptions import NonNegativeError,NonZeroError,InvalidChoice
from ATM_Operations import deposit,withDraw,balanceEnquiry,exit
try:    
    balance=float(10000)
    printMenu()
    
    while(True):
        if 0 < (choice :=(int(input('Please enter you choice : ')))) < 5 :
                match(choice):
                    case 1 :
                        balance=deposit(balance,float(input('Enter the deposit amount: ')))
                        printMenu()
                    case 2 :
                        balance=withDraw(balance,float(input('Enter the withdraw amount : ')))
                        printMenu()
                    case 3 :
                        balanceEnquiry(balance)
                        printMenu()
                    case 4:
                        exit()
                        break 
        else:
            raise InvalidChoice
except NonNegativeError:
     print("Please don't enter negative value")
except NonZeroError:
     print("Please don't enter zero value")
except InvalidChoice:
     print("Please enter the valid choice [1,2,3,4]")
finally:
    print('\t***Please Visit Again***')