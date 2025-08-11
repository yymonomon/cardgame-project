import pygame
from pygame.locals import *
import sys
import random
import json
import textBasedUtils as tbu

pygame.init()

#define some colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
grey = pygame.Color(128, 128, 128)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
cyan = pygame.Color(0, 255, 255)
magenta = pygame.Color(255, 0, 255)
yellow = pygame.Color(255, 255, 0)

#scaling factor for all* images. (*most)
SCALE = 2

#window                               vvvvvvvvvvv  window size: 720p (I think)
DISPLAY = pygame.display.set_mode((1280, 720))

FramePerSec = pygame.time.Clock()
FPS = 30
DT = 0

RUNNING = True

KEYS = pygame.key.get_pressed()
MOUSE = pygame.mouse.get_pressed()



class Pack (pygame.sprite.Sprite):
    def __init__(self, arrCardPool, strImage):
        pygame.sprite.Sprite.__init__(self)
        self.Pool = pygame.sprite.Group(arrCardPool)
        self.Image = strImage

    #def pull(self):

def getKeys():
    KEYS = pygame.key.get_pressed()
    MOUSE = pygame.mouse.get_pressed()

tbu.gameStart()
while RUNNING:
    DISPLAY.fill(white)
    getKeys()

    for event in pygame.event.get():
        if event.type == QUIT:
            RUNNING = False

    pygame.display.update()

    DT = FramePerSec.tick(FPS) / 1000

sys.exit()
pygame.quit()
