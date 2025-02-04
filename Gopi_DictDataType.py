'''
Dict Data Type
-----------------
-> Dict data type is a predefined class in python, which is used to store the data in the form of key and value pair.
-> The elements(key, value) that is stored inside the dict which may be a same type or different type.
-> Key must be unique where as values may or may not be unique.
-> We cannot perform indexing and slicing operations on dict data type why because dict stores the data in the form of key and value pair.
-> In dict data type keys are immutable where as values are mutable.
-> We can access the values by calling the keys.
-> Dict data type store the elements(key, value) on bases of insertion order.
-> To convert any type of data [list, Tupple, set, frozenset] into dict python has provided one predefinedfunction called dict(key:(list/tupple/set/frozenset)).
-> To create dict we have use curly braces and the elements(key, value) which is enclosed with in the curly braces and the elements are seperated by comma(,).
	Syntax:- d = {emp1:[10,"scott",20000.00,"male"], emp2:[20,"carlo",25000.00,"male"]}
-> To perform operations on dict python has provided some predefined functions. They are
	1. remove(key)
	2. pop(key)
	3. popitem()
	4. get(key)
	5. keys()
	6. values()
	7. items()
	8. copy()
	9. update()

'''
#creating dict
d1={}
print(d1,type(d1),id(d1))
'''
Output:
{} <class 'dict'> 1977611902336
'''

d2=dict()
print(d2,type(d2),id(d2))
'''
Output:
{} <class 'dict'> 2102739926464
'''

l1 = [10,[20,30,40],50]
print(l1,type(l1),id(l1))
'''
Output:
[10, [20, 30, 40], 50] <class 'list'> 1522071651008
'''

d3=dict(list1=l1)
print(d3,type(d3),id(d3))
'''
Output:
{'list1': [10, [20, 30, 40], 50]} <class 'dict'> 1522071960960
'''

s1={10,20,30,40,50}
print(s1,type(s1),id(s1))
'''
Output:
{50, 20, 40, 10, 30} <class 'set'> 3287370407200
'''

d4=dict(set1=s1)
print(d4,type(d4),id(d4))
'''
Output:
{'set1': {50, 20, 40, 10, 30}} <class 'dict'> 1954358164608
'''

#clear()
d1=dict(CR220="GOPI")
print(d1,type(d1),id(d1))
'''
Output:
{'CR220': 'GOPI'} <class 'dict'> 1676724665152
'''

d1={"CR219":"anil","CR220":"gopi","CR221":"rajyalakshmi","CR222":"shanmukh"}
print(d1,type(d1),id(d1))
'''
Output:
{'CR219': 'anil', 'CR220': 'gopi', 'CR221': 'rajyalakshmi', 'CR222': 'shanmukh'} <class 'dict'> 2156256550272
'''

d1.clear()
print(d1,type(d1),id(d1))
'''
Output:
{} <class 'dict'> 2086397336960
'''

#insert
d2={}
d2["cr219"]="anill"
d2['cr220']="gopi"
d2['cr221']='rajyalakshmi'
d2['cr222']="shanmukh"
print(d2,"\n",type(d2),"\n",id(d2))
'''
Output:
{'cr219': 'anill', 'cr220': 'gopi', 'cr221': 'rajyalakshmi', 'cr222': 'shanmukh'} 
 <class 'dict'> 
 2933729246016
'''

#updating
d2['cr220']="Gopi Veera Malleswar"
print(d2,"\n",type(d2),"\n",id(d2))
'''
Output:
{'cr219': 'anill', 'cr220': 'Gopi Veera Malleswar', 'cr221': 'rajyalakshmi', 'cr222': 'shanmukh'} 
 <class 'dict'> 
 2460631153472
'''

d2['cr220']="Gopi"
print(d2,"\n",type(d2),"\n",id(d2))
'''
Output:
{'cr219': 'anill', 'cr220': 'Gopi', 'cr221': 'rajyalakshmi', 'cr222': 'shanmukh'} 
 <class 'dict'> 
 2740769766208
'''

#pop(key)
print("Before pop(key) : ",d2)
d2.pop("cr220")
print("After pop(key) : ",d2)
'''
Before pop(key) :  {'cr219': 'anill', 'cr220': 'Gopi', 'cr221': 'rajyalakshmi', 'cr222': 'shanmukh'}
After pop(key) :  {'cr219': 'anill', 'cr221': 'rajyalakshmi', 'cr222': 'shanmukh'}
'''

print("Before pop(key) : ",d2)
d2.pop("cr219")
print("After pop(key) : ",d2)
'''
Output:
Before pop(key) :  {'cr219': 'anill', 'cr221': 'rajyalakshmi', 'cr222': 'shanmukh'}
After pop(key) :  {'cr221': 'rajyalakshmi', 'cr222': 'shanmukh'}
'''

#popitem()
d3={}
d3["intType"]=12
d3["floatType"]=1.2
d3["boolType"]=True
d3["complexType"]=-2j
print(d3)
'''
Output:
{'intType': 12, 'floatType': 1.2, 'boolType': True, 'complexType': (-0-2j)}
'''

print("Before popitem() : ",d3)
d3.popitem()
print("After popitem() : ",d3)
'''
Output:
Before popitem() :  {'intType': 12, 'floatType': 1.2, 'boolType': True, 'complexType': (-0-2j)}
After popitem() :  {'intType': 12, 'floatType': 1.2, 'boolType': True}
'''

print("Before popitem() : ",d3)
d3.popitem()
print("After popitem() : ",d3)
'''
Output:
Before popitem() :  {'intType': 12, 'floatType': 1.2, 'boolType': True}
After popitem() :  {'intType': 12, 'floatType': 1.2}
'''

print("Before popitem() : ",d3)
d3.popitem()
print("After popitem() : ",d3)
'''
Output:
Before popitem() :  {'intType': 12, 'floatType': 1.2}
After popitem() :  {'intType': 12}
'''

#get()
d4={'cr219': 'anill', 'cr220': 'Gopi', 'cr221': 'rajyalakshmi', 'cr222': 'shanmukh'} 
print(d4.get('cr220'))
'''
Output:
Gopi
'''

print(d4.get('cr219'))
'''
Output:
anill
'''

#key()
d5={'cr219': 'anill', 'cr220': 'Gopi', 'cr221': 'rajyalakshmi', 'cr222': 'shanmukh'} 
print(d5.keys())
'''
Output:
dict_keys(['cr219', 'cr220', 'cr221', 'cr222'])
'''
for key in d5.keys():
    print(key,end="\t")
'''
Output:
cr219	cr220	cr221	cr222	
'''

#values(), items()
print(d5.values())
'''
Output:
dict_values(['anill', 'Gopi', 'rajyalakshmi', 'shanmukh'])
'''

for value in d5.values():
    print(value,end="\t")
'''
Output:
anill	Gopi	rajyalakshmi	shanmukh
'''

#items()
print(d5.items())
'''
Output:
dict_items([('cr219', 'anill'), ('cr220', 'Gopi'), ('cr221', 'rajyalakshmi'), ('cr222', 'shanmukh')])
'''

for key, value in d5.items():
    print("key : ",key,"\tvalue : ",value)
'''
Output:
key :  cr219 	value :  anill
key :  cr220 	value :  Gopi
key :  cr221 	value :  rajyalakshmi
key :  cr222 	value :  shanmukh
'''

#copy()
d6= d5.copy()
print(d6,"\n",type(d6),"\n",id(d6))
'''
Output:
{'cr219': 'anill', 'cr220': 'Gopi', 'cr221': 'rajyalakshmi', 'cr222': 'shanmukh'} 
 <class 'dict'> 
 2444537882560
'''

#update()
d7={'a':'apple','b':'ball','c':'cat','d':'dog'}
d8={'e':'eagle','f':'flower','g':'goat','h':'hat'}
d7.update(d8)
print(d7)
print(d8)
'''
Output:
{'a': 'apple', 'b': 'ball', 'c': 'cat', 'd': 'dog', 'e': 'eagle', 'f': 'flower', 'g': 'goat', 'h': 'hat'}
{'e': 'eagle', 'f': 'flower', 'g': 'goat', 'h': 'hat'}
'''