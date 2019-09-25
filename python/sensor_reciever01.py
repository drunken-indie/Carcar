import pygame, serial, time
class BlueTooth:
    def __init__(self):
        self.port="/dev/tty.HC-05-DevB"
        self.bluetooth=serial.Serial(self.port, 9600)
    def recvMsg(self):
        input_data=self.bluetooth.readline()
        print(input_data.decode())
    def sendMsg(self, msg):
        
        time.sleep(0.1)
        self.bluetooth.write(str.encode(str(msg)))
    def terminate(self):
        self.bluetooth.close()
def getInput():
    bluetooth=BlueTooth()
    counter=0
    while True:
        bluetooth.recvMsg()
        
        
            

def main():
    
    getInput()

if __name__=='__main__':
    getInput()