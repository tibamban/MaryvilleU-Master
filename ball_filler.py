import math as mt
amoutOfBall=int(input('How many bowling balls will be manufactured ? '))
diameterOfBall=float(input('What is the diameter of each ball in inches ? '))
VolumeOfCore=int(input('What is the core volume in inches cubed ? '))
'''using the formula for a sphere'''
VolumeOfFiller=(mt.pi*4/3)*(diameterOfBall/2)**3
print('You will need ',amoutOfBall*(VolumeOfFiller-VolumeOfCore))