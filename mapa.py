
import pygame,sys
from pygame.locals import *
import random
import time
pygame.init()

win= pygame.display.set_mode((500,500))
screenWidth = 500
FPS=60
clock = pygame.time.Clock()

#walkRight = [pygame.image.load("")] 
#walkLeft = [pygame.image.load("")]
bg = pygame.image.load("mapagame.png")
bg1 = pygame.transform.scale(bg, (900, 500))
#char = pygame.image.load("")

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
        self.rect.x=20
        self.rect.y=20
        self.speedy = 0
        self.speedx = 0
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Mantem dentro da tela
               
    
class bgc(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        bg = pygame.image.load("mapagame.png")
        self.image = pygame.transform.scale(bg, (900, 500))
       
        self.rect = self.image.get_rect()
     
    
clock = pygame.time.Clock()

bg = pygame.image.load("mapagame.png")
bg1 = pygame.transform.scale(bg, (900, 500)) 
bg1_rect = bg1.get_rect()      
run = True
pygame.init()
pygame.mixer.init()
all_sprites = pygame.sprite.Group()
player = jogador()
link= pygame.sprite.Group()
all_sprites.add(player)
link.add(player)
mapa= pygame.sprite.Group()
all_sprites.add(bgc())
mapa.add(bgc())


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
            
    win.fill((255,255,255))
    win.blit(bg1,bg1_rect)
    all_sprites.draw(win)                   
    pygame.display.flip
    all_sprites.update()    
            
            
pygame.quit()

#ainda sem o background e a skin do char
