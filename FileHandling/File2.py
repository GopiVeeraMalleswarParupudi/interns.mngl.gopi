'''
write a program which will demonstrates how to write the data to the file.
'''
try:
    with open('file2.txt','w') as file:
        l=[10,'hello','world','qwqw','ewdwed','yfyff']
        file.writelines(list(map(lambda s : str(s),l)))
except Exception as e:
    print(e)