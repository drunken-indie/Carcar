from graphics import *

def main():
	fillColor='gray'
	outlineColor='black'
	win = GraphWin("Control", 500, 500)
	#downTriangle
	downTriangle = Polygon([Point(250, 450), Point(200, 350), Point(300, 350)])
	downTriangle.setFill(fillColor)
	downTriangle.setOutline(outlineColor)
	#upTriangle
	upTriangle = Polygon([Point(250, 50), Point(200, 150), Point(300, 150)])
	upTriangle.setFill(fillColor)
	upTriangle.setOutline(outlineColor)
	#leftTriangle
	leftTriangle = Polygon([Point(50, 250), Point(150, 200), Point(150, 300)])
	leftTriangle.setFill(fillColor)
	leftTriangle.setOutline(outlineColor)
	#rightTriangle
	rightTriangle = Polygon([Point(450, 250), Point(350, 200), Point(350, 300)])
	rightTriangle.setFill(fillColor)
	rightTriangle.setOutline(outlineColor)
	#automated
	autoCircle = Circle(Point(75, 75), 50)
	autoCircle.setFill(fillColor)
	#draw it
	downTriangle.setWidth(4)
	downTriangle.draw(win)
	upTriangle.setWidth(4)
	upTriangle.draw(win)
	leftTriangle.setWidth(4)
	leftTriangle.draw(win)
	rightTriangle.setWidth(4)
	rightTriangle.draw(win)
	autoCircle.draw(win)
	win.getMouse()
	win.close()

main()