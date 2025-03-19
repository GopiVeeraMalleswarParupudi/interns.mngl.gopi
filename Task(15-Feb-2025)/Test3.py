'''
write a program which will generate RTO number plates
'''
from random import sample as s
number='0123456789'
alphabet='ABCDEFGHIJKLMNOPQRSTUVXYZ'
for i in range(0,50):
    alp=''
    print('AP '+''.join(s(alphabet,2))+' '+''.join(s(number,4)))