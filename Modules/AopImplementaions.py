def operations():
    while(True):
        choice=num if 0<(num:=int(input('Enter your choice : ')))<=8 else print('Please enter valid input[1 to 8]')
        a,b=float(input('Enter num1 : ')),float(input('Enter num2 : '))
        match(choice):
            case 1: print('Addition({},{}) = {}'.format(a,b,(a+b)))
            case 2: print('Subtraction({},{}) = {}'.format(a,b,(a-b)))
            case 3: print('Multiplication({},{}) = {}'.format(a,b,(a*b)))
            case 4: print('Normal Division({},{}) = {}'.format(a,b,(a/b)))
            case 5: print('Floor Division({},{}) = {}'.format(a,b,(a//b)))
            case 6: print('Modulo Division({},{}) = {}'.format(a,b,(a%b)))
            case 7: print('Exponentiation({},{}) = {}'.format(a,b,(a**b)))