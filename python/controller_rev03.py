import pygame, serial, time
from graphics import *
class BlueTooth:
    def __init__(self):
        self.port="/dev/tty.HC-05-DevB"
        self.bluetooth=serial.Serial(self.port, 9600)
    def sendMsg(self, msg):
        self.bluetooth.write(str.encode(str(msg)))
        input_data=self.bluetooth.readline()
        #print(input_data.decode())
        time.sleep(0.1)
    def terminate(self):
        self.bluetooth.close()
class Graph:
    def __init__(self):
        fillColor='gray'
        outlineColor='black'
        self.win = GraphWin("Control", 500, 500)
        #downTriangle
        self.downTriangle = Polygon([Point(250, 450), Point(200, 350), Point(300, 350)])
        self.downTriangle.setFill(fillColor)
        #upTriangle
        self.upTriangle = Polygon([Point(250, 50), Point(200, 150), Point(300, 150)])
        self.upTriangle.setFill(fillColor)
        #leftTriangle
        self.leftTriangle = Polygon([Point(50, 250), Point(150, 200), Point(150, 300)])
        self.leftTriangle.setFill(fillColor)
        #rightTriangle
        self.rightTriangle = Polygon([Point(450, 250), Point(350, 200), Point(350, 300)])
        self.rightTriangle.setFill(fillColor)
        #automated
        self.autoCircle = Circle(Point(75, 75), 50)
        self.autoCircle.setFill(fillColor)
        #draw it
        #self.downTriangle.setWidth(4)
        self.downTriangle.draw(self.win)
        #self.upTriangle.setWidth(4)
        self.upTriangle.draw(self.win)
        #self.leftTriangle.setWidth(4)
        self.leftTriangle.draw(self.win)
        #self.rightTriangle.setWidth(4)
        self.rightTriangle.draw(self.win)
        self.autoCircle.draw(self.win)

    def upOn(self):
        self.upTriangle.setFill('red')
    def upOff(self):
        self.upTriangle.setFill('gray')
    def downOn(self):
        self.downTriangle.setFill('red')
    def downOff(self):
        self.downTriangle.setFill('gray')
    def rightOn(self):
        self.rightTriangle.setFill('red')
    def rightOff(self):
        self.rightTriangle.setFill('gray')
    def leftOn(self):
        self.leftTriangle.setFill('red')
    def leftOff(self):
        self.leftTriangle.setFill('gray')

def getInput():
    controller = Graph()
    bluetooth=BlueTooth()
    pygame.init()
    # to spam the pygame.KEYDOWN event every 100ms while key being pressed
    pygame.key.set_repeat(100, 100)
    keyPressed=[0,0,0,0]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    controller.upOn()
                    keyPressed[0]=1
                elif event.key == pygame.K_DOWN:
                    controller.downOn()
                    keyPressed[1]=1
                elif event.key == pygame.K_RIGHT:
                    controller.rightOn()
                    keyPressed[2]=1
                elif event.key == pygame.K_LEFT:
                    controller.leftOn()
                    keyPressed[3]=1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    controller.upOff()
                    keyPressed[0]=0
                elif event.key == pygame.K_DOWN:
                    controller.downOff()
                    #print ('stop backward')
                    keyPressed[1]=0
                elif event.key == pygame.K_RIGHT:
                    controller.rightOff()
                    #print ('stop right')
                    keyPressed[2]=0
                elif event.key == pygame.K_LEFT:
                    controller.leftOff()
                    #print ('stop left')
                    keyPressed[3]=0

        #print(keyPressed)

        msg=sendIt(keyPressed)
        bluetooth.sendMsg(msg)
        
            

def sendIt(keyPressed):
    message=0
    for i in range (len(keyPressed)):
        message+=((2**i)*keyPressed[i])
    return message

def main():
    
    getInput()

if __name__=='__main__':
    getInput()