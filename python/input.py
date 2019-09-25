import sys,tty,termios
class _Getch:       
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(9)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch


def getInput():
        inkey = _Getch()
        #up, down, right, left
        keyPressed=[0,0,0,0]
        while(1):
                k=inkey()
                if k!='':break
        for i in range(0, 9, 3):
        	key=k[i:i+3]
        	if key=='\x1b[A':
                	keyPressed[0] = 1
        	elif key=='\x1b[B':
                	keyPressed[1] = 1
        	elif key=='\x1b[C':
                	keyPressed[2] = 1
        	elif key=='\x1b[D':
                	keyPressed[3] = 1
        	else:
                	break

        sendIt(keyPressed)

def sendIt(keyPressed):
	message=0
	for i in range (len(keyPressed)):
		message+=((2**i)*keyPressed[i])
	print (message)

def main():
    for i in range(0,5):
        getInput()

if __name__=='__main__':
    main()


'''
import termios
import sys
import fcntl
import os

def getKeyCode(blocking = True):
    fd = sys.stdin.fileno()
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)
    if not blocking:
        oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
    try:
        return ord(sys.stdin.read(1))
    except IOError:
        return 0
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        if not blocking:
            fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

def getKeyStroke():
    code  = getKeyCode()
    if code == 27:
        code2 = getKeyCode(blocking = False)
        if code2 == 0:
            return "esc"
        elif code2 == 91:
            code3 = getKeyCode(blocking = False)
            if code3 == 65:
                return "up"
            elif code3 == 66:
                return "down"
            elif code3 == 68:
                return "left"
            elif code3 == 67:
                return "right"
            else:
                return "esc?"
    elif code == 127:
        return "backspace"
    elif code == 9:
        return "tab"
    elif code == 10:
        return "return"
    elif code == 195 or code == 194:        
        code2 = getKeyCode(blocking = False)
        return chr(code)+chr(code2) # utf-8 char
    else:
        return chr(code)


while True:
    print (getKeyStroke())
'''