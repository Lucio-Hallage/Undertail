
import pygame,sys
from pygame.locals import *
import random
import time
from os import path
from Fase1 import fase1
from Fase2 import fase2
from Fase3 import fase3
from Fase4 import fase4
from Fase5 import fase5
from tkinter import *
from tkinter import messagebox

pygame.init()

inventario=[]
FPS=60
WIDTH=480
HEIGHT=600
skn= pygame.display.set_mode((WIDTH,HEIGHT)) 


class jogador(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        player_img = pygame.image.load('yasuo1.png').convert()
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (100, 138))
        
        # Deixando transparente.
        self.image.set_colorkey((137,164,125))
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.x=184
        self.rect.y=WIDTH
        self.speedy =0
        self.speedx =0
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.x<-15:
            self.rect.x=-15
        if self.rect.x>384:
            self.rect.x=384
        if self.rect.y<56:
            self.rect.y=56
        if self.rect.y>WIDTH:
            self.rect.y=WIDTH
        if self.rect.x<=57 and self.rect.x>=-15 and self.rect.y<=440 and self.rect.y>=376 and 'Fase1' not in inventario:
            inventario.append(fase1())
        if self.rect.x<=384 and self.rect.x>=320 and self.rect.y<=440 and self.rect.y>=376 and 'Fase2' not in inventario:
            inventario.append(fase2())
        if self.rect.x<=57 and self.rect.x>=-15 and self.rect.y<=216 and self.rect.y>=152 and 'Fase3' not in inventario:
            inventario.append(fase3())
        if self.rect.x<=384 and self.rect.x>=320 and self.rect.y<=216 and self.rect.y>=152 and 'Fase4' not in inventario:
            inventario.append(fase4())
        
        print(self.rect.x,self.rect.y)
     
    
clock = pygame.time.Clock()

pygame.init()
pygame.mixer.init()
bg = pygame.image.load("mapa.png").convert()
background = pygame.transform.scale(bg, (WIDTH,HEIGHT))
background_rect = background.get_rect()
all_sprites = pygame.sprite.Group()

player = jogador()
#link= pygame.sprite.Group()
all_sprites.add(player)
#link.add(player)


run = True
while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx = -8
            if event.key == pygame.K_RIGHT:
                player.speedx = 8
            if event.key == pygame.K_UP:
                player.speedy = -8
            if event.key == pygame.K_DOWN:
                player.speedy = 8
                    # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx = 0
            if event.key == pygame.K_RIGHT:
                player.speedx = 0
            if event.key == pygame.K_UP:
                player.speedy = 0
            if event.key == pygame.K_DOWN:
                player.speedy = 0
    skn.blit(background,background_rect)
    all_sprites.update()        
    all_sprites.draw(skn)                       
    pygame.display.flip()
            
pygame.quit() 

    
    #ainda sem o background e a skin do char
