l=[10,20,30,40,[50,60,70,80]]
l[-1].append(l)
print(l)

print(l.reverse())
print(l)

l6 = [40,20,30,10]
l7 = [50,60,70,80]
l8 = [40,20,30,10,[50,60,70,80]]
 
l8[-1].append(l7)
print(l8)
