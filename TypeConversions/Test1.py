Python 3.13.1 (tags/v3.13.1:0671451, Dec  3 2024, 19:06:28) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=10
>>> a=12.34
>>> print(a,type(a))
12.34 <class 'float'>
>>> b=int(a)
>>> print(b,type(b))
12 <class 'int'>
>>> a=true
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> a=True
>>> print(a,type(a))
True <class 'bool'>
>>> b=int(a)
>>> print(b,type(b))
1 <class 'int'>
>>> a=False
>>> print(a,type(a))
False <class 'bool'>
>>> b=int(a)
>>> print(b,type(b))
0 <class 'int'>
>>> a=1+2j
>>> print(a,type(a))
(1+2j) <class 'complex'>
>>> b=int(a)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    b=int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> a='123'
>>> print(a,type(a))
123 <class 'str'>
>>> b=int(a)
>>> print(b,type(b))
123 <class 'int'>
>>> a='12.34'
>>> print(a,type(a))
12.34 <class 'str'>
>>> b=int(a)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    b=int(a)
ValueError: invalid literal for int() with base 10: '12.34'
>>> a='True'
>>> print(a,type(a))
True <class 'str'>
>>> b=int(a)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    b=int(a)
ValueError: invalid literal for int() with base 10: 'True'
a='1+2j'
print(a,type(a))
1+2j <class 'str'>
b=int(a)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    b=int(a)
ValueError: invalid literal for int() with base 10: '1+2j'
a='hello'
print(a,type(a))
hello <class 'str'>
b=int(a)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    b=int(a)
ValueError: invalid literal for int() with base 10: 'hello'
a=1
print(a,type(a))
1 <class 'int'>
b=float(a)
print(b,type(b))
1.0 <class 'float'>
a=True
print(a,type(a))
True <class 'bool'>
b=int(a)
print(b,type(b))
1 <class 'int'>
b=float(a)
print(b,type(b))
1.0 <class 'float'>
a=1+2j
print(a,type(a))
(1+2j) <class 'complex'>
b=float(a)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    b=float(a)
TypeError: float() argument must be a string or a real number, not 'complex'
a='123'
print(a,type(a))
123 <class 'str'>
b=float(a)
print(b,type(b))
123.0 <class 'float'>
a='1.23'
print(a,type(a))
1.23 <class 'str'>
b=float(a)
print(b,type(b))
1.23 <class 'float'>
a='True'
print(a,type(a))
True <class 'str'>
b=float(a)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    b=float(a)
ValueError: could not convert string to float: 'True'
a='1-2j)
SyntaxError: unterminated string literal (detected at line 1)
a=1-2j
print(a,type(a))
(1-2j) <class 'complex'>
b=float(a)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    b=float(a)
TypeError: float() argument must be a string or a real number, not 'complex'
a='hello'
print(a,type(a))
hello <class 'str'>
b=float(a)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    b=float(a)
ValueError: could not convert string to float: 'hello'
a=0.0
print(a,type(a))
0.0 <class 'float'>
b=bool(a)
print(b,type(b))
False <class 'bool'>
a=1.0000
print(a,type(a))
1.0 <class 'float'>
b=bool(0.0000001)
print(abtype(b))
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    print(abtype(b))
NameError: name 'abtype' is not defined. Did you mean: 'type'?
print(b,type(b))
True <class 'bool'>
a=''
print(a,type(a))
 <class 'str'>
b=bool(a)
print(b,type(b))
False <class 'bool'>
a=123
print(a,type(a))
123 <class 'int'>
b=complex(a)
print(b,type(b))
(123+0j) <class 'complex'>
a=12.34
print(a,type(a))
12.34 <class 'float'>
b=complex(a)
print(b,type(b))
(12.34+0j) <class 'complex'>
a=0.0
print(a,type(a))
0.0 <class 'float'>
b=complex(a)
print(b,type(b))
0j <class 'complex'>
a='223'
print(a,type(a))
223 <class 'str'>
b=complex(a)
print(b,type(b))
(223+0j) <class 'complex'>
a='223.222'
print(a,type(a))
223.222 <class 'str'>
b=complex(a)
print(b,type(b))
(223.222+0j) <class 'complex'>
a=22-22i
SyntaxError: invalid decimal literal
a=22-22j
a='True'
print(a,type(a))
True <class 'str'>
b=complex(a)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    b=complex(a)
ValueError: complex() arg is a malformed string

a='11-22j'
print(a,type(a))
11-22j <class 'str'>
b=complex(a)
print(b,type(b))
(11-22j) <class 'complex'>
a='hello'
print(a,type(a))
hello <class 'str'>
b=complex(a)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    b=complex(a)
ValueError: complex() arg is a malformed string
a='j'
print(a,type(a))
j <class 'str'>
b=complex(a)
print(b,type(b))
1j <class 'complex'>
a='J'
print(a,type(a))
J <class 'str'>
b=complex(a)
print(b,type(b))
1j <class 'complex'>
