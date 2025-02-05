#dict data type
d1=dict()
d1['cr219']='anil'
d1['cr220']='gopi'
d1['cr221']='rajyalakshmi'
d1['cr222']='shanmukh'
d2=d1
print(id(d1),"\n",id(d2))
print(d1 is d2)
print(d1 is not d2)
d2=d1.copy()
print(id(d1),"\n",id(d2))
print(d1 is d2)
print(d1 is not d2)

#set data type
s1=set()
s1.add(1)
s1.add("scott")
s1.add(23.15)
s1.add(True)
s1.add(2+3j)
s2=s1.copy()
print(s1 is s2)
print(s1 is not s2)

#frozenset
fs1=frozenset(s1)
fs2=frozenset(s2)

print(fs1 is fs2)
print(fs1 is not fs2)

#str
name1 = "scott"
name2 = "scott"
print(id(name1),"\t",id(name2))
print(name1 is name2,"\n",name1 is not name2)

#int
i1=255
i2=255

print(id(i1),"\t",id(i2))
print(i1 is i2, i1 is not i2)

i3=257
i4=257

print(id(i3),"\t",id(i4))
print(i3 is i4, i3 is not i4)

