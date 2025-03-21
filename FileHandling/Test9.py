try:
    with open('file5.txt','r') as file5:
        print('***File opened sucessfully***')
        fileReader = file5.read()
        
except FileNotFoundError:
    print('file does not exist')
else:
    print('-'*50)
    print('\t\tData')
    print('-'*50)
    print(fileReader)
    print('=> Type of data : {}'.format(type(fileReader)))