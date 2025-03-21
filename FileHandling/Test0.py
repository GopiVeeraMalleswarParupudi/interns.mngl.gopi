stdData={}
for records in range(0,num if 0<(num:=int(input('Enter the number of records : ')))<20 else print('Please enter valid range[1-20]') ):
   s={}
   s['sno']=input('Enter your roll number : ')
   s['name']=input('Enter your name : ')        
   s['age']=int(input('Enter your age in years : '))
   stdData['student-{}_data'.format(records)]=s
print(stdData)