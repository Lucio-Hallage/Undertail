#programa do cursor
import pygame,sys
from pygame.locals import *
import random

#determinar tamanho tela
WIDTH = 360
HEIGHT = 480
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
        image.fill(AMARELO)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2 , HEIGHT/2)

# initialize pyagme and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Donkey Kong 5")
clock = pygame.time.Clock()

yc = "coracao.png"


skn = pygame.display.set_mode((640,360),0,32)
rc = pygame.image.load(yc).convert_alpha()

all_sprites = pygame.sprite.Group()
player = Jogador()
all_sprites,add(player)

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
    skn.fill(AMARELO)
    x,y = pygame.mouse.get_pos()
    x -= rc.get_width()/2
    y -= rc.get_height()/2
    skn.blit(rc,(x,y))
    pygame.display.update()

    #updates
    all_sprites.update()

    #gráficos/desenhos
    screen.fill(AMARELO)
    all_sprites.draw(screen)
    # depois de desenhar tudo 
    pygame.display.flip()

pygame.quit()
