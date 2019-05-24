
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
pygame.init()

FPS=60
WIDTH=1440
HEIGHT=810
skn= pygame.display.set_mode((WIDTH,HEIGHT)) 


class jogador(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        player_img = pygame.image.load('link1.png').convert()
        #walkRight = [pygame.image.load('link1.png'), pygame.image.load('link2.png'), pygame.image.load('link3.png'), pygame.image.load('link4.png'), pygame.image.load('link5.png'), pygame.image.load('link6.png'), pygame.image.load('link7.png'), pygame.image.load('link8.png')]
        #walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
        #char = pygame.image.load('standing.png')
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (35, 50))
        
        # Deixando transparente.
        self.image.set_colorkey((137,164,125))
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.x=0
        self.rect.y=HEIGHT-200
        self.speedy =0
        self.speedx =0
    # Metodo que atualiza a posição do link
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.x > WIDTH-100:
            self.rect.x = WIDTH-100
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y < 250:
            self.rect.y=250
        if self.rect.y > HEIGHT-200:
            self.rect.y= HEIGHT-200
        print(self.rect.x,self.rect.y)    
        if self.rect.y<609 and self.rect.x<344 and self.rect.y>249 and self.rect.x>-1:
            self.rect.x+=8
            self.rect.y+=8
        if self.rect.y<=374 and self.rect.x<952 and self.rect.y>274 and self.rect.x>200:
            self.rect.x+=8
            self.rect.y-=8
        if self.rect.y<498 and self.rect.x<952 and self.rect.y>374 and self.rect.x>200:
            self.rect.x+=8
            self.rect.y+=8
        if self.rect.y<586 and self.rect.x<579 and self.rect.y>497 and self.rect.x>488:
            self.rect.x-=8
            self.rect.y+=8
        if self.rect.y<586 and self.rect.x<952 and self.rect.y>497 and self.rect.x>578:
            self.rect.x+=8
            self.rect.y+=8
        if self.rect.y<586 and self.rect.x<952 and self.rect.y>497 and self.rect.x>578:
            self.rect.x+=8
            self.rect.y+=8
        if self.rect.y<=410 and self.rect.x<=1192 and self.rect.y>=300 and self.rect.x>=1136:
            fase2()
        if self.rect.y<=530 and self.rect.x<=488 and self.rect.y>=498 and self.rect.x>=344:
            fase1()
        if self.rect.y<=610 and self.rect.x<=1340 and self.rect.y>=274 and self.rect.x>=1196:
            self.rect.x-=8
            self.rect.y-=8    
    
class bgc(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        bg = pygame.image.load("mapagame.png").convert()
        self.image = pygame.transform.scale(bg, (WIDTH,HEIGHT))
       
        self.rect = self.image.get_rect()
        self.rect.x=0
        self.rect.y=0
        self.speedx=0
        
    def uptade(self):
        self.rect.x += self.speedx
        
        
    
     
    
clock = pygame.time.Clock()

pygame.init()
pygame.mixer.init()
all_sprites = pygame.sprite.Group()
#mapa= pygame.sprite.Group()
backg = bgc()
all_sprites.add(backg)
#mapa.add(backg)

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
    all_sprites.update()        
    all_sprites.draw(skn)                       
    pygame.display.flip()
            
pygame.quit()

#ainda sem o background e a skin do char
