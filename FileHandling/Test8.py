try:
    with open('file6.txt','w') as file6:
        print('file-6 created sucessfully')
        l=[10,20,0,40,50]
        file6.writelines(str(l)+'\n')
        file6.writelines([str(num)+'\t' for num in l if num>0])
        file6.writelines('\n')
        file6.write('Type of data : {}'.format(type(l))) 
        file6.writelines('\n')
        file6.writelines('-'*60)
        file6.writelines('\n')
        s={10,20,0,40,50}
        file6.writelines(str(s)+'\n')
        file6.writelines({str(num)+'\t' for num in s if num>0})
        file6.writelines('\n')
        file6.writelines('Type of data : {}'.format(type(s)))
        file6.writelines('\n')
        file6.writelines('-'*60)
        file6.writelines('\n')
        d={10:'ten',20:'twenty',30:'thirty',40:'fourty',50:'fifty'}
        file6.writelines(str(d)+'\n')
        file6.writelines(str(d.keys())+'\n')
        file6.writelines([str(key)+'\t' for key in d.keys()])
        file6.write('\n')
        file6.write(str(d.values())+'\n')
        file6.writelines([str(value)+'\t' for value in d.values()])
        file6.writelines('\n')
        file6.write('Type of data : {}'.format(type(d)))
        file6.writelines('\n')
        file6.writelines('-'*60)
        file6.writelines('\n')
except Exception as e:
    print(e)
else :
    print('Data saved sucessfully')