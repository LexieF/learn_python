import pygame
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
display = pygame.display.set_mode((640, 480))
# suface = pygame.Surface((600, 440))
pygame.display.set_caption('Memory Box')
redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150, 150, 150)
greenColor = pygame.Color(0, 255, 0)
yellowColor = pygame.Color(255, 255, 0)
boxesPosition = [240, 400, 300, 400, 360, 400, 300, 340]
timer = pygame.time.Clock()

display.fill(blackColour)
pygame.display.flip()

while True:
    print('Inicio do Laco')
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                print('teclou enter')

    fpsClock.tick(20)