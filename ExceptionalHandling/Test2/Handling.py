import Develoment as dev #import NonZeroError,NegativeNumberError
from Raising import printTable
try:
    printTable(a:=int(input('Enter which table you want to print : ')),
                b:=int(input('Enter the range of the table : ')))
except dev.NonZeroError:
    print('Number must not be zero')
except dev.NegativeNumberError:
    print('Number must not be negative')