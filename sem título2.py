# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:57:18 2019

@author: insper
"""

import random
import time
from os import path
import pygame,sys
from pygame.locals import *
pygame.init()

yc = "coracao.png"

BLACK = (0, 0, 0)
WHITE = (255,255,255)
skn = pygame.display.set_mode((480,600),0,32)
rc = pygame.image.load(yc).convert_alpha()
pygame.display.set_caption("Undertail")
background = pygame.image.load('Chão dungeon.png').convert()
background_rect = background.get_rect()
#skn.fill(WHITE)
running = True
try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        skn.fill((0,0,0))
        x,y = pygame.mouse.get_pos()
        x -= rc.get_width()/2
        y -= rc.get_height()/2
        
        skn.blit(background, background_rect)
        #skn.fill(BLACK(200,100,300,400))
        skn.blit(rc,(x,y))
        
        #pygame.display.update()
        pygame.display.flip()
        
    
        
    
finally:
    
    pygame.quit()
    sys.exit()