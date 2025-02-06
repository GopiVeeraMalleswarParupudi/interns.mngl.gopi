print("-"*40,"\n\tArea of Different Figures\n","-"*40)
print("1. Circle \n2.Rectangle \n3. Square \n4. Triangle \n5. Exit")
print("-"*40)
choice = int(input("Enter your choice : "))
print("-"*40)
match(choice) :
    case 1 :
        radius=float(input("Enter the radius : "))
        print("The area of the cirlce having radius {} is {}".format(radius,3.14*radius**radius))
    case 2 :
        length=float(input("Enter the length : "))
        width=float(input("Enter the width : "))
        print("The area of the rectangle having length {} and width {} is {}".format(length,width,length*width))
    case 3 :
        length=float(input("Enter the length of the side : "))
        print("The area of the square having length {} of one of it's side is {}".format(length,length*length))
    case 4 :
        base=float(input("Enter the base : "))
        height=float(input("Enter the height : "))
        print("The area the triangle having base {} and height {} is {}".format(base,height,(1/2)*base*height))
    case 5 :
        print("Thanks for using")
        exit()
    case _ :
        print("Please enter valid choice")