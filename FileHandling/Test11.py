try:
    with open('file5.txt','r') as file5:
        print('*** File opened sucessfully ***')
        fileReader=file5.readlines()
except FileNotFoundError:
    print('file does not exists')
else:
    print('-'*50)
    print('\t\tData')
    print('-'*50)
    for data in fileReader :
        print(data,end="")