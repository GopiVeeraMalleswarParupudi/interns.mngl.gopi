'''
write a program which will read the student records from the file(un-pickling)
'''
from pickle import load

def writeData(sourceFile,destinationFile):
    stdData=unPickling(sourceFile)
    print(stdData)
    if(stdData!='No Data'):
        with open(destinationFile,'w') as writeFile:
            for records in stdData:
                for fields in records:
                    writeFile.writelines(fields)
    else:
        print('No data available in the source file')

def unPickling(sourceFile):
    stdData=[]
    with open(sourceFile,'rb') as readFile:
        while(True):
            try:
                record=load(readFile)
                stdData.append(record)
            except EOFError:break
    return stdData if len(stdData)>0 else 'No Data'
            


try:
    writeData(input('Enter the source file name : '),input('Enter the destination file name : '))
except FileNotFoundError:
    print('File does not exist')
else:
    print('***Data converted sucessfully from binary to text***')