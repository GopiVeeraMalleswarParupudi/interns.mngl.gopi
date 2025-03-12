'''
write a program which will accepts a line and fint the words whose length is greater than 3 by using 
filter function.
'''
data = input("Enter the data : ")
words=list(filter(lambda word:len(word)>3,data.split()))
less=list(filter(lambda word:len(word)<3,data.split()))
print(words,"\n",less)