import sys
sys.path.append('D:/PythonFullStack/CorePython/ExceptionalHandling/Test1/ExceptionDevelopment')
import NonZeroError
import NegativeNumberError
def generateTable(a,b):
    if(b<=0):
        if(b==0):
            raise NonZeroError
        if(b<0):
            raise NegativeNumberError
    else:
        for i in range(1,b+1):
            print('{} x {} = {}'.format(a,i,(a*i)))
    