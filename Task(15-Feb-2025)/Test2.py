'''
Given a range[m,n] (both inclusive) where 0<=m,n<=10000, find the sum of all integers between m and n.
Example:
Input : 0 3
Output : 6
Explanation : 0+1+2+3=6
'''

def calSum(m, n):
    total = 0  # Using a different variable name
    for i in range(m, n):
        total += i
    print('Sum : {}'.format(total))

calSum(start if 0<=(start:=int(input())) else print('start number must be greater than zero'),
       end if (end:=int(input()))<=10000 else print('end number must be less than 10000'))