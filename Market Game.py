#Market Game
import pygame
import random
import time
pygame.init()

class Door: 
    #self is replaced by the interpreter with the individual name assigned to an object when created
    #Ex: warrior = Character(100,50,10) // self is replaced with warrior which means that variables are accessed with warrior.health instead of self.health
    #"self" can be anything as long as you use the same term throughout the class. "self" is just the standard term. 
    def __init__(self,pos):
        self.pos = pos
    def SetPosition(self):
        



#Display
windowSize = [1280,660]
center = [windowSize[0] / 2,(windowSize[1] / 2)]


#Player
pos = [windowSize[0] / 2, (windowSize[1] / 2)]

#Room
room1 = [random.randint(100,300), random.randint(100,300)]
roomPos = [center[0] - (room1[0] / 2),center[1] - (room1[1] / 2)]

#PyGame Set-up
screen = pygame.display.set_mode((windowSize[0], windowSize[1]))
clock = pygame.time.Clock()
running = True



#Game
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                room1 = [random.randint(100,300), random.randint(100,300)]
                roomPos = [center[0] - (room1[0] / 2),center[1] - (room1[1] / 2)]
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        roomPos[0] += 1
    if keys[pygame.K_s]:
        roomPos[1] -= 1
    if keys[pygame.K_d]:
        roomPos[0] -= 1
    if keys[pygame.K_w]:
        roomPos[1] += 1
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    #room
    room = pygame.Rect(roomPos[0], roomPos[1], room1[0],room1[1])
    pygame.draw.rect(screen, "blue", room)

    #player
    pygame.draw.circle(screen, "green", (pos[0], pos[1]), 10)


    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()