'''
Type Casting:
-------------
-> Type casting is a technique which is used to convert from one possible type of value into another possible 
type of value.

-> In python there are three types of type casting conversions.
    1. Base Converstions: Base conversion functions are used to perform type casting from one type of  
    number system into another type of number system.
        1.1 bin()
        1.2 oct()
        1.3 hex()
    2. Fundamental Data Types converstions: Fundamental data type conversion functions are used to perform 
    type casting from one possible type of value into another possible type of value.
        2.1 int()
        2.2 float()
        2.3 bool()
        2.4 complex()
        2.5 str()
    3. Collections Data types conversitions: Collection data type conversion functions are used to perform 
    type casting from one possible type of data type into another possible type of data type.
        3.1 list()
        3.2 tuple()
        3.3 set()
        3.4 frozenset()
        3.5 dict()
'''

        #Fundamental data Types Type casting 

    # 1. int()

#float to int
a=2.822
print(a, type(a))
'''
Output: 2.822 <class 'float'>
'''
b=int(a)
print(b,type(b))
'''
Output: 2 <class 'int'>
'''

a=0.12
print(a,type(a))
'''
Output: 0.12 <class 'float'>
'''
b=int(a)
print(b,type(b))
'''
Output: 0 <class 'int'>
'''

a=1e3
print(a,type(a))
'''
Output:1000.0 <class 'float'>
'''
b=int(a)
print(b,type(b))
'''
Output:1000 <class 'int'>
'''

#bool to int
a=True
print(a,type(a))
'''
Output:True <class 'bool'>
'''
b=int(a)
print(b,type(b))
'''
Output:1 <class 'int'>
'''

a=False
print(a,type(a))
'''
Output:False <class 'bool'>
'''
b=int(a)
print(b,type(b))
'''
Output:0 <class 'int'>
'''

a=True
b=False
c=a+b
print(c,type(c))
'''
Output:1 <class 'int'>
'''

'''
-> Type casting is not possible in Complex to int data type.
'''

#str to int
a="1"
print(a,type(a))
'''
Output:1 <class 'str'>
'''
b=int(a)
print(b,type(b))
'''
Output:1 <class 'int'>
'''

a="scott"
print(a,type(a))
'''
Output:scott <class 'str'>
'''
#b=int(a)
#print(b,type(b))
'''
Output:
Traceback (most recent call last):
  File "d:\PythonFullStack\CorePython\TypeCasting.py", line 119, in <module>
    b=int(a)
ValueError: invalid literal for int() with base 10: 'scott'
'''

a="3o"
print(a,type(a))
'''
Output:3o <class 'str'>
'''
#b=int(a)
#print(b,type(b))
'''
Output:
Traceback (most recent call last):
  File "d:\PythonFullStack\CorePython\TypeCasting.py", line 134, in <module>
    b=int(a)
ValueError: invalid literal for int() with base 10: '3o'
'''

a="1.1"
print(a,type(a))
'''
Output:1.1 <class 'str'>
'''
b=int(float(a))
print(b,type(b))
'''
Output:1 <class 'int'>
'''

    #float
#int to float
a=12328932
print(a,type(a))
'''
Output:12328932 <class 'int'>
'''
b=float(a)
print(b,type(b))
'''
Output:12328932.0 <class 'float'>
'''

#bool to float
a=True
print(a,type(a))
'''
Output:True <class 'bool'>
'''
b=float(a)
print(b,type(b))
'''
Output:1.0 <class 'float'>
'''

a=False
print(a,type(a))
'''
Output:False <class 'bool'>
'''
b=float(a)
print(b,type(b))
'''
Output:0.0 <class 'float'>
'''

# complex to float
a=1+2j
print(a,type(a))
'''
Output:(1+2j) <class 'complex'>
'''
#b=float(a)
#print(b,type(b))
'''
Output:
Traceback (most recent call last):
  File "d:\PythonFullStack\CorePython\TypeCasting.py", line 186, in <module>
    b=float(a)
TypeError: float() argument must be a string or a real number, not 'complex'
'''

#str to float
a="123"
print(a,type(a))
'''
Output:
'''
b=float(a)
print(b,type(b))
'''
Output:123.0 <class 'float'>
'''

a="True"
print(a,type(a))
'''
Output:True <class 'str'>
'''
b=float(bool(a))
print(b,type(b))
'''
Output:1.0 <class 'float'>
'''

    #bool
#int to bool
a=10
print(a,type(a))
'''
Output:10 <class 'int'>
'''
b=bool(a)
print(b,type(b))
'''
Output:True <class 'bool'>
'''

a=-1
print(a,type(a))
'''
Output:-1 <class 'int'>
'''
b=bool(a)
print(b,type(b))
'''
Output:True <class 'bool'>
'''

a=0
print(a,type(a))
'''
Output:0 <class 'int'>
'''
b=bool(a)
print(b,type(b))
'''
Output:False <class 'bool'>
'''

#float to bool
a=12.34
print(a,type(a))
'''
Output:12.34 <class 'float'>
'''
b=bool(a)
print(b,type(b))
'''
Output:True <class 'bool'>
'''

a=0.0
print(a,type(a))
'''
Output:0.0 <class 'float'>
'''
b=bool(a)
print(b,type(b))
'''
Output:False <class 'bool'>
'''

#complex to bool
a=1+2j
print(a,type(a))
'''
Output:(1+2j) <class 'complex'>
'''
b=bool(a)
print(b,type(b))
'''
Output:True <class 'bool'>
'''

#str to bool
a="scott"
print(a,type(a))
'''
Output:scott <class 'str'>
'''
b=bool(a)
print(b,type(b))
'''
Output:True <class 'bool'>
'''

a=""
print(a,type(a))
'''
Output: <class 'str'>
'''
b=bool(a)
print(b,type(b))
'''
Output:False <class 'bool'>
'''

a=" "
print(a,type(a))
'''
Output:  <class 'str'>
'''
b=bool(a)
print(b,type(b))
'''
Output:True <class 'bool'>
'''