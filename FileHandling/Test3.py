'''
write a program which will read the data dynamically from keyboard and write it to the file.
'''

try:
    with open('file3.txt','w') as file:
        
        while(True):   
            file.write(text) if (text:=(input('Enter you data : ')))!='' else print('Please enter the valid data')
except Exception as e:
    print(e)