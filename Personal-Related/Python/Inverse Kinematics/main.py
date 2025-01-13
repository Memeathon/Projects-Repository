import pygame
import math
from utils import *

pygame.init()

window = pygame.display.set_mode((800, 600))

root = pygame.Rect((100, 400, 30, 50))

BASE_COLOUR = (255, 255, 153)
BODY_COLOUR = (255, 255, 255)
UPPER_LEG_LENGTH = 100
LOWER_LEG_LENGTH = 50

body = [root]
mousepos = pygame.mouse.get_pos()

while True:
    
    window.fill((0, 0, 0))
    mousepos = pygame.mouse.get_pos()

    Basecorners = get_rect_corners(root.center, mousepos, 10)
    #pygame.draw.polygon(window, BASE_COLOUR, Basecorners)

    _, Knee = getKneeJointCoords(root.center, mousepos, UPPER_LEG_LENGTH, LOWER_LEG_LENGTH)

    upperLegcorners = get_rect_corners(root.center, Knee, 10)
    pygame.draw.polygon(window, BODY_COLOUR, upperLegcorners)

    lowerLegcorners = get_rect_corners(Knee, mousepos, 10)
    pygame.draw.polygon(window, BODY_COLOUR, lowerLegcorners)

    for bodyparts in body:
        pygame.draw.rect(window, BODY_COLOUR, bodyparts)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    pygame.display.flip()