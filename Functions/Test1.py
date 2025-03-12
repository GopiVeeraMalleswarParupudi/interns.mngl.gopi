'''
write a program which will display list of tuple, list, set, dict values by using functions.
'''
def display(x):
    print(x, type(x))

l=[10,20,30,34]
t=tuple([23,45,34,21])
set=set([234,45,42,3,5])
frozenset = frozenset([23,6,42,1,46,6])
dict={"k1":"v1","k2":"v2","k3":"v3","k4":"v4",}
display(l)
display(t)
display(set)
display(frozenset)
display(dict)