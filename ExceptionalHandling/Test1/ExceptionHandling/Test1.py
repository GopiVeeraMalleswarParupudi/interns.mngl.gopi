import sys
sys.path.append('D:/PythonFullStack/CorePython/ExceptionalHandling/Test1/ExceptionDevelopment')
sys.path.append('D:/PythonFullStack/CorePython/ExceptionalHandling/Test1/ExceptionRaising')
import NonZeroError
import NegativeNumberError
from GeneratingMulTable import generateTable as table
try:
    table(a:=int(input('Enter which number table you want to generate : ')),
          b:=int(input('Enter range of the table you want to generate : ')))
except NegativeNumberError:
    print('Range must not be negative')
except NonZeroError:
    print('Range must not be zero')
