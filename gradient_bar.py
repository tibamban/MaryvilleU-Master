from graphics import *

topLeftRectPoint=Point(0,0)
bottomRightRectPoint=Point(66,386)

def gradient_bar() :
    win=GraphWin('Gradient Bar',400,400)
    for barCount in range(300):
        gradRect = Rectangle( topLeftRectPoint, bottomRightRectPoint )
        newrect=gradRect.clone()
        newrect.move(barCount,0)
        newrect.draw(win).setWidth(0)
        newrect.setFill(color_rgb(0,int((barCount*255)/300),0))
    
gradient_bar()
    