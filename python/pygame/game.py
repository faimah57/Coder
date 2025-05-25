import pygame
from pygame.locals import *
pygame.init()

size= width, height= 500,360
pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.quit()

