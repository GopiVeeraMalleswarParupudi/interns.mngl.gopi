try:
    file=open('D:/PythonFullStack/CorePython/FileHandling/file1.txt','r')
except FileNotFoundError:
    print('File not available at your specified location. Please enter correct path.')