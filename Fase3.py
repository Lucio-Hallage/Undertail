# -*- coding: utf-8 -*-
"""
Created on Tue May 14 22:09:11 2019

@author: insper
"""
#FASE3-bowser
import pygame,sys
from pygame.locals import *
import random
import time

def fase3():
    #determinar tamanho tela
    WIDTH = 480
    HEIGHT = 600
    FPS = 60
    #FONT_NAME = 'courier'
    #HS_FILE = "highscore.txt"
    inventario=[]
    
    #determinar cores
    PRETO = (0,0,0)
    AMARELO = (244, 209, 66)
    VERMELHO = (255, 0, 0)
    CINZA = (88,88,88)
    BRANCO=(255,255,255)
    VERDE = (0, 255, 0)
    AZUL=(0,0,255)
    
    # definindo os personagens
    
    class Coracao(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            cor_img = pygame.image.load("coracao.png").convert_alpha()
            self.image = pygame.transform.scale(cor_img, (12,12))
    
            self.rect = self.image.get_rect()
            self.x=0
            self.y=0
            self.radius = 6
        def update(self):
            self.rect.x = self.x-10
            self.rect.y = self.y-10
    
    
    class Bowser(pygame.sprite.Sprite):
        
        # Construtor da classe.
        def __init__(self):
            
            # Construtor da classe pai (Sprite).
            pygame.sprite.Sprite.__init__(self)
            
            # Carregando a imagem de fundo.
            bowser_img = pygame.image.load("bowser.pixel.png").convert()
            
            # Diminuindo o tamanho da imagem.
            self.image = pygame.transform.scale(bowser_img, (90, 115))
            
            # Deixando transparente.
            self.image.set_colorkey(PRETO)
            
            # Detalhes sobre o posicionamento.
            self.rect = self.image.get_rect()
            self.rect.x = 240-52.5
            self.rect.y = 200-125
            self.speedx = 2
    
            # Metodo que atualiza a posição da navinha
        def update(self):
            self.rect.x += self.speedx
            
            
            # Se o meteoro passar do final da tela, volta para cima
            if  self.rect.right > 396:
                    self.speedx=-2
                    
            if self.rect.left < 84:
                    self.speedx=2
                    
                
                
    #Classe Mob que representa os meteoros
    class Mob(pygame.sprite.Sprite):
        
        # Construtor da classe.
        def __init__(self):
            
            # Construtor da classe pai (Sprite).
            pygame.sprite.Sprite.__init__(self)
            
            # Carregando a imagem de fundo.
            mob_img = pygame.image.load("bulletmario.jpg").convert()
            
            # Diminuindo o tamanho da imagem.
            self.image = pygame.transform.scale(mob_img, (35, 24))
            
            # Deixando transparente.
            self.image.set_colorkey(CINZA)
            
            # Detalhes sobre o posicionamento.
            self.rect = self.image.get_rect()
            
            
            # Sorteia um lugar inicial em x
            self.rect.x = 81
            # Sorteia um lugar inicial em y
            self.rect.y = random.randrange(210,560)
            
            # Sorteia uma velocidade inicial
            self.speedx = random.randrange(1,4)
            self.speedy = 0
            
            # Melhora a colisão estabelecendo um raio de um circulo
            #self.radius = int(self.rect.width * .85 / 2)
            self.radius=12
            #pygame.draw.circle(self.image,VERMELHO,self.rect.center,self.radius)
        # Metodo que atualiza a posição da navinha
    
        def update(self):
            self.rect.x += self.speedx
    
            # Se o meteoro passar do final da tela, volta para cima
    
            if self.rect.left < 80 or self.rect.right > 396:
                self.rect.x = 81
                self.rect.y = random.randrange(210,560)
                self.speedx = random.randrange(2, 6)
                self.rect.x += self.speedx
    
    #Classe Mob que representa os meteoros
    class MobInvertido(pygame.sprite.Sprite):
        
        # Construtor da classe.
        def __init__(self):
            
            # Construtor da classe pai (Sprite).
            pygame.sprite.Sprite.__init__(self)
            
            # Carregando a imagem de fundo.
            mob_img = pygame.image.load("bulletmarioincer.jpg").convert()
            
            # Diminuindo o tamanho da imagem.
            self.image = pygame.transform.scale(mob_img, (35, 24))
            
            # Deixando transparente.
            self.image.set_colorkey(CINZA)
            
            # Detalhes sobre o posicionamento.
            self.rect = self.image.get_rect()
            self.rect = self.image.get_rect()
            
            # Sorteia um lugar inicial em x
            self.rect.x = 362
            # Sorteia um lugar inicial em y
            self.rect.y = random.randrange(210,560)
            
            # Sorteia uma velocidade inicial
            self.speedx = random.randrange(-4,-1)
            self.speedy = 0
            
            # Melhora a colisão estabelecendo um raio de um circulo
            #self.radius = int(self.rect.width * .85 / 2)
            self.radius=12
            #pygame.draw.circle(self.image,VERMELHO,self.rect.center,self.radius)
        # Metodo que atualiza a posição da navinha
    
        def update(self):
            self.rect.x += self.speedx
    
            # Se o meteoro passar do final da tela, volta para cima
    
            if self.rect.left < 84 or self.rect.right > 396:
                self.rect.x = 362
                self.rect.y = random.randrange(210,560)
                self.speedx = random.randrange(-4, -1)
                
    
    def text_objects(text, font):
        textSurface = font.render(text, True, PRETO)
        return textSurface, textSurface.get_rect()
    
     #botão
    def button(msg,x,y,w,h,ic,ac,action=None):
    
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
    
        if x + y > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(skn, ac, (x,y,w,h))
    
            if click[0] == 1 and action !=None:
                action()
    
        else:
            pygame.draw.rect(skn, ic, (x,y,w,h))
    
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        skn.blit(textSurf, textRect)
                
    def init_screen(screen):
        # Variável para o ajuste de velocidade
        clock = pygame.time.Clock()
    
        # Carrega o fundo da tela inicial
        background1 = pygame.image.load('Cursor.png').convert()
        text_surface = score_font.render("FASE 3" , True, PRETO)
        text_surface2 = score_font.render("BOWSER" , True, AMARELO)
        text_surface3 = score_font.render("ENTRE NA TELA PRETA" , True, PRETO)
        text_surface1= pygame.transform.scale(text_surface3, (460, 40))
    
        running = True
        while running:
            
            # Ajusta a velocidade do jogo.
            clock.tick(FPS)
            
            # Processa os eventos (mouse, teclado, botão, etc).
            for event in pygame.event.get():
                # Verifica se foi fechado.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    running = False
                mx,my = pygame.mouse.get_pos()
                if not (mx<90 or mx>392 or my<210 or my>560):
                    running=False
                    coracao.x = mx
                    coracao.y = my    
            # A cada loop, redesenha o fundo e os sprites
            screen.fill(AZUL)
            screen.blit(background1,(72,192))
            screen.blit(text_surface,(80,30))
            screen.blit(text_surface2,(260,70))
            screen.blit(text_surface1,(10,150))
    
            # Depois de desenhar tudo, inverte o display.
            pygame.display.flip()
            all_sprites.update()
    
    def end_screen(skn,c,t,inventario):
        print(inventario)
        if c>t:
            t=c
        if 'Fase3' not in inventario:
            
            gameoversound.play()
            text_surface = score_font.render("GAME OVER" , True, PRETO)
            text_surface1 = score_font.render("Pontuação Atual:", True, PRETO)
            text_surface2 = score_font.render("Recorde Atual:", True, PRETO)
            text_surface3 = score_font.render("{0} segundos".format(int(c)) , True, PRETO)
            text_surface4 = score_font.render("{0} segundos".format(int(t)) , True, PRETO)
            restart = button("RESTART",150,450,100,50,VERMELHO,PRETO,init_screen) 
            
        else:
            
            pygame.mixer.music.pause()
            winsound.play()
            text_surface = score_font.render("Você Ganhou" , True, PRETO)
        running = True
    
        while running:
            
            # Ajusta a velocidade do jogo.
            clock.tick(FPS)
            
            # Processa os eventos (mouse, teclado, botão, etc).
            for event in pygame.event.get():
                # Verifica se foi fechado.
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    running = False
    
                if event.type == pygame.KEYUP:
                    
                    running = False
                        
            # A cada loop, redesenha o fundo e os sprites
            skn.fill(AMARELO)
            skn.blit(text_surface,(72,192))
            if 'Fase3' not in inventario:
                skn.blit(text_surface1,(10,252))
                skn.blit(text_surface3,(10,302))
                skn.blit(text_surface2,(10,362))
                skn.blit(text_surface4,(10,412))
            all_sprites.draw(skn)
            # Depois de desenhar tudo, inverte o display.
            pygame.display.flip()
        return t
    
            
            
    # initialize pygame and create window
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Undertail")
    clock = pygame.time.Clock()
    
    winsound = pygame.mixer.Sound('mariowin.wav')
    skn = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.mixer.music.load('mariotheme.wav.wav')
    pygame.mixer.music.set_volume(2)
    boom=pygame.mixer.Sound('expl6.wav') 
    gameoversound = pygame.mixer.Sound('GAMEOVER.wav')
    mariobackground = pygame.image.load('mario.background.png').convert()
    background=pygame.transform.scale(mariobackground, (480, 600))
    bg_end = pygame.image.load("gameover.jpg").convert()
    bg_end = pygame.transform.scale(bg_end, (480, 200))
    background1 = pygame.image.load('Cursor.png').convert()
    background_rect = background.get_rect()
    score_font=pygame.font.Font("PressStart2P.ttf", 28)
    gameover=True
    t=0
    
    
    
    try:
        while 'Fase3' not in inventario:
            
            all_sprites = pygame.sprite.Group()
            coracao = Coracao()
            all_sprites.add(coracao)
            init_screen(skn)
            bowser = pygame.sprite.Group()
            all_sprites.add(Bowser())
            bowser.add(Bowser())  
            mobs = pygame.sprite.Group()
            mobsi = pygame.sprite.Group()
            #all_sprites.add(player)
            for i in range(3):
                m = Mob()
                all_sprites.add(m)
                mobs.add(m)
                minv =MobInvertido()
                all_sprites.add(minv)
                mobsi.add(minv)
                
            c = 60
            
            # Loop do jogo
            pygame.mixer.music.play()
            running = True
            
            while running:
                clock.tick(FPS)
                c -=1/60
                if c <= 0:
                    running = False
                    inventario.append('Fase3')
                    
                
                for event in pygame.event.get():
                    #check for closing window
                    if event.type == pygame.QUIT:
                        running = False
                        gameover=False
                
                mx,my = pygame.mouse.get_pos()
                if not (mx<95 or mx>392 or my<210 or my>560):
                             
                    coracao.x = mx
                    coracao.y = my
                
                # Verifica se houve colisão entre nave e meteoro
        
                hits = pygame.sprite.groupcollide(mobsi, mobs,True,True)
    
                for hit in hits:
                    boom.play()
                    m = Mob()
                    minv =MobInvertido()
                    all_sprites.add(m)
                    mobs.add(m)
                    all_sprites.add(minv)
                    mobsi.add(minv)
    
                hits1 = pygame.sprite.spritecollide(coracao, mobs, False, pygame.sprite.collide_circle)
                hits2 = pygame.sprite.spritecollide(coracao, mobsi, False, pygame.sprite.collide_circle)
                if hits1 or hits2:
                    pygame.mixer.music.pause()
                    boom.play()
                    running = False
                    time.sleep(1)
    
                   
                                
                skn.blit(background, background_rect)
                skn.blit(background1,(72,192))
                text_surface = score_font.render("Sobreviva Por" , True, BRANCO)
                text_surface2 = score_font.render(" {0} Segundos".format(int(c)), True, BRANCO)
                text_rect = text_surface.get_rect()
                text_rect.midtop = (WIDTH / 2,  10)
                skn.blit(text_surface, text_rect)
                skn.blit(text_surface2, (70,  50))
                        
                all_sprites.draw(skn)
                  #pygame.display.update()
                pygame.display.flip()
                #updates
                all_sprites.update()
              
                
                # depois de desenhar tudo
            #chefe.kill()
        
            
    
            for mobs in all_sprites:
                mobs.kill()
            t=end_screen(skn,60-c,t,inventario) 
            
        
    finally:     
        if c<=0:
            return 'Fase3'
        else:
            pygame.quit()

