
import pygame,sys
from pygame.locals import *
import random
import time
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
        player_img = pygame.image.load('yasuo1.png').convert()
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (100, 138))
        
        # Deixando transparente.
        self.image.set_colorkey((137,164,125))
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.x=0
        self.rect.y=HEIGHT-200
        self.speedy =0
        self.speedx =0
    # Metodo que atualiza a posição da navinha
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
            
        
        if not (self.rect.top > 564-25 or self.rect.left < 84 or self.rect.right > 396):
            print('fase1')
    
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
