'''
write a program which will generate multiple table by using modules
'''
def generateTable(s):
    print(s)
    number=int(input("Enter which table you want to generate : "))
    r=int(input('Enter the range : '))
    for i in  range(1,r+1):
        print('{} X {} = {}'.format(number,i,number*i))


def checkPrimeOrNot(number):
    status = True
    for i in range(2,number):
        if number%i==0:
            status=False
            break
    print('Given number is prime number') if(status) else print('Given number is not a prime number')
