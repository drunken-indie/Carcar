import pygame

pygame.init()

# to spam the pygame.KEYDOWN event every 100ms while key being pressed
pygame.key.set_repeat(100, 100)
keyPressed=[0,0,0,0]
while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                #print ('go forward')
                keyPressed[0]=1
            if event.key == pygame.K_DOWN:
                #print ('go backward')
                keyPressed[1]=1
            if event.key == pygame.K_RIGHT:
                #print ('go right')
                keyPressed[2]=1
            if event.key == pygame.K_LEFT:
                #print ('go left')
                keyPressed[3]=1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                #print ('stop forward')
                keyPressed[0]=0
            if event.key == pygame.K_DOWN:
                #print ('stop backward')
                keyPressed[1]=0
            if event.key == pygame.K_RIGHT:
                #print ('stop right')
                keyPressed[2]=0
            if event.key == pygame.K_LEFT:
                #print ('stop left')
                keyPressed[3]=0

    print(keyPressed)