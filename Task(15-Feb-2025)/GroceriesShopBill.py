item_codes={'gp':'grains_pusles','eg':'edibleOil_ghee',
            'ss':'sugar_sweetners','sc':'spices_condiments',
            'dn':'dryFruits_nuts','de':'dairyProducts_eggs',
            'bv':'beverages','sr':'snacks_readyToEat',
            'pc':'packed_cannedFood','he':'houseHoldEssentials'}
hsn_codes={"grains_pusles":0,"edibleOil_ghee":5,
           "sugar_sweetners":5,"spices_condiments":5,
           "dryFruits_nuts":5,"dairyProducts_eggs":0,
           "beverages":18,"snacks_readyToEat":12,
           "packed_cannedFood":12,"houseHoldEssentials":12}
b=True
numberOfItems=1
listItems={}
print("Enter '1' if items to be added. If there are no items to be added enter '0'.")
while(b):
    i=int(input("Enter your choice : "))
    match(i):
        case 1:
            itemName = input("Enter the item-{} Name : ".format(numberOfItems)).upper()
            itemCategory = input("Enter Category of item : ").lower()
            if itemCategory in item_codes.keys(): 
                itemPrice=input("Enter price for one quantity : ")
                itemQuantity = input("Enter the quantity : ")
                item=itemName+':'+itemCategory+':'+itemPrice+':'+itemQuantity
                listItems[numberOfItems]=item
                numberOfItems+=1
                print('-'*30)
            else:
                print("Please enter valid hsn codes")
        case 0:
            b=False
        case _:
            print("Please enter valid option[0,1]")
totalItemsPrice=0.0
totalItemsGST=0.0
print("*"*100)
print("\t\t\t\t\tCASH RECEIPT")
print("*"*100)
print("Item Number\tDescription\tPrice\tQuantity\tGST\tTotalPrice")
for itemNumber in range(1,len(listItems)+1):
    list=listItems.get(itemNumber).split(':')
    category=list[1]
    price=float(list[2])
    quantity=float(list[3])
    gst=price*((hsn_codes.get(item_codes.get(category)))/100)*quantity
    totalPrice=(price+gst)*quantity
    totalItemsGST+=gst
    totalItemsPrice+=price*quantity
    print('{}\t\t{}\t\t{}\t{}\t\t{}\t{}'.format(itemNumber,list[0],price,quantity,gst,totalPrice))
print('-'*50)
print('Total Price : {}'.format(totalItemsPrice))
print('Tax : {}'.format(totalItemsGST))
print('-'*50)
print('Total Payment : {}'.format(totalItemsPrice+totalItemsGST))
print('-'*50)