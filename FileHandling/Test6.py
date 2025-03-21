'''
write a program which will demonstrates how to write the data to the file.
'''
try:
    with open('file4.txt','w')as file4:
        print('file4.txt file is created sucessfully')
        file4.write('hello')
        file4.write('world')
        file4.write(100)
        file4.write('i')
        file4.write('am learning python')
except FileNotFoundError:
    print('file does not found')
else:
    print('***Data saved sucessfully.***')