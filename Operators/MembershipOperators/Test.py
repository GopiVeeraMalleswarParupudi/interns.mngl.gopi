'''
-> Membership operators are not applicable for fundamental data types.
'''

s1 = "maark tm scribbling pad no.5"
print("." in s1)
print("=" not in s1)
print("5." in s1)

l1=[12,34,[23.34,3422,4,42]]
print(4 in l1[-1][0:0:-1])
