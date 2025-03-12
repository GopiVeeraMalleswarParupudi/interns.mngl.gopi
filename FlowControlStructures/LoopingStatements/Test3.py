'''
write a progam which will generate multiplication table for a given positive integer value.
'''
table=int(input("Enter which number table you want to print : "))
limit = int(input("Enter the limit : "))
start=0
while(start<=limit):
    print("{} x {} = {}".format(table,start,table*start))
    start+=1