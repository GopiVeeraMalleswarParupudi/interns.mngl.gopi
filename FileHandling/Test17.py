'''
write a program which will copy an image
'''
from pickle import load,dump

def copyImage(srcFile,desFile):
    with open(srcFile,'rb') as readFile:
        with open(desFile,'wb') as writeFile:
            data=readFile.readlines()
            writeFile.writelines(data)

try:
    copyImage(input('Enter the source file name : '),input('Enter the destination file name : '))
    
except FileNotFoundError:
    print('File does not exists')
else:
    print('Image copied to file sucessfully')    