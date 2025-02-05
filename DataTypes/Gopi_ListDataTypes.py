'''
					List Category Data Types:
					-------------------------
->The purpose of list category data type is used to store the values of same type or different or both types in single object.
-> List can store both unique and duplicate elements.
-> In list category we have two types, they are:
	1. Lis(Mutable)
	2. Tuple(Immutable)
1.List:
--------
-> List is treated as predefined class and treated as List Category Data Types.
-> We can perform indexing and slicing operations on list.
-> List is mutable, we perform insert, updation, searching and deletion operation on list by using predefined functions provided by python.
-> To work with list python has provided predefined functions like
	1. append(value)
	2. insert(position, value)
	3. remove(value)
	4. pop(index)
	5. pop()
	6. count(value)
	7. index(value)
	8. copy()
	9. reverse()
	10. sort()
	11. extend()
->To convert other data types into list python has provided one predefined function called list().
->List stores the elements based on their insertion order.
'''

#creating list.
l1=[] #empty list
str="hello world"
l2=list(str)
print(l2)
l2=list("welcome")
print(l2)
'''
Output:
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
['w', 'e', 'l', 'c', 'o', 'm', 'e']
'''

#append()
l3=[]
l3.append(10)
l3.append("hello world")
l3.append(123.456)
l3.append(True)
l3.append(1+3j)
print("Output : ","\n-------------------------","\n",l3)
'''
Output :  
------------------------- 
 [10, 'hello world', 123.456, True, (1+3j)]
'''
l4=[20,30,40,50]
l4.append(l3)
print("Output : ","\n-------------------------","\n",l4)
'''
Output :  
------------------------- 
 [20, 30, 40, 50, [10, 'hello world', 123.456, True, (1+3j)]]

'''

#indexing
print(l4[0])
print(l4[4])
print(l4[4][4])
'''
Output:
20
[10, 'hello world', 123.456, True, (1+3j)]
(1+3j)
'''

#updating the values
l4[4][1]="welcome"
print(l4)
'''
Output:
[20, 30, 40, 50, [10, 'welcome', 123.456, True, (1+3j)]]
'''

#insert
l4.insert(0,[12,"hello world",6213.123,False])
print(l4)
'''
Output:
[[12, 'hello world', 6213.123, False], 20, 30, 40, 50, [10, 'welcome', 123.456, True, (1+3j)]]
'''
l4.insert(0,["python","java","cpp",".net"])
print(l4)
'''
Output:
[['python', 'java', 'cpp', '.net'], [12, 'hello world', 6213.123, False], 20, 30, 40, 50, [10, 'welcome', 123.456, True, (1+3j)]]
'''

#remove()
l4[1].remove(False)
print(l4)
'''
Output:
[['python', 'java', 'cpp', '.net'], [12, 'hello world', 6213.123], 20, 30, 40, 50, [10, 'welcome', 123.456, True, (1+3j)]]
'''
l4[0].remove("java")
print(l4)
'''
Output:
[['python', 'cpp', '.net'], [12, 'hello world', 6213.123], 20, 30, 40, 50, [10, 'welcome', 123.456, True, (1+3j)]]
'''

l4.remove(['python', 'cpp', '.net'])
print(l4)
'''
Output:
[[12, 'hello world', 6213.123], 20, 30, 40, 50, [10, 'welcome', 123.456, True, (1+3j)]]
'''
l4.remove(50)
print(l4)
'''
Output:
[[12, 'hello world', 6213.123], 20, 30, 40, [10, 'welcome', 123.456, True, (1+3j)]]
'''

#pop(index)
l4[0].pop(0)
print(l4)
'''
Output:
[['hello world', 6213.123], 20, 30, 40, [10, 'welcome', 123.456, True, (1+3j)]]
'''

l4[-1].pop(-1)
print(l4)
'''
Output:
[['hello world', 6213.123], 20, 30, 40, [10, 'welcome', 123.456, True]]
'''

l4.pop(1)
print(l4)
'''
Output:
[['hello world', 6213.123], 30, 40, [10, 'welcome', 123.456, True]]
'''

#pop()
l4[0].pop()
print(l4)
'''
Output:
[['hello world'], 30, 40, [10, 'welcome', 123.456, True]]
'''

l4.pop()
print(l4)
'''
Output:
[['hello world'], 30, 40]
'''

#count()
l5=[10,20,23,12,87,20,10,23,10,23,10]
print(l5.count(10))
'''
Output:
4
'''

s1=set(l5)
for element in s1:
    print("l[",element,"] count : ",l5.count(element))
'''
Output:
l[ 10 ] count :  4
l[ 12 ] count :  1
l[ 20 ] count :  2
l[ 23 ] count :  3
l[ 87 ] count :  1
'''

#index()
l4=[['python', 'java', 'cpp', '.net'], [12, 'hello world', 6213.123, False], 20, 30, 40, 50, [10, 'welcome', 123.456, True, (1+3j)]]
print("index : ",l4[0].index('java'))
'''
Output:
index : 1
'''
print("index : ",l4.index(['python', 'java', 'cpp', '.net']))
'''
Output:
index :  0
'''

#copy
l6=[10,20,30,40]
l7=[50,60,70,80]
l8=l7.copy()
print(l8)
'''
Output:
[50, 60, 70, 80]
'''

l8[0]=l6.copy()
print(l8)
'''
Output:
[[10, 20, 30, 40], 60, 70, 80]
'''

#clear
print(l6,"\n",l7,"\n",l8)
print(l6.clear(),"\n",l7.clear(),"\n",l8.clear())
'''
Output:
[10, 20, 30, 40] 
 [50, 60, 70, 80] 
 [[10, 20, 30, 40], 60, 70, 80]
None 
 None 
 None
'''

#reverse()
l6=[10,20,30,40]
l7=[50,60,70,80]
l6[0]=l7.copy()
l8=l6.copy()
print("Actualy order : ",l6)

print("Reverse Order : ",l6.reverse())
print(l6)
'''
Output:
Actualy order :  [[50, 60, 70, 80], 20, 30, 40]
Reverse Order :  None
[40, 30, 20, [50, 60, 70, 80]]
'''
l6[-1].reverse()
print(l6)
'''
Output:
[40, 30, 20, [80, 70, 60, 50]]
'''

#sort
l6=[40,20,30,10]
l7=[50,70,60,80]
l8=[40, 30, 20, [80, 70, 60, 50]]

print("Actualy order : ",l6)
l6.sort()
print("Reverse Order : ",l6)
'''
Output:
Actualy order :  [40, 20, 30, 10]
Reverse Order :  [10, 20, 30, 40]
'''

print("Actualy order : ",l7)
l7.sort()
print("Reverse Order : ",l7)
'''
Output:
Actualy order :  [50, 70, 60, 80]
Reverse Order :  [50, 60, 70, 80]
'''

print("Actualy order : ",l8)
#l8.sort()
print("Reverse Order : ",l8)
'''
Output:
Actualy order :  [40, 30, 20, [80, 70, 60, 50]]
Traceback (most recent call last):
  File "d:\PythonFullStack\CorePython\ListDataTypes.py", line 270, in <module>
    l8.sort()
    ~~~~~~~^^
TypeError: '<' not supported between instances of 'list' and 'int'
'''

l8[-1].sort()
print(l8)
'''
Output:
[40, 30, 20, [50, 60, 70, 80]]
'''

#extend
l6=[40,20,30,10]
l7=[50,70,60,80]
l8=[40, 30, 20, [80, 70, 60, 50]]
print("l6 : ",l6)
l6.extend(l7)
print("l6 : ",l6,"\nl7 : ",l7)
'''
Output:
l6 :  [40, 20, 30, 10]
l6 :  [40, 20, 30, 10, 50, 70, 60, 80] 
l7 :  [50, 70, 60, 80]
'''

print("Before extend : ",l8)
l8[-1].extend(l8)
print("After extend : ",l8)
'''
Output:
Before extend :  [40, 30, 20, [80, 70, 60, 50]]
After extend :  [40, 30, 20, [80, 70, 60, 50, 40, 30, 20, [...]]]
'''

l9=l6+l7+l8
print(l9)