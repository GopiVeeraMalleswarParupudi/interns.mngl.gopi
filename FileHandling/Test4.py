try:
    with open('file2.txt','w') as file:
        print('File opened sucessfully in write mode.')
except FileNotFoundError:
    print('File does not exists')
else:
    print('Type  of file : ',type(file))