'''
                                    Sequence Catagery Data Types
                                ------------------------------------
-> Sequence Catagery data types are predefined classes in python, which are used to store sequence data.

->In python there are four types of sequence catagery data types.
1. str
2. bytes
3. bytearray
4. range

1. str:
-------
    -> str is used to store sequence characters data, the data may be alphabets, numbers, alpha-numericals 
    and including special symbols.
    -> To find the length of the string we have to use predefined function len(string).
    -> To store the value of string in a variable, for this the data must enclosed with single single/double 
    quotations['data' or "data"] or double single/double quotations[''data'' or "data""] or thripple thripple 
    quotations.
    ->String are two types. They
        1) Single line Strings : To create single line strings we have to create the string using single single
        quotations or double double quotations or thripple thripple quotations.
        2) Multiple line strings : To create multi line strings i.e., more than one line we have to create string
        using thripple thripple quotations.

2.Bytes: 
--------
    ->Bytes is used to store the sequences of bytes which is in binary format i.e., 0's and 1's.
    ->Bytes can store the data with in the range of 0 to 255.
    ->Bytes is immutable, which means once the value is store inside the bytes the value cannot be moddified.
    ->To convert any type of data into bytes data type python has provided one predefined function called bytes(data/variable)

3.Bytearray:
-----------
    ->Both  bytes and bytearray is same which means bytearray is used to store the sequences of bytes which is in binary format
     i.e., 0's and 1's but the main difference between them is bytes is immutable where as bytearray is muttable.
    ->To convert any type of data into bytes data type python has provided one predefined function called bytearray(data/variable)

4. Range:
---------
    ->Range is used to store sequence of integral values. The values may be positive or negative or zero.

-> We can perform two types of opertaions on the sequence Catagery data types.They are
i) Indexing : Indexing is the process of fetching the variable from a given string or bytes or bytearray.
ii)Slicing : Slicing is the process of creating substring from a given string, fecting data from the given 
start index to end index.

'''

#str examples
string1 = '''hello'''
string_1 = """hello"""
_string1 = '''hello
            world'''
print(string1,"\n",string_1,"\n",_string1)
#str indexing example
string = "hello world"
for i in range(len(string)):
    print(string[i])
#str slicing example
string2=string[2:5]
print("Slicing part = ",string2)
#bytes examples
b=[10,20,30,40,50]
#creatring bytes from string
bytes1=string.encode()
#creating bytes from list
bytes2=bytes(b)
print(bytes1)
for i in bytes2: 
    print(i)
#indexing example for bytes
for i in bytes2[2:len(bytes2)-1]:
    print(i)
#creating bytes from list
bytes3=bytearray(b)
bytes3[2]=100
print(bytes3)
for i in bytes3: 
    print(i)
#indexing example for bytes
for i in bytes2[2:len(bytes2)-1]:
    print(i)
#range examples
for i in range(1,10):
    print(i)
for i in range(-1,-10):
    print(i)

for i in range(1,10,2):
    print(i)

for i in range(1,10,-2):
    print(i)

for i in range(10,0): # here it will not give output since end index is zero
    print(i)
for i in range(10,0,-2):
    print(i)