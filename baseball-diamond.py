import graphics as gp
from graphics import *
win=gp.GraphWin('baseball diamond',500,500)
win.setBackground('darkgreen')
bigCircle=gp.Circle(gp.Point(250,250),150)
bigCircle.draw(win).setFill('darkgrey')
topRectangle=gp.Rectangle(gp.Point(242,154),gp.Point(250,160))
topRectangle.draw(win).setFill('white')
leftRectangle=topRectangle.clone().move()
leftRectangle.draw(win)
for clickCount in range(600):
    clickPoint = win.getMouse()
    Text( clickPoint, clickPoint ).draw( win )
