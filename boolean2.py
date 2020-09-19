# a=str(input('Enter the first fruit: '))
# b=str(input('Enter the second fruit: '))
# c=str(input('Enter the third fruit: '))
# if a[0]<b[0] and a[0]<c[0]:
#     firstWord=a
# elif b[0]<a[0] and b[0]<c[0]:
#     firstWord=b
# elif c[0]<b[0] and c[0]<a[0]:
#     firstWord=c
# if a[0]<b[0]:
#     if a[0]<c[0]:
#         print('the first word will be : ', a)
#     elif a[0]>c[0] and b[0]>c[0]:
#         print('the first word will be : ', c)
# else:
#     if c[0]>b[0]:
#         print('the first word will be : ', b)
#     elif a[0]>c[0] and b[0]>c[0]:
#         print('the first word will be : ', c)
    
numOfWord=int(input('Enter the number of word: '))
for string in range(numOfWord-1):
    userString=str(input('Enter the fruit: '))
    firstChar=userString[0]
    if userString[0]<=firstChar:
        alphaString=userString
        print('The first fruit is : ',alphaString)
