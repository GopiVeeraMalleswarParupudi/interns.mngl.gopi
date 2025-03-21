try:
    with open('file.txt','x+') as file:
        print('Name : ',file.name)
        print('Type : ',type(file))
        print('Mode : ',file.mode)
        print('Is Readable : ',file.readable())
        print('Is Writable : ',file.writable())
        print('IS closed : ',file.closed)
except Exception as e:
    print(e)
    print("File doesn't exits" )