# -*- coding: utf-8 -*-
"""
Created on Sat May 18 22:13:57 2019

@author: insper
"""
#Fase5
#programa do cursor
import pygame,sys
from pygame.locals import *
import random
import time

def fase5():
    #determinar tamanho tela
    WIDTH = 480
    HEIGHT = 600
    FPS = 60
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
    
    class Jogador(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((50,50))
            self.rect = self.image.get_rect()
            self.rect.center = (WIDTH/2 , HEIGHT/2)
    
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
    class Chefe(pygame.sprite.Sprite):
        
        # Construtor da classe.
        def __init__(self):
            
            # Construtor da classe pai (Sprite).
            pygame.sprite.Sprite.__init__(self)
            
            # Carregando a imagem de fundo.
            chefe_img = pygame.image.load("genos.png").convert()
            
            # Diminuindo o tamanho da imagem.
            self.image = pygame.transform.scale(chefe_img, (105, 130))
            
            # Deixando transparente.
            self.image.set_colorkey(BRANCO)
            
            # Detalhes sobre o posicionamento.
            self.rect = self.image.get_rect()
            self.rect.x = 240-52.5
            self.rect.y = 185-125
            self.speedx = 5
            # Metodo que atualiza a posição da navinha
        def update(self):
            self.rect.x += self.speedx
            
            
            # Se o meteoro passar do final da tela, volta para cima
            if  self.rect.right > 396:
                    self.speedx=-10
                    
            if self.rect.left < 84:
                    self.speedx=10
                    
                
                
    #Classe Mob que representa os meteoros
    class lucha(pygame.sprite.Sprite):
        
        # Construtor da classe.
        def __init__(self):
            
            # Construtor da classe pai (Sprite).
            pygame.sprite.Sprite.__init__(self)
            
            # Carregando a imagem de fundo.
            mob_img = pygame.image.load("teia.png").convert()
            
            # Diminuindo o tamanho da imagem.
            self.image = pygame.transform.scale(mob_img, (24, 24))
            
            # Deixando transparente.
            self.image.set_colorkey(BRANCO)
            
            # Detalhes sobre o posicionamento.
            self.rect = self.image.get_rect()
            
            # Sorteia um lugar inicial em x
            self.rect.x = random.randrange(84,396)
            # Sorteia um lugar inicial em y
            self.rect.y = 204
            
            # Sorteia uma velocidade inicial
            self.speedx = random.randrange(-3, 3)
            self.speedy = random.randrange(5, 6)
            
            # Melhora a colisão estabelecendo um raio de um circulo
        
            self.radius=10
            
        # Metodo que atualiza a posição da navinha
        def update(self):
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            
            # Se o meteoro passar do final da tela, volta para cima
            if self.rect.top > 564-25 or self.rect.left < 84 or self.rect.right > 396:
                self.rect.x = random.randrange(84,396)
                self.rect.y = 204
                self.speedx = random.randrange(-3, 3)
                self.speedy = random.randrange(5, 6)
    class rings(pygame.sprite.Sprite):
        
        # Construtor da classe.
        def __init__(self):
            
            # Construtor da classe pai (Sprite).
            pygame.sprite.Sprite.__init__(self)
            
            # Carregando a imagem de fundo.
            mob_img = pygame.image.load("sonic rings.png").convert()
            
            # Diminuindo o tamanho da imagem.
            self.image = pygame.transform.scale(mob_img, (24, 24))
            
            # Deixando transparente.
            self.image.set_colorkey(PRETO)
            
            # Detalhes sobre o posicionamento.
            self.rect = self.image.get_rect()
            
            # Sorteia um lugar inicial em x
            self.rect.x = random.randrange(84,396)
            # Sorteia um lugar inicial em y
            self.rect.y = 204
            
            # Sorteia uma velocidade inicial
            self.speedx = random.randrange(-3, 3)
            self.speedy = random.randrange(5, 6)
            
            # Melhora a colisão estabelecendo um raio de um circulo
            self.radius=10
           
        # Metodo que atualiza a posição da navinha
        def update(self):
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            mx,my = pygame.mouse.get_pos()
            if mx<self.rect.x:
                self.speedx-=0.2
            if mx>self.rect.x:
                self.speedx+=0.2   
                    
            # Se o meteoro passar do final da tela, volta para cima
            if self.rect.top > 564-25 or self.rect.left < 84 or self.rect.right > 396:
                self.rect.x = random.randrange(84,396)
                self.rect.y = 204
                self.speedx = 0
                self.speedy = random.randrange(5, 6)    
    class tornado(pygame.sprite.Sprite):
        
        # Construtor da classe.
        def __init__(self):
            
            # Construtor da classe pai (Sprite).
            pygame.sprite.Sprite.__init__(self)
            
            # Carregando a imagem de fundo.
            mob_img = pygame.image.load("tornado.jpg").convert()
            
            # Diminuindo o tamanho da imagem.
            self.image = pygame.transform.scale(mob_img, (24, 24))
            
            # Deixando transparente.
            self.image.set_colorkey(PRETO)
            
            # Detalhes sobre o posicionamento.
            self.rect = self.image.get_rect()
            
            # Sorteia um lugar inicial em x
            self.rect.x = 380
            self.rect.y = random.randrange(204,539)
            
            # Sorteia uma velocidade inicial
            self.speedx = 0
            self.speedy =0
            
            # Melhora a colisão estabelecendo um raio de um circulo
            
            self.radius=10
            
        # Metodo que atualiza a posição da navinha
        def update(self):
            self.rect.x += self.speedx         
            self.rect.y += self.speedy
            mx,my = pygame.mouse.get_pos()
            if mx<self.rect.x:
                self.speedx-=0.2
            if mx>self.rect.x:
                self.speedx+=0.2
            if my<self.rect.y:
                self.speedy-=0.2
            if my>self.rect.y:
                self.speedy+=0.2
            # Se o meteoro passar do final da tela, volta para cima
            if self.rect.top > 564-25 or self.rect.left < 84 or self.rect.right > 396 or self.rect.y<204:
                self.rect.x = 370
                self.rect.y = random.randrange(204,539)
                self.speedx = 0
                self.speedy = 0
    class mario(pygame.sprite.Sprite):
        
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
            self.speedx = random.randrange(3,6)
            self.speedy = 0
            
            # Melhora a colisão estabelecendo um raio de um circulo
            self.radius=12

        # Metodo que atualiza a posição da navinha
    
        def update(self):
            self.rect.x += self.speedx
    
            # Se o meteoro passar do final da tela, volta para cima
    
            if self.rect.left < 80 or self.rect.right > 396:
                self.rect.x = 81
                self.rect.y = random.randrange(210,560)
                self.speedx = random.randrange(3, 6)
                self.rect.x += self.speedx
    
    def init_screen(screen):
        # Variável para o ajuste de velocidade
        clock = pygame.time.Clock()
    
        # Carrega o fundo da tela inicial
        background1 = pygame.image.load('Cursor.png').convert()
        text_surface = score_font.render("FASE 5" , True, BRANCO)
        text_surface2 = score_font.render("GENOS" , True, AZUL)
        text_surface3 = score_font.render("ENTRE NA TELA PRETA" , True, BRANCO)
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
                if not (mx<95 or mx>392 or my<210 or my>560):
                    running=False
                    coracao.x = mx
                    coracao.y = my    
            # A cada loop, redesenha o fundo e os sprites
            screen.blit(bg_init,background_rect)
            screen.blit(background1,(72,192))
            screen.blit(text_surface,(80,30))
            screen.blit(text_surface2,(260,70))
            screen.blit(text_surface1,(10,150))
    
            # Depois de desenhar tudo, inverte o display.
            pygame.display.flip()
            all_sprites.update()
    
    def end_screen(skn,c,t):
        if c>t:
            t=c
        if 'Fase1' not in inventario:
            text_surface = score_font.render("GAME OVER" , True, PRETO)
            text_surface1 = score_font.render("Pontuação Atual:", True, PRETO)
            text_surface2 = score_font.render("Recorde Atual:", True, PRETO)
            text_surface3 = score_font.render("{0} segundos".format(int(c)) , True, PRETO)
            text_surface4 = score_font.render("{0} segundos".format(int(t)) , True, PRETO)
            
        else:
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
            skn.blit(bg_end,background_rect)
            skn.blit(text_surface,(72,192))
            if 'Fase1' not in inventario:
                skn.blit(text_surface1,(10,252))
                skn.blit(text_surface3,(10,302))
                skn.blit(text_surface2,(10,362))
                skn.blit(text_surface4,(10,412))
            all_sprites.draw(skn)
            # Depois de desenhar tudo, inverte o display.
            pygame.display.flip()
        return t
    
    
            
            
    
   
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Undertail")
    clock = pygame.time.Clock()
    
    skn = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.mixer.music.load('cyborgue.mpeg')
    pygame.mixer.music.set_volume(2)
    backgroun = pygame.image.load('bgtec.jpg').convert()
    background = pygame.transform.scale(backgroun, (480, 600))
    background1 = pygame.image.load('Cursor.png').convert()
    bg_init = pygame.image.load("genosinit.jpg").convert()
    bg_init = pygame.transform.scale(bg_init, (480, 650))
    bg_end = pygame.image.load("genos_end.jpg").convert()
    bg_end = pygame.transform.scale(bg_end, (480, 600))
    background_rect = background.get_rect()
    gameover=True
    score_font=pygame.font.Font("PressStart2P.ttf", 28)
    t=0
    pygame.mixer.music.play(loops=-1)
    try:
        while gameover:
            
            all_sprites = pygame.sprite.Group()
            coracao = Coracao()
            all_sprites.add(coracao)
            init_screen(skn)
            chefe = Chefe()
            all_sprites.add(chefe)
            mobs = pygame.sprite.Group()
            m=tornado()
            all_sprites.add(m)
            mobs.add(m)
            for i in range(3):
                m = lucha()
                all_sprites.add(m)
                mobs.add(m)
            for i in range(2):
                m = rings()
                all_sprites.add(m)
                mobs.add(m)
            for i in range(2):
                m = mario()
                all_sprites.add(m)
                mobs.add(m)
            c = 1
            
            # Loop do jogo
        
            running = True
            
            while running:
                clock.tick(FPS)
                c -=1/60
                if c <= 0:
                    running = False
                    inventario.append('Fase1')
                    gameover=False
                
                for event in pygame.event.get():
                  
                    if event.type == pygame.QUIT:
                        running = False
                        gameover=False
                
                mx,my = pygame.mouse.get_pos()
                if not (mx<95 or mx>392 or my<210 or my>560):
                             
                    coracao.x = mx
                    coracao.y = my
                
                # Verifica se houve colisão entre nave e meteoro
                hits = pygame.sprite.spritecollide(coracao, mobs, False, pygame.sprite.collide_circle)
                if hits:
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
                  
                pygame.display.flip()
              
                all_sprites.update()
                
            for mobs in all_sprites:
                mobs.kill()
            t=end_screen(skn,15-c,t)      
    finally:     
        pygame.quit()
fase5()