from graphics import *

def main():
    win = GraphWin('My Window',500,500)
    win.setBackground(color_rgb(255,255,255))
    #grass and the base for the house 
    grass=Rectangle(Point(0,350),Point(500,500))
    grass.setFill('green')
    grass.draw(win)
    base=Rectangle(Point(150,250),Point(400,350))
    base.draw(win)
    #the windows
    windowLeft=Rectangle(Point(337,260),Point(367,281))
    windowLeft.draw(win).setFill('yellow')
    
    
                       
    windowRight=windowLeft.clone()
    windowRight.move(-150,0)
    windowRight.draw(win)
    #the roof
    roof=Polygon(Point(133,250),Point(269,118),Point(418,250))
    roof.draw(win).setFill(color_rgb(230,120,50))
    #the stairs
    firstStair=Rectangle(Point(251,350),Point(300,360))
    firstStair.draw(win).setFill('maroon')
    secondStair=firstStair.clone()
    secondStair.move(0,-5)
    secondStair.draw(win)
    # the door and the door handler
    door=Rectangle(Point(250,300),Point(300,350))
    door.draw(win).setFill('darkgrey')
    door_handler=Circle(Point(293,325),2)
    door_handler.draw(win)
    #the sun
    sun=Circle(Point(104,56),40)
    sun.draw(win).setFill('yellow')
    # the window dividers made at the end for programming purposes
    windowLeftDivider=Line(Point(202,260),Point(202,280))
    windowLeftDivider.draw(win)
    windowRightDivider=windowLeftDivider.clone()
    windowRightDivider.move(150,0)
    windowRightDivider.draw(win)

    t = Text(Point(50,250), "peacefull house")
    t.draw(win).setSize(13)
    
    # a little animation for days/nights 
    for clickCount in range(1):
        win.getMouse()
        clickPoint = sun.move(350,0)
        win.setBackground('darkgrey')
        sun.setFill('white')
    
        

    win.getMouse()
    win.close()
    
main()