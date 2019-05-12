# -*- coding: utf-8 -*-
"""
Created on Thu May  9 21:53:54 2019

@author: VitorMiada
"""

import pygame,sys
from pygame.locals import *
pygame.init()

yc = "coracao.png"


skn = pygame.display.set_mode((640,360),0,32)
rc = pygame.image.load(yc).convert_alpha()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    skn.fill((0,0,0))
    x,y = pygame.mouse.get_pos()
    x -= rc.get_width()/2
    y -= rc.get_height()/2
    skn.blit(rc,(x,y))
    pygame.display.update()