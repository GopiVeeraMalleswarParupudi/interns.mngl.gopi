try:
    filePath='D:/PythonFullStack/CorePython/FileHandling/file1.txt'
    file=open(filePath,'w')
except FileNotFoundError:
    print('File is not available at your provided location.')
else:
    print('File with name "{}"is opened sucessfully in writemode'.format(file.name))