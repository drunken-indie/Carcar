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

    def updateColor(self, keyPressed):
        if (keyPressed[0]==1):
            self.upTriangle.setFill('red')
        else:
            self.upTriangle.setFill('gray')
        if (keyPressed[1]==1):
            self.downTriangle.setFill('red')
        else:
            self.downTriangle.setFill('gray')
        if (keyPressed[2]==1):
            self.rightTriangle.setFill('red')
        else:
            self.rightTriangle.setFill('gray')
        if (keyPressed[3]==1):
            self.leftTriangle.setFill('red')
        else:
            self.leftTriangle.setFill('gray')

def getInput():
    controller = Graph()
    bluetooth=BlueTooth()
    pygame.init()
    # to spam the pygame.KEYDOWN event every 100ms while key being pressed
    pygame.key.set_repeat(1000, 1000)
    keyPressed=[0,0,0,0]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    #print ('go forward')
                    keyPressed[0]=1
                elif event.key == pygame.K_DOWN:
                    #print ('go backward')
                    keyPressed[1]=1
                elif event.key == pygame.K_RIGHT:
                    #print ('go right')
                    keyPressed[2]=1
                elif event.key == pygame.K_LEFT:
                    #print ('go left')
                    keyPressed[3]=1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    #print ('stop forward')
                    keyPressed[0]=0
                elif event.key == pygame.K_DOWN:
                    #print ('stop backward')
                    keyPressed[1]=0
                elif event.key == pygame.K_RIGHT:
                    #print ('stop right')
                    keyPressed[2]=0
                elif event.key == pygame.K_LEFT:
                    #print ('stop left')
                    keyPressed[3]=0

        #print(keyPressed)

        msg=sendIt(keyPressed, controller)
        bluetooth.sendMsg(msg)
        
            

def sendIt(keyPressed, controller):
    controller.updateColor(keyPressed)
    message=0
    for i in range (len(keyPressed)):
        message+=((2**i)*keyPressed[i])
    return message

def main():
    
    getInput()

if __name__=='__main__':
    getInput()