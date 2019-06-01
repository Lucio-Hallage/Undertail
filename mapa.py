
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

inventario=[]
FPS=60
WIDTH=480
HEIGHT=600
PRETO = (0,0,0)
AMARELO = (244, 209, 66)
VERMELHO = (255, 0, 0)
CINZA = (88,88,88)
BRANCO=(255,255,255)
VERDE = (0, 255, 0)
AZUL=(0,0,255)
skn= pygame.display.set_mode((WIDTH,HEIGHT)) 


pygame.init()
class jogador(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        player_img = pygame.image.load('link.png').convert()
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(player_img, (38, 52))
        
        # Deixando transparente.
        self.image.set_colorkey(CINZA)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Centraliza embaixo da tela.
        self.rect.x=240-38/2
        self.rect.y=600
        self.speedy =0
        self.speedx =0
    # Metodo que atualiza a posição do link
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if 'all' not in inventario:
             if self.rect.y<96:
                 self.rect.y=96
        if self.rect.x<20:
            self.rect.x=20
        if self.rect.x>430:
            self.rect.x=430       
        if self.rect.y>WIDTH+52:
            self.rect.y=WIDTH+52
        if self.rect.x<=100 and self.rect.x>=20 and self.rect.y<=500 and self.rect.y>=348 and 'Fase1' not in inventario:
            self.speedx=0
            self.speedy=0
            inventario.append(fase1())
            pygame.mixer.music.load('pokemonsong.wav')
            pygame.mixer.music.set_volume(2)
            pygame.mixer.music.play(loops=-1)
            Tk().wm_withdraw()#esconde a tela principal
            messagebox.showinfo('Continue','Parabens!!!Você passou a primeira fase. ')
        if self.rect.x<=428 and self.rect.x>=356 and self.rect.y<=500 and self.rect.y>=348 and 'Fase2' not in inventario:
            self.speedx=0
            self.speedy=0
            inventario.append(fase2())
            pygame.mixer.music.load('pokemonsong.wav')
            pygame.mixer.music.set_volume(2)
            pygame.mixer.music.play(loops=-1)
            Tk().wm_withdraw() #esconde a tela principal
            messagebox.showinfo('Continue','Parabens!!!Você passou a segunda fase. ')
        if self.rect.x<=100 and self.rect.x>=20 and self.rect.y<=268 and self.rect.y>=172 and 'Fase3' not in inventario:
            self.speedx=0
            self.speedy=0
            inventario.append(fase3())
            pygame.mixer.music.load('pokemonsong.wav')
            pygame.mixer.music.set_volume(2)
            pygame.mixer.music.play(loops=-1)
            Tk().wm_withdraw() #esconde a tela principal
            messagebox.showinfo('Continue','Parabens!!!Você passou a terceira fase. ')
        if self.rect.x<=428 and self.rect.x>=356 and self.rect.y<=268 and self.rect.y>=172 and 'Fase4' not in inventario:
            self.speedx=0
            self.speedy=0
            inventario.append(fase4())
            pygame.mixer.music.load('pokemonsong.wav')
            pygame.mixer.music.set_volume(2)
            pygame.mixer.music.play(loops=-1)
            Tk().wm_withdraw()#esconde a tela principal
            messagebox.showinfo('Continue','Parabens!!!Você passou a quarta fase. ')
        if 'Fase1' in inventario:
            if 'Fase2' in inventario:
                if 'Fase3' in inventario:
                    if 'Fase4' in inventario:
                        inventario.append('all')
        if self.rect.y<=0:
            fase5()
            pygame.quit()                      
     

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
pygame.mixer.music.load('pokemonsong.wav')
pygame.mixer.music.set_volume(2)
bgc = pygame.image.load("chão.png").convert()
background1 = pygame.transform.scale(bgc, (WIDTH,HEIGHT))
bg = pygame.image.load("mapa.png").convert()
bg.set_colorkey(BRANCO)
background = pygame.transform.scale(bg, (WIDTH,HEIGHT))
background_rect = background.get_rect()
score_font=pygame.font.Font("PressStart2P.ttf", 28)
porta = pygame.image.load('porta.jpg').convert()
porta = pygame.transform.scale(porta, (130,120))
porta.set_colorkey(PRETO)
sonic = pygame.image.load('sonic.png').convert()
sonic = pygame.transform.scale(sonic, (100, 138))
sonic.set_colorkey((88,88,88))
venom = pygame.image.load('venom.mapa.png').convert()
venom = pygame.transform.scale(venom, (100, 138))
venom.set_colorkey((76,3,112))
yasuo = pygame.image.load("yasuo1.png").convert()
yasuo = pygame.transform.scale(yasuo, (105, 130))
yasuo.set_colorkey((88,88,88))
bowser = pygame.image.load("bowser.pixel.png").convert()
bowser = pygame.transform.scale(bowser, (90, 115))
bowser.set_colorkey(PRETO)
text_surface = score_font.render('Fase 1' , True, VERMELHO)
text_surface2 = score_font.render('Fase 2', True, VERMELHO)
text_surface3 = score_font.render('Fase 3', True, VERMELHO)
text_surface4 = score_font.render('Fase 4', True, VERMELHO)
text_surface5 = score_font.render('Fase 5', True, CINZA)
text_surface = pygame.transform.scale(text_surface, (120, 80))
text_surface2 = pygame.transform.scale(text_surface2, (120, 80))
text_surface3 = pygame.transform.scale(text_surface3, (120, 80))
text_surface4 = pygame.transform.scale(text_surface4, (120, 80))
all_sprites = pygame.sprite.Group()
player = jogador()
all_sprites.add(player)
pygame.mixer.music.play(loops=-1)
run = True
while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
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
    skn.blit(background1,background_rect)
    skn.blit(background,background_rect)
    skn.blit(text_surface,(13,327))
    skn.blit(text_surface2,(350,328))
    skn.blit(text_surface3,(13,100))
    skn.blit(text_surface4,(350,100))
    if 'all' in inventario:
        skn.blit(text_surface5,(13,50))
        skn.blit(text_surface5,(300,50))
    else:
        skn.blit(porta,(175,-10))
    skn.blit(sonic,(360,380))
    skn.blit(venom,(40,380))
    skn.blit(yasuo,(360,150))
    skn.blit(bowser,(40,170))
    all_sprites.update()        
    all_sprites.draw(skn)                       
    pygame.display.flip()


   
