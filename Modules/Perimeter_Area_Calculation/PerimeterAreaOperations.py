import Circle,Square,Rectangle,Triangle
from PerimterAreaMenu import displayMenu as menu
def calculations():
    while(True):
        menu()
        if(0<(choice:=int(input('Enter your choice : ')))<=5):
            match(choice):
                case 1:
                    while(True):
                        print('\t\t\t\t'+'-'*40)
                        print('\t\t\t\t1. Area of Cirlce')
                        print('\t\t\t\t2. Perimeter of Circle')
                        print('\t\t\t\t3. Exit')
                        print('\t\t\t\t'+'-'*40)
                        if(0<(innerChoice:=(int(input('\t\t\t\tEnter your choice : '))))<=3):
                            match(innerChoice):
                                case 1: 
                                    Circle.area(float(input('\t\t\t\tEnter the radius of a circle : ')))
                                case 2:
                                    Circle.perimeter(float(input('\t\t\t\tEnter the radius of a circle : ')))
                                case 3: break
                        else:
                            print('Enter enetr valid option [1,2,3]')
                case 2:
                    while(True):
                        print('\t\t\t\t'+'-'*40)
                        print('\t\t\t\t1. Area of Square')
                        print('\t\t\t\t2. Perimeter of Square')
                        print('\t\t\t\t3. Exit')
                        print('\t\t\t\t'+'-'*40)
                        if(0<(innerChoice:=(int(input('\t\t\t\tEnter your choice : '))))<=3):
                            match(innerChoice):
                                case 1: 
                                    Square.area(float(input('\t\t\t\tEnter the length of square : ')))
                                case 2:
                                    Square.perimeter(float(input('\t\t\t\tEnter the length of square : ')))
                                case 3: break
                        else:
                            print('Enter enetr valid option [1,2,3]')
                case 3:
                    while(True):
                        print('\t\t\t\t'+'-'*40)
                        print('\t\t\t\t1. Area of Rectangle')
                        print('\t\t\t\t2. Perimeter of Rectangle')
                        print('\t\t\t\t3. Exit')
                        print('\t\t\t\t'+'-'*40)
                        if(0<(innerChoice:=(int(input('\t\t\t\tEnter your choice : '))))<=3):
                            match(innerChoice):
                                case 1: 
                                    Rectangle.area(float(input('\t\t\t\tEnter the length of rectangle: ')),float(input('\t\t\t\tEnter the width of rectangle: ')))
                                case 2:
                                    Rectangle.perimeter(float(input('\t\t\t\tEnter the length of rectangle: ')),float(input('\t\t\t\tEnter the width of rectangle: ')))
                                case 3: break
                        else:
                            print('Enter enetr valid option [1,2,3]')
                case 4:
                    while(True):
                        print('\t\t\t\t'+'-'*40)
                        print('\t\t\t\t1. Area of Triangle')
                        print('\t\t\t\t2. Perimeter of Triangle')
                        print('\t\t\t\t3. Exit')
                        print('\t\t\t\t'+'-'*40)
                        if(0<(innerChoice:=(int(input('\t\t\t\tEnter your choice : '))))<=3):
                            match(innerChoice):
                                case 1: 
                                    Triangle.area(float(input('\t\t\t\tEnter the base of the triangle : ')),float(input('\t\t\t\tEnter the height of the triangle : ')))
                                case 2:
                                    Triangle.perimeter(float(input('\t\t\t\tEnter the length of side-1 : ')),float(input('\t\t\t\tEnter the length of side-2 : ')),float(input('\t\t\t\tEnter the length of side-3 : ')))
                                case 3: break
                        else:
                            print('Enter enetr valid option [1,2,3]')
                case 5:
                    print('***Thanks for using the application***')
                    break
        else:
            print('Enter the valid option [1,2,3,4,5]')