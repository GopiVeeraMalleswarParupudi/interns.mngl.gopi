try:
    with open('file5.txt','w') as file5:
        file5.write('hello\t')
        file5.write('world\n')
        file5.write('i am learning python')
except FileNotFoundError:
    print('file does not exist')
else:
    print('Data stored in the file sucessfully')