# value = int(input('Enter number : '))
#  
# if (value/10) < 1 :
#      print ('This is a one digit number')
# if (value/10) >= 1 :
#      print ('This number has more than one digit')

# myString=str(input('Enter the string: '))
# if len(myString) >=10 :
#     print('Maybe consider a more diminutive option?')
# else:
#     print('Short and sweet!')

studentNote=int(input('Enter the student note: '))

if 0 < studentNote < 60 :
    print('student need to retake the course ')
elif 60 <=studentNote < 90:
    print('student passed the course')
elif 90 <= studentNote <= 100 :
    print('student passed with honors')
else:
    print('the total course points entered is not a valid value, please check again')