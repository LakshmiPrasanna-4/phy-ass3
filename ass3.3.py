#To check whether the student is pass or fail
sno=int(input('Enter the sno:'))
sname=input('Enter the sname:')
group=input('Enter the group:')
s1=int(input('Enter maths marks'))
s2=int(input('Enter accounts marks'))
s3=int(input('Enter economics marks'))
if(s1>=40 and s2>=40 and s3>=40):
    print('Pass')
else:
    print('Fail')
