'''
write a program which will converts celcius into foreign heat and kelvin temperature.
'''
celcius=float(input("Enter the celcius : "))
foreignHeat = 1.8*celcius+32
kinetikHeat = celcius+273.15
print("-"*25,"\nResult\n","-"*25)
print("{} degrees centigrade of foreign heat is {}".format(celcius,foreignHeat))
print("{} degrees centigrade of foreign heat is {}".format(celcius,kinetikHeat))
'''
Enter the celcius : 27
------------------------- 
Result
 -------------------------
27.0 degrees centigrade of foreign heat is 80.6
27.0 degrees centigrade of foreign heat is 300.15
'''