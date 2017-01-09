import pygame, sys, time, random
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()
playSurface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Memory Box')
redColour = pygame.Color(255, 0, 0)
blackColour = pygame.Color(0, 0, 0)
whiteColour = pygame.Color(255, 255, 255)
greyColour = pygame.Color(150, 150, 150)
greenColor = pygame.Color(0, 255, 0)
yellowColor = pygame.Color(255, 255, 0)
boxesPosition = [240, 400, 300, 400, 360, 400, 300, 340]
play = []
randomPlay = []
nivel = 1
boxes = 4

def greenBox1():
    return pygame.draw.rect(playSurface, greenColor, Rect(boxesPosition[0], boxesPosition[1], 40, 40))


def whiteBox1():
    return pygame.draw.rect(playSurface, whiteColour, Rect(boxesPosition[0], boxesPosition[1], 40, 40))


def greenBox2():
    return pygame.draw.rect(playSurface, greenColor, Rect(boxesPosition[2], boxesPosition[3], 40, 40))


def whiteBox2():
    return pygame.draw.rect(playSurface, whiteColour, Rect(boxesPosition[2], boxesPosition[3], 40, 40))


def greenBox3():
    return pygame.draw.rect(playSurface, greenColor, Rect(boxesPosition[4], boxesPosition[5], 40, 40))


def whiteBox3():
    return pygame.draw.rect(playSurface, whiteColour, Rect(boxesPosition[4], boxesPosition[5], 40, 40))


def greenBox4():
    return pygame.draw.rect(playSurface, greenColor, Rect(boxesPosition[6], boxesPosition[7], 40, 40))


def whiteBox4():
    return pygame.draw.rect(playSurface, whiteColour, Rect(boxesPosition[6], boxesPosition[7], 40, 40))

def gameOver():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 24)
    gameOverSurf = gameOverFont.render('Game Over', True, redColour)
    gameOverRect = gameOverSurf.get_rect()
    gameOverRect.midtop = (320, 10)
    playSurface.blit(gameOverSurf, gameOverRect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()


def win():
    winFont = pygame.font.Font('freesansbold.ttf', 24)
    winSurf = winFont.render('Nivel %d' % nivel, True, yellowColor)
    winRect = winSurf.get_rect()
    winRect.midtop = (320, 10)
    playSurface.blit(winSurf, winRect)
    pygame.display.flip()
    time.sleep(2)


def start():
    playSurface.fill(blackColour)
    whiteBox1()
    whiteBox2()
    whiteBox3()
    whiteBox4()
    pygame.display.flip()


# gerando os boxes randomicamente
def generateBoxes():
    randomPlay = []

    for i in range(boxes):
        randomPlay.append(random.randrange(1, 5))
    print(randomPlay)

    # Mostrando ao jogador os boxes gerados
    for b in randomPlay:
        start()
        if (b == 1):
            greenBox1()
            pygame.display.flip()
            time.sleep(1)
        if (b == 2):
            greenBox2()
            pygame.display.flip()
            time.sleep(1)
        if (b == 3):
            greenBox3()
            pygame.display.flip()
            time.sleep(1)
        if (b == 4):
            greenBox4()
            pygame.display.flip()
            time.sleep(1)
    fpsClock.tick(20)
    return randomPlay

#Jogando
while True:
    gaming = True
    start()
    computer = generateBoxes()

    while gaming:
        start()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == ord('d'):
                    greenBox3()
                    pygame.display.flip()
                    play.append(3)
                if event.key == K_LEFT or event.key == ord('a'):
                    greenBox1()
                    pygame.display.flip()
                    play.append(1)
                if event.key == K_UP or event.key == ord('w'):
                    greenBox4()
                    pygame.display.flip()
                    play.append(4)
                if event.key == K_DOWN or event.key == ord('s'):
                    greenBox2()
                    pygame.display.flip()
                    play.append(2)
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
                if event.key == K_RETURN:
                    if play == computer:
                        play = []
                        nivel += 1
                        boxes += 1
                        win()
                    else:
                        gameOver()
                    gaming = False

        print(play)
        fpsClock.tick(60)
