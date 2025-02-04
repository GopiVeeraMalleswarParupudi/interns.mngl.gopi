'''
                                    Set Category Data Types
                                -------------------------------
->Set category data types are predefined classes in python which are used to store single or multiple 
values where values may be homogeneous values or heterogeneous values or both homogeneous and 
heterogeneous in a single variable.

->Set Category data types can stores unique elements only, which means it will not allow duplicate values 
even if we are trying to insert into set.

->Set data types will not store the elements in their insertion order. Set will store the elements based 
on their hashcode. Hashcode is the unique integral value which is given for the elements.

->To know the address of the object i.e., variable in python, python has provided one predefined function 
called id(). The memory is different for every object.

->The hash value is same if the value stored inside the variables is same.

->Set will print the elements based on their hashcode.

->We cannot perform indexing and slicing on the set data types.

-> In python there are two types. They are
    1. Set
    2. Frozenset
1.Set:
------
->We can create the set in two ways.
    i) By using set() function
    ii) By using curly braces{}.
  i) Creating set by using set() function :
   ----------------------------------------
    -> By using set() function we can create an empty set, which means creating set without elements.
            Syntax: a = set()
  ii) Creating set by using curly braces :
  -----------------------------------------
  -> By using curly braces {} we can create a non-empty set if we are having an elements to store inside 
  inside the set.
            Syntax: a = {10,'hello',20,'world'}

->Set is both mutable and immutable i.e., Mutable in the sense we are able add another elements after 
creating the set by using add() function where as Immutable in the sense we are not able to modify the 
element that is stored already inside the set since we are not able to perform indexing operation on set.

-> Python has provided a number of predefined to work with set data types to perform inserting, comparing 
and deleting operation on elements inside the set. They are
        1. add()
        2. remove()
        3. discard()
        4. pop()
        5. isdisjoint()
        6. issuperset()
        7. issubset()
        8. union()
        9. intersection()
        10. differences()
        11.symmetric_difference()
        12. update()
'''

#   Creating set in python
s1=set()
s2={10,20,30,40,50}
s3={'hello','world',23.2323,True, 12}
print('Empty set : ',s1,'\nHomogeneous set : ',s2,'\nHomogeneous set : ',s3)
'''
Empty set :  set() 
Homogeneous set :  {50, 20, 40, 10, 30} 
Homogeneous set :  {True, 'hello', 23.2323, 'world', 12}
'''


#  Inserting  element into set
'''
1.add():
->add() functions is used to insert the element into set and the element is stored inside the set 
based on their hash value.
->By using add() function we are able to insert exactly one element into set.
'''
s3.add('good morning')
s3.add('welcome to caratred')
print('Updated s3 : ',s3)
'''
Output : Updated s3 :  {True, 'hello', 'good morning', 'welcome to caratred', 23.2323, 'world', 12}
'''

# Deleting element from the set
'''
2.remove():
->remove() function is used to remove the specified element from a given set, if the specified 
element is not present inside the set then it will raise an error called 'keyerror'.
->elements are removed from the set based on the hash vaule of the arbitary element i.e., random element
->By using remove() we are able to get only one element from the set.
->discard() function after removing the element from the set it will not return any thing.
'''
s4=set()
s4.add(10)
print(s4)
s4.add('hello world')
print(s4)
s4.add(1334.237671)
print(s4)
s4.add(True)
print('Ouput : ',s4)
'''
Output :
{'10'}
{'hello world', '10'}
{'hello world', 1334.237671, '10'}
Ouput : {True, 'hello world', 1334.237671, '10'}
'''
print('Hash Values  : ','\nFor 10 : ',hash(10),'\nFor hello world : ',hash('hello world'),'\nFor 1334.237671 : ',hash(1334.237671),'\nFor True : ',hash(True))
'''
Output:
Hash Values  :  
For 10 :  10 
For hello world :  5953919070050221973 
For 1334.237671 :  548032013843039542 
For True :  1
'''
print(s4)
s4.remove(10)
print(s4)
s4.remove(True)
print(s4)
s4.remove(1334.237671)
print(s4)
#print(s4.remove('hello world'))
s4.remove('hello world')
print(s4)
#4.remove('Hello world')
print(s4)
'''
Output :
{True, 10, 'hello world', 1334.237671}
{True, 'hello world', 1334.237671}
{'hello world', 1334.237671}
{'hello world'}
set()
Traceback (most recent call last):
  File 'd:\PythonFullStack\CorePython\SetCategoryDataTypes.py', line 124, in <module>
    s4.remove('Hello world')
    ~~~~~~~~~^^^^^^^^^^^^^^^
KeyError: 'Hello world'
'''

'''
3.discard():
->discard() function is used to remove the specified element from a given set, even if the specified 
element is not present inside the set then it will not raise any error called 'keyerror'.
->elements are removed from the set based on the hash vaule of the arbitary element i.e., random element
->By using discard() we are able to get only one element from the set.
->discard() function after removing the element from the set it will not return any thing.
'''
s4.discard('Hello World')


'''
4.pop():
->pop() function is used to remove the element from the set. pop() function first will display which is to be removed from the
set and then removed the element from set.
'''
s5=set()
s5.add(10)
s5.add('hello world')
s5.add(1224.32423423)
s5.add(False)
print(s5)
s5.pop()
print(s5)
s5.pop()
print(s5)
s5.pop()
print(s5)
s5.pop()
print(s5)
#s5.pop()
'''
Output:
{1224.32423423, False, 10, 'hello world'}
{False, 10, 'hello world'}
{10, 'hello world'}
{'hello world'}
set()
Traceback (most recent call last):
  File 'd:\PythonFullStack\CorePython\SetCategoryDataTypes.py', line 171, in <module>
    s5.pop()
    ~~~~~~^^
KeyError: 'pop from an empty set'
'''

# Comparing sets
'''
5.isdisjoint() : 
-> isdisjoint() function is used to check whether the two given sets are either joint sets or disjoint sets.
->If the elements of a set are present inside the another set then they are treated as joint sets otherwise they are disjoint sets.
->isdisjoint() function retuns boolean values either True or False.
->If isdisjoint() function return true then the two sets are disjoint sets.
->If isdisjoint() function return false then the two sets are joint sets.
'''
s6={10,20,30,40,50}
s7={30,40,50,60,70}
s8={80,90,91,92,93}
print(s6.isdisjoint(s7))
print(s7.isdisjoint(s8))
'''
Output:
False
True
'''


'''
6.issuperset():
-> issuperset() function is used to check whether all the elements of a set is present inside the another set or not.
->If all the elements of a set are present inside the another set then they are treated as super set to that other set otherwise 
they are not super sets.
->issuperset() function retuns boolean values either True or False.
->If issuperset() function return true then they are treated as super set to that other set.
->If issuperset() function return false then they are not treated as super set to that other set.
'''
s9={10,20,30,40,50}
s10={10,50}
s11={'a','b'}
print(s9.issuperset(s10)) #The elements present inside the s10 present in s9.
print(s10.issuperset(s11))
'''
Output:
True
False
'''
#subset examples
print(s10.issubset(s9))
print(s9.issubset(s11))
'''
Output:
True
False
'''

#8) Union()
s1={'RS','JG','DR','Stup'}
s2={'TRAVIS','MCK','RS'}
print(s1)
print(s2)
allcptp=s1.union(s2)
print(allcptp)
'''
Output:
{'RS', 'JG', 'DR', 'Stup'}
{'RS', 'TRAVIS', 'MCK'}
{'RS', 'DR', 'Stup', 'JG', 'TRAVIS','MCK'}
'''


#9)difference()
s1={'RS','JG','DR','Stup'}
s2={'TRAVIS','MCK','RS'}
print(s1)
print(s2)
onlycp=s1-s2
print(onlycp)
onlytp=s2-s1
print(onlytp)
onlycp=s1.difference(s2)
print(onlycp)
onlytp=s2.difference(s1)
print(onlytp)
'''
Output:
{'RS', 'DR', 'Stup', 'JG'}
{'RS', 'TRAVIS', 'MCK'}
{'JG', 'DR', 'Stup'}
{'TRAVIS', 'MCK'}
{'JG', 'DR', 'Stup'}
{'TRAVIS', 'MCK'}
'''


#10) intersection():
s1={'RS','JG','DR','Stup'}
s2={'TRAVIS','MCK','RS'}
s3=s1.intersection(s2)
print(s3)
s3=s2.intersection(s1)
print(s3)
'''
Output:
{'RS'}
{'RS'}
'''

#11) symmetric_difference():
s1={'RS','JG','DR','Stup'}
s2={'TRAVIS','MCK','RS'}
print(s1)
print(s2)
excptp=s1.symmetric_difference(s2)
print(excptp)
'''
Output:
{'RS', 'DR', 'Stup', 'JG'}
{'RS', 'TRAVIS', 'MCK'}
{'DR', 'TRAVIS', 'Stup', 'JG', 'MCK'}
'''

s1={'RS','JG','DR','Stup'}
s2={'TRAVIS','MCK','RS'}
s3=s1.union(s2)
print(s3)
s4=s1|s2 # Bitwise OR
print(s4)
'''
Output:
{'RS', 'DR', 'Stup', 'JG', 'TRAVIS', 'MCK'}
{'RS', 'DR', 'Stup', 'JG', 'TRAVIS', 'MCK'}
'''

s1={'RS','JG','DR','Stup'}
s2={'TRAVIS','MCK','RS'}
s3=s1.intersection(s2)
print(s3)
s4=s1&s2 # Bitwise AND ( & )
print(s4)
'''
Output :
{'RS'}
{'RS'}
'''
s1={'RS','JG','DR','Stup'}
s2={'TRAVIS','MCK','RS'}
s3=s1.symmetric_difference(s2)
print(s3)
s4=s1^s2 # Bitwise XOR (^)
print(s4)
'''
Output:
{'DR', 'TRAVIS', 'Stup', 'JG', 'MCK'}
{'DR', 'TRAVIS', 'Stup', 'JG', 'MCK'}
'''

s1={'RS','JG','DR','Stup'}
s2={'TRAVIS','MCK','RS'}
s3=s1.difference(s2)
print(s3)
s4=s1-s2
print(s4)
'''
Output:
{'JG', 'DR', 'Stup'}
{'JG', 'DR', 'Stup'}
'''

#12) update():
s1={'C','CPP'}
s2={'PYTHON','DS'}
s1.update(s2)
print(s1)
print(s2)
'''
Output:
{'C', 'CPP', 'PYTHON', 'DS'}
{'PYTHON', 'DS'}
'''