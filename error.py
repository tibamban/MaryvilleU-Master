# try:
#     inputString = input("Enter your String: ")
#     characterIndex = int(input("Enter the index of the character you want: "))
# 
#     character = inputString[characterIndex]
#     print( "The character is", character )
# except IndexError:
#     print('The string does not have that many characters')
#

# inputString = input("Enter your String: ")
# characterIndex = int(input("Enter the index of the character you want: "))
# if (len(inputString)-1)<characterIndex:
#     print('outside')
# else:
#     characters = inputString[characterIndex]
#     print( "The character is", characters )

count = 0
inputWord = input("Enter a word ('quit' to stop): ")
while inputWord != 'quit':
    inputWord = input("Enter a word ('quit' to stop): ")
    if len( inputWord ) < 5:
        count = count + 1
print("You entered {0} words with less than 5 characters".format(count))

