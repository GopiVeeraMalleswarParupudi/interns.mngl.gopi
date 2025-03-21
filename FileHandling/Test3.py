try:
    filePath='D:/PythonFullStack/CorePython/FileHandling/file1.txt'
    with open(filePath,'r') as file:
        print('File opened in read mode sucessfully')
except FileNotFoundError:
    print('File does not exist')
else:
    print('Type of file : ',type(file))