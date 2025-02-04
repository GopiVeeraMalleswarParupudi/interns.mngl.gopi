'''
FrozenSet Data Type
-------------------
-> FrozenSet is a predefined class, which is used to store the values randomly.
-> Frozenset will not store the elements based on insertion order but it will store the values based on hashvalue of the values.
-> FrozenSetwill not store duplicate values.
-> We cannot perform indexing and slicing operations on frozenset.
-> FrozenSet is immutable, it will not allow insertions once it is created.
-> FrozenSet is two types.
	1. Empty frozenset:
		-> Empty frozenset can be created by using frozenset() function
			Syntax : fs = frozenset()
			
	2. Non-Empty frozenset:
		-> Non-Empty frozenset can be created by using frozenset(list/tuple/set).
			Syntax : fs = frozenset(list/tuple/set)
-> FrozenSet and set is both are similar in functionally, but the set is both mutable and immutable where as frozenset is immutable.
->Python has provided some predefined functions
	1. isdisjoint()
	2. issuperset()
	3. issubset()
	4. union()
	5. intersection()
	6. difference()
	7. symmetric_difference()
'''
# creating frozenset
fs3=frozenset()
print("Empty frozoneset : ",fs3)
'''
Output:
Empty frozoneset :  frozenset()
'''

s1= set()
s1.add(10)
s1.add("hello world")
s1.add(123.456)
s1.add(True)
fs=frozenset(s1)
print("set : ",s1,"\nfrozenset : ",fs)
'''
Output: 
set :  {True, 10, 123.456, 'hello world'} 
frozenset :  frozenset({True, 10, 123.456, 'hello world'})
'''

fs2=frozenset([60,70,80,90,100])
print("frozenset created by using list : ",fs2)
'''
Output:
frozenset created by using list :  frozenset({50, 20, 40, 10, 30})
'''

fs1=frozenset({10,20,30,40,50})
print("frozenset created by using set : ",fs1)
'''
Output:
frozenset created by using set :  frozenset({50, 20, 40, 10, 30})
'''

#isdisoint examples
fs1=frozenset([10,20,30,40])
fs2=frozenset({30,40,50,60})

if not fs1.isdisjoint(fs2) :
    print("Given two frozensets are joint sets")
else :
    print("Given two frozensets are disjoint sets")
'''
Output: 
Given two frozensets are joint sets
'''

for elements in fs1:
    print(elements,end=" ")
'''
Output:
40 10 20 30 
'''

#issuperset()
fs3=frozenset({10,"hello world",123.456,False})
l1=[20,"thank you",652.231,True]
fs4=frozenset(l1)
s1={"hello world",True}
fs5=frozenset(s1)
fs5={False,"hello world"}
if fs3.issuperset(fs4):
    print("\nfs3 : ",fs3," is superset to fs4 :",fs4)
elif fs3.issuperset(fs5):
    print("\nfs3 : ",fs3," is superset to fs5 :",fs5)
elif fs4.issuperset(fs3):
    print("\nfs4 : ",fs4," is superset to fs3 :",fs3)
elif fs4.issuperset(fs5):
    print("\nfs4 : ",fs4," is superset to fs5 :",fs5)
elif fs5.issuperset(fs3):
    print("\nfs5 : ",fs5," is superset to fs3 :",fs3)
elif fs5.issuperset(fs4):
    print("\nfs5 : ",fs5," is superset to fs4 :",fs4)
'''
Output:
fs3 :  frozenset({False, 10, 123.456, 'hello world'})  is superset to fs5 : {False, 'hello world'}
'''

#issubset()
fs6=frozenset({10,"hello world",123.456,False})
fs7=frozenset({"hello world",True})
fs8=frozenset({False,"hello world"})

if fs6.issubset(fs7):
    print("fs6 : ",fs6," is subset to fs7 :",fs7)
else:
    print("fs6 : ",fs6," is not subset to fs7 :",fs7)
'''
Output:
fs6 :  frozenset({False, 'hello world', 10, 123.456})  is not subset to fs7 : frozenset({'hello world', True})
'''

if fs8.issubset(fs6):
    print("fs8 : ",fs8," is subset to fs6 :",fs6)
else:
    print("fs8 : ",fs8," is not subset to fs6 :",fs6)
'''
Output:
fs8 :  frozenset({False, 'hello world'})  is subset to fs6 : frozenset({False, 'hello world', 10, 123.456})
'''


fs9=frozenset({10,"hello world",123.456,False})
fs10=frozenset({"hello world",True,234.29,23})
#union
fs11=fs9.union(fs10)
print("Union Output","\n------------------------------","\nfs9 : ",fs9,"\nfs10 : ",fs10,"\nfs11 :",fs11)
'''
Union Output 
------------------------------ 
fs9 :  frozenset({False, 10, 123.456, 'hello world'}) 
fs10 :  frozenset({True, 234.29, 'hello world', 23}) 
fs11 : frozenset({False, True, 10, 234.29, 'hello world', 23, 123.456})
'''

#bitwise OR( | )
fs12= fs9 | fs10
print("Bitwise OR( | ) Output","\n------------------------------","\nfs9 : ",fs9,"\nfs10 : ",fs10,"\nfs13 :",fs12)
'''
Bitwise OR( | ) Output 
------------------------------ 
fs9 :  frozenset({False, 10, 123.456, 'hello world'}) 
fs10 :  frozenset({True, 234.29, 'hello world', 23}) 
fs13 : frozenset({False, True, 10, 234.29, 'hello world', 23, 123.456})
'''

#intersection
fs13=fs9.intersection(fs10)
print("Intersection Output","\n------------------------------","\nfs9 : ",fs9,"\nfs10 : ",fs10,"\nfs11 :",fs13)
'''
Intersection Output 
------------------------------ 
fs9 :  frozenset({False, 10, 123.456, 'hello world'}) 
fs10 :  frozenset({True, 234.29, 'hello world', 23}) 
fs11 : frozenset({'hello world'})
'''

#bitwise AND( & )
fs14=fs9 & fs10
print("Bitwise AND( & ) Output","\n------------------------------","\nfs9 : ",fs9,"\nfs10 : ",fs10,"\nfs13 :",fs13)
'''
Bitwise AND( & ) Output 
------------------------------ 
fs9 :  frozenset({False, 10, 123.456, 'hello world'}) 
fs10 :  frozenset({True, 234.29, 'hello world', 23}) 
fs13 : frozenset({'hello world'})
'''

#difference
fs15=fs9-fs10
print("Difference Output","\n------------------------------","\nfs9 : ",fs9,"\nfs10 : ",fs10,"\nfs15 :",fs15)
'''
Difference Output 
------------------------------ 
fs9 :  frozenset({False, 10, 123.456, 'hello world'}) 
fs10 :  frozenset({True, 234.29, 'hello world', 23}) 
fs15 : frozenset({False, 10, 123.456})
'''

fs16=fs10-fs9
print("Difference Output","\n------------------------------","\nfs9 : ",fs9,"\nfs10 : ",fs10,"\nfs16 :",fs16)
'''
Difference Output 
------------------------------ 
fs9 :  frozenset({False, 10, 123.456, 'hello world'}) 
fs10 :  frozenset({True, 234.29, 'hello world', 23}) 
fs16 : frozenset({True, 234.29, 23})
'''

fs17=fs9.difference(fs10)
print("Difference Output","\n------------------------------","\nfs9 : ",fs9,"\nfs10 : ",fs10,"\nfs17 :",fs17)
'''
Difference Output 
------------------------------ 
fs9 :  frozenset({False, 10, 123.456, 'hello world'}) 
fs10 :  frozenset({True, 234.29, 'hello world', 23}) 
fs17 : frozenset({False, 10, 123.456})
'''

fs18=fs10.difference(fs9)
print("Difference Output","\n------------------------------","\nfs9 : ",fs9,"\nfs10 : ",fs10,"\nfs18 :",fs18)
'''
Difference Output 
------------------------------ 
fs9 :  frozenset({False, 10, 123.456, 'hello world'}) 
fs10 :  frozenset({True, 234.29, 'hello world', 23}) 
fs18 : frozenset({True, 234.29, 23})
'''

#symmetric_difference()
fs19=fs9.symmetric_difference(fs10)
print("Symmetric_Difference Output","\n------------------------------","\nfs9 : ",fs9,"\nfs10 : ",fs10,"\nfs19 :",fs19)

#bitwise exclusive OR( ^ )
fs20=fs10^fs9
print("Bitwise Exclusive OR Output","\n------------------------------","\nfs9 : ",fs9,"\nfs10 : ",fs10,"\nfs20 :",fs20)


'''
List Category Data Types:
------------------------
-> 
'''
