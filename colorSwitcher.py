import graphics as gp

win=gp.GraphWin('color switcher',600,600)
win.setBackground('tomato')
leftPupil=gp.Point(75,75)
leftEye=gp.Circle(leftPupil,50)
leftEye.draw(win).setFill('red')
leftPupil.draw(win)
rightPupil=gp.Point(525,75)
rightEye=gp.Circle(rightPupil,50)
rightEye.draw(win).setFill('red')
rightPupil.draw(win)
bigNose=gp.Rectangle(gp.Point(200,300),gp.Point(360,380))
bigNose.draw(win).setOutline('orange')
mouth=gp.Oval(gp.Point(200,500),gp.Point(400,597))
mouth.draw(win).setFill('white')
ligne=gp.Line(gp.Point(300,450),gp.Point(350,450))
ligne.draw(win)
ligne2=gp.Line(gp.Point(200,450),gp.Point(250,450))
ligne2.draw(win)
