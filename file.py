inputFile=input('Enter the users file name: ')
OutputFile=input('Enter the name for saving the user names')

inFile=open(inputFile,'r')
outFile=open(OutputFile,'w')

names=inFile.readlines()
for name in names:
    Names = name.split(',')
    firstname = Names[0]
    lastname = Names[1]
    username = firstname + lastname[0:3]
    username = username.lower()

print (username, file=outFile)

inFile.close()

outFile.close()

print ("All Done")