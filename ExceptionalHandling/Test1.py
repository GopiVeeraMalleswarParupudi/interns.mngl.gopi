try:
    a,b=int(input('Enter the first number : ')),int(input('Enter the secound number : '))
    c=a/b
except Exception as e:
    print(e)
else:
    print('Result : {}'.format(c))
finally:
    print('*'*5,'X','*'*5)