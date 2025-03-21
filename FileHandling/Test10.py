try:
    with open('file5.txt','r') as file5:
        print('***File opened sucefully***')
        fileReader = file5.readlines()

except FileNotFoundError:
    print('File does not exist')
else:
    print('-'*50)
    print('\t\tData')
    print('-'*50)
    print(fileReader)
    print('-'*50)
    print('Type of data : {}'.format(type(fileReader)))