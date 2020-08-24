phrase=str(input('Input your phrase: '))
repeater=int(input('How many times should it be repeated ? '))

for i in range(repeater):
    print ( str(i+1)  + ' ' + phrase)