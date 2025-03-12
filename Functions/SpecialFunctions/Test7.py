'''
write a program which will accepts list of words which are seperated by comma and form a sentence
'''
import functools
print('Enter the words seperated by comma : ')
lst=[val for val in input().split(',')]
updatedLine=functools.reduce(lambda val1,val2: val1+' '+val2,lst)
print(updatedLine)