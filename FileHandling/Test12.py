'''
write a program which will read the data dynamically from keyboard and write it to the file.
'''

def writeData(readingData):
    def writingDataToFile():
        data=readingData()
        with open('file7.txt','w') as file7:
            file7.writelines(data)
    return writingDataToFile

@writeData
def readData():
    emptyLinesCount=0
    actualData=''
    print('Enter your data : ')
    print('-'*50)
    while(True):
        if (data:=input())=='':
            emptyLinesCount+=1
            if emptyLinesCount==2:
                break
        else:
            if(emptyLinesCount==1):
                actualData+='\n'
            actualData+=data+'\n'
            emptyLinesCount=0
    return actualData

#main program
try:
    print('*** Writing the data to the file ***')
    readData()
except Exception as e:
    print(e)
else:
    print('Data saved sucessfully to the file')