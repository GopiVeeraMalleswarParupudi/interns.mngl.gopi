'''
write a program which will read the student data from the keyboard and
 save as a record in a file(pickling).
'''
from pickle import dump

def writeData(fileName):
    def wrapper(readData):
        def writingDataToFile():
            with open(fileName,'w') as writeFile:
                dump(readData,writeFile)
        return writingDataToFile
    return wrapper

@writeData(input('Enter file name : '))
def readData():
    stdData={}
    for records in range(0,num if 0<(num:=int(input('Enter the number of records : ')))<20 else print('Please enter valid range[1-20]') ):
        s={}
        s['sno']=input('Enter your roll number : ')
        s['name']=input('Enter your name : ')
        s['age']=int(input('Enter your age in years : '))
        stdData['student-{}_data'.format(records)]=s



try:
    readData()
except FileNotFoundError:
    print('File does not exists')
else:
    print('Student data is saved sucessfully')