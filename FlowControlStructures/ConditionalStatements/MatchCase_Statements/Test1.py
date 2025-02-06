'''
write a program which will implement the follwoing menu driven application
                -------------------------------------
                    Arithmetic Operations
                -----------------------------------
                1. Addition
                2. Subtraction
                3. Multiplication
                4. Division
                5. Floor Division
                6. Modulus
                7. Exponentiation
                8. Exit
                ----------------------------------------
                Enter your choice :
                ------------------------------------------
'''
import sys
print("-"*50,"\n\t\tArithmetic Operations\n","-"*50)
print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")
print("5. Floor Division \n6. Modulus \n7. Exponentiation \n8. Exit")
print("-"*50)
choice=int(input("Enter your choice : "))
print("-"*50)
if(choice==8):
    print("Thanks for using")
    sys.exit()
match(choice) :
    case 1 :
        num1=int(input("Enter the first number : "))
        num2=int(input("Enter the secound number : "))
        print("Addition({},{}) = {}".format(num1,num2,(num1+num2)))
    case 2 :
        num1=int(input("Enter the first number : "))
        num2=int(input("Enter the secound number : "))
        print("Subtraction({},{}) = {}".format(num1,num2,num1-num2))
    case 3 :
        num1=int(input("Enter the first number : "))
        num2=int(input("Enter the secound number : "))
        print("Multiplication({},{}) = {}".format(num1,num2,num1*num2))
    case 4 :
        num1=int(input("Enter the first number : "))
        num2=int(input("Enter the secound number : "))
        print("Division({},{}) = {}".format(num1,num2,num1/num2))
    case 5 :
        num1=int(input("Enter the first number : "))
        num2=int(input("Enter the secound number : "))
        print("Floor Division({},{}) = {}".format(num1,num2,num1//num2))
    case 6 :
        num1=int(input("Enter the first number : "))
        num2=int(input("Enter the secound number : "))
        print("Modulus({},{}) = {}".format(num1,num2,num1%num2))
    case 7 :
        num1=int(input("Enter the base number : "))
        num2=int(input("Enter the power number : "))
        print("Exponentiation({},{}) = {}".format(num1,num2,num1**num2))
    case 8 :
        print("Thanks for using")
        sys.exit()
    case _ :
        print("Please enter a valid choice in the menu. Choice must be [1-8]")