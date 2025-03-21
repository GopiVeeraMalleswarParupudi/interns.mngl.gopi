'''
write a program which will obtain internal information about the file such as file name, file mode, 
readability, writability and closability.
'''
try:
    with open('file3.txt','x+') as file1:
        print('File name : {}'.format(file1.name))
        print('File mode : {}'.format(file1.mode))
        print('File is readable : {}'.format(file1.readable()))
        print('File is writable : {}'.format(file1.writable()))
        print('File is closed : {}'.format(file1.closed))
except FileNotFoundError:
    print('File not found at your specified location')
except FileExistsError:
    print('The given File is already, please give another file')
else:
    print('-'*60)