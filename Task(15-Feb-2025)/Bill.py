#defining printBill function which will accepts order details dictionary object as input and 
# generates bill amount.
def printBill(order):
    bill=0.0
    i=0
    print('*'*20,'CUSTOMER BILL','*'*20)
    print('-'*50)
    print('S.No\tItems\tQty\tPrice\tAmount')
    print('-'*50)
    while(i<len(order)):
        orderItemNames=list(order.keys())
        itemPrice=price.get(orderItemNames[i])
        quantity=order.get(orderItemNames[i])
        itemBill=itemPrice*quantity
        print('{}\t{}\t{}\t{}\t{}\t'.format((i+1),orderItemNames[i],quantity,itemPrice,itemBill))
        bill+=itemBill
        i+=1
    print('-'*50)
    print('\t\t    Sub Total : {}'.format(bill))
    print('\t\t    CGST 2.5% : {}'.format(calGST(bill)))
    print('\t\t    SGST 2.5% : {}'.format(calGST(bill)))
    print('-'*50)
    grandTotal=bill+calGST(bill)+calGST(bill)
    print('\t\t  Grand Total : {}'.format(grandTotal))
    couponCode=input('      Enter PROMO code if any : ')
    if couponCode=='':
        print('\t\t\t\t***NO COUPON CODE ENTERED***')
    elif couponCode not in couponCodes:
        print('***YOU HAVE ENTERED WRONG COUPON CODE***')
    elif couponCode in couponCodes:  
        offerAmount=calOffer(grandTotal,couponCode)
        print('\t\t Offer Amount : {}'.format(offerAmount))
        print('-'*50)
        print('\t Total Payable Amount : {}'.format(grandTotal-offerAmount))
        
    print('-'*50)
    print('*'*15,'Thank You | Visit Again','*'*15)

#defining calGST function which will calculate GST for the provided bill and the calGST function accepts 
# bill amount in the form of float type and returns GST of the bill amount. 
def calGST(bill):
    return bill*(2.5/100)

def calOffer(billAmount,couponCode):
    offer=couponCodes.get(couponCode)
    return billAmount*(offer/100)

#defining hotel menu
menu={1:'IDLY',2:'DOSA',3:'VADA',
    4:'CHAPATHI',5:'PAROTA',6:'PURI',
    7:'MYSOOR BONDA',8:'ONION BONDA',9:'UPMA'}

#defining prices for each item
price={'IDLY':30.00,'DOSA':30.00,'VADA':40.00,
       'CHAPATHI':35.00,'PAROTA':40.00,'PURI':40.00,
       'MYSOOR BONDA':30.00,'ONION BONDA':30.00,'UPMA':25.00}

#defining coupon codes
couponCodes = {'WgbuDw':5,'vVAIZS':10,'GXati9':15,'DiBOxC':20,
                't5QqvH':25,'XbeTO5':30,'Kj9iD2':35,'seLnDu':40,
                'HVQntr':45,'Iz4oer':50,'DiPHT':55,'la2dvl':60,
                'htUWQm':65,'e3FgyW':70,'CjXaZs':75,'OvVty2':80}

#main program --> which will takes input from the user, stores into orderItem dict object 
#and calls printBil(orderDetalis) functions after reading the order menu.
orderItems={}
s=True
print('*'*50,'MENU','*'*50)
print("Enter '1' for IDLY\t\t|\tEnter '2' for DOSA \t\t|\tEnter '3' for VADA")
print("Enter '4' for CHAPATHI\t\t|\tEnter '5' for PAROTA \t\t|\tEnter '6' for PURI")
print("Enter '7' for MYSOOR BONDA\t|\tEnter '8' for ONION BONDA\t|\tEnter '9' for UPMA")
print('*'*41,'ENTER YOUR ORDER BELOW','*'*41)
while(s):
    item,quantity=input("Enter the item : "),input("Enter the quantity : ")
    if(item=='' or quantity==''):
        s=False
    else:
        i=list(menu.keys())
        if int(item) in i:
            print(menu.get(int(item)),"\t:\t",quantity+' Plates')
            orderItems[menu.get(int(item))]=float(quantity)
        else:
            print('Please enter valid menu item, You have entered wrong menu ID ["{}"]'.format(item))
            break
else:
    print(orderItems)
    if(len(orderItems)!=0):
        printBill(orderItems)
    else:
        print('No items entered to print the bill')