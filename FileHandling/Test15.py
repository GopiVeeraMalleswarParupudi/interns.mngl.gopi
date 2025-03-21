'''
write a program which will read the student data dynamically from keyboard and 
stored as a record in file
'''
from pickle import dump
def pickling(fileName,data):
    with open(fileName,'ab') as writeFile:
        dump(list(map(lambda dataFields: str(dataFields)+'\t' if dataFields!='\n' else str(dataFields),data)),writeFile)

def writeData(fileName,data):
    with open(fileName,'a') as writeFile:
        writeFile.writelines(list(map(lambda dataFields: str(dataFields)+'\t' if(dataFields!='\n') else str(dataFields),data)))


try:
    count=0
    fileName=input('Enter the file name : ')
    for records in range(0,int(input('Enter the number of records you want to enter : '))):
        stdData=[]
        stdData.append(int(input('Enter you roll number : ')))
        stdData.append(input('Enter your name : '))
        stdData.append(float(input('Enter your marks : ')))
        stdData.append('\n')
        print('-'*60)
        pickling(fileName,stdData)
        count+=1
    else:
        print('*** {} record inserted sucessfully ***'.format(count))

except FileNotFoundError:
    print('File does not exist')
else:
    print('Data saved sucessfully in file')