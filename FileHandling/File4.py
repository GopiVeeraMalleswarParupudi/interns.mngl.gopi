'''
write a program which copy the content of one into another file.
'''
def writeData(filePath,data):
    with open(filePath,'w') as writeFile:
        status=True
        while(status):
            status=False if data!='\n\n' else writeFile.write(data)



def readData(filePath):
    with open(filePath,'r') as readFile:
        if(readFile.readable()):
            status=True
            data=''
            while(status):
                status=False if (readFile.read())=='' else data+readFile.read()
            return data
            
#main program
try:
    sourceFile=input('Enter the source file location :')
    destinationFile=input('Enter the destination file location : ')
    print('Press 1 for read-writing\nPress 2 for writing-reading')
    match(choice if 0<(choice:=int(input('Enter your choice : ')))<3 else print('Enter a valid option[1,2]')):
        case 1 :
            writeData(destinationFile,readData(sourceFile))
        case 2 :
            print(readData(sourceFile))
            writeData(destinationFile,readData(sourceFile))
except Exception as e :
    print(e)