#programa do cursor
import pygame,sys
from pygame.locals import *
import random

#determinar tamanho tela
WIDTH = 1000
HEIGHT = 1000
FPS = 30

#determinar cores
PRETO = (0,0,0)
AMARELO = (244, 209, 66)
VERMELHO = (173, 15, 15)

# definindo os personagens
class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))  #TROCAR POR IMAGEM PLAYER
        #image.fill(AMARELO)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2 , HEIGHT/2)

# initialize pyagme and create window
pygame.init()
pygame.mixer.init()
#screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Undertail")
clock = pygame.time.Clock()

yc = "coracao.png"

skn = pygame.display.set_mode((640,360),0,32)
rc = pygame.image.load(yc).convert_alpha()
background = pygame.image.load('ChãoLava.png').convert()
background_rect = background.get_rect()

all_sprites = pygame.sprite.Group()
player = Jogador()
#all_sprites,add(player)

# Loop do jogo
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False

    #cursor coração
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    skn.fill(VERMELHO)
    x,y = pygame.mouse.get_pos()
    x -= rc.get_width()/2
    y -= rc.get_height()/2
    skn.blit(background, background_rect)
    skn.blit(rc,(x,y))
    #pygame.display.update()
    
        
        
        
        #pygame.display.update()
    pygame.display.flip()
    #updates
    all_sprites.update()

    #gráficos/desenhos
    skn.fill(AMARELO)
    all_sprites.draw(skn)
    # depois de desenhar tudo 
    

pygame.quit()
