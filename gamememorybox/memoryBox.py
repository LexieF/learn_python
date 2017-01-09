import pygame, sys, time, random
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
running = True

#Desenhando as boxes brancas e verdes
def greenBox1():
    return pygame.draw.rect(display, greenColor, Rect(boxesPosition[0], boxesPosition[1], 40, 40))


def whiteBox1():
    return pygame.draw.rect(display, whiteColour, Rect(boxesPosition[0], boxesPosition[1], 40, 40))


def greenBox2():
    return pygame.draw.rect(display, greenColor, Rect(boxesPosition[2], boxesPosition[3], 40, 40))


def whiteBox2():
    return pygame.draw.rect(display, whiteColour, Rect(boxesPosition[2], boxesPosition[3], 40, 40))


def greenBox3():
    return pygame.draw.rect(display, greenColor, Rect(boxesPosition[4], boxesPosition[5], 40, 40))


def whiteBox3():
    return pygame.draw.rect(display, whiteColour, Rect(boxesPosition[4], boxesPosition[5], 40, 40))


def greenBox4():
    return pygame.draw.rect(display, greenColor, Rect(boxesPosition[6], boxesPosition[7], 40, 40))


def whiteBox4():
    return pygame.draw.rect(display, whiteColour, Rect(boxesPosition[6], boxesPosition[7], 40, 40))

def begin():
    display.fill(blackColour)
    whiteBox1()
    whiteBox2()
    whiteBox3()
    whiteBox4()
    pygame.display.flip()

def start():
    randomPlay = []
    boxes = 4
    nivel = 1

    # Gerando os boxes randomicamente
    c = 0
    for i in range(boxes):
        randomPlay.append(random.randrange(1, 4))
        c += 1
    print('c %d' % c)
    print(randomPlay)

    # Mostrando ao jogador os boxes gerados
    e = 0
    for b in randomPlay:
        start()
        e += 1
        if (b == 1):
            greenBox1()
            pygame.display.flip()
            time.sleep(1)
            pygame.display.flip()
        if (b == 2):
            greenBox2()
            pygame.display.flip()
            time.sleep(1)
            pygame.display.flip()
        if (b == 3):
            greenBox3()
            pygame.display.flip()
            time.sleep(1)
            pygame.display.flip()
        if (b == 4):
            greenBox4()
            pygame.display.flip()
            time.sleep(1)
            pygame.display.flip()
    randomPlay = []
    pygame.display.flip()
    print('e %d' % e)

while running == True:
    begin()
    start()