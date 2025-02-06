num=int(input("Enter the number : "))
if num not in range(0,10,1):
    print('please enter the valid number and the number must be in between [0-9]')
if(num>=0 and num<=9):
    if(num==0):
        print("Given number is zero")
    else:
        if(num==1):
            print("Given number is one")
        else:
            if(num==2):
                print("Given number is two")
            else:
                if(num==3):
                    print("Given number is three")
                else:
                    if(num==4):
                        print("Given number is four")
                    else:
                        if(num==5):
                            print("Given number is five")
                        else:
                            if(num==6):
                                print("Given number is six")
                            else:
                                if(num==7):
                                    print("Given number is seven")
                                else:
                                    if(num==8):
                                        print("Given number is eight")
                                    else:
                                        print("Given number is nine")
