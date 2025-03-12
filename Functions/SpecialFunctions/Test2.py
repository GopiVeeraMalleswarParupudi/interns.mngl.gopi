'''
write a program which will accept the line and split by spaces and show the original words 
and its reverse side by side by using zip()
'''
words=[word for word in input().split()]
reverseWords = list(map(lambda word : word[::-1],words))
z=zip(words,reverseWords)
for original,reverse in z:
    print(original," : ",reverse)