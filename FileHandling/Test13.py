'''
write a program which will copy the content of one into another file.
'''
class NoDataFound(Exception):pass

def writeData(fileName):
    def wrapper(readData):
        def writingDataToFile():
            data=readData()
            with open(fileName,'w') as writeFile:
                writeFile.writelines(data)
        return writingDataToFile
    return wrapper


@writeData(input('Enter the destination file name : '))
def readData():
    fileName=input('Enter the source file name : ')
    with open(fileName,'r') as readFile:    
        if (data:=readFile.read())=='':
            raise NoDataFound 
        else:
            return data
            

        

#main propgram
try:
    readData()
except FileNotFoundError:
    print('File does not exists')
except NoDataFound:
    print('No data found in the file')
except Exception as e:
    print(e)
else:
    print('copying data from source file to destination file sucessfully')