#programa do cursor
import pygame,sys
from pygame.locals import *
import random

#determinar tamanho tela
WIDTH = 480
HEIGHT = 600
FPS = 60


#determinar cores
PRETO = (0,0,0)
AMARELO = (244, 209, 66)
VERMELHO = (255, 0, 0)


# definindo os personagens

class Jogador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))  #TROCAR POR IMAGEM PLAYER
        #image.fill(AMARELO)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2 , HEIGHT/2)

class Coracao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        cor_img = pygame.image.load("coracao.png").convert_alpha()
        self.image = pygame.transform.scale(cor_img, (12,12))
        #image.fill(AMARELO)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2 , HEIGHT/2)
        self.x = 0
        self.y = 0
        self.radius = 6
        pygame.draw.circle(self.image,VERMELHO,self.rect.center,self.radius)
    def update(self):
        self.rect.x = self.x-10
        self.rect.y = self.y-10
class Chefe(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        chefe_img = pygame.image.load("venom.png").convert()
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(chefe_img, (105, 130))
        
        # Deixando transparente.
        self.image.set_colorkey(PRETO)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        self.rect.x = 240-52.5
        self.rect.y = 192-125
        self.speedx = 5
        # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        
        
        # Se o meteoro passar do final da tela, volta para cima
        if  self.rect.right > 396:
                self.speedx=-5
                print('boa')
        if self.rect.left < 84:
                self.speedx=5
                print('iuuuhuuulllll')
            
            
#Classe Mob que representa os meteoros
class Mob(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        mob_img = pygame.image.load("luchalibre.png").convert()
        
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
        self.speedy = random.randrange(3, 6)
        
        # Melhora a colisão estabelecendo um raio de um circulo
        #self.radius = int(self.rect.width * .85 / 2)
        self.radius=12
        pygame.draw.circle(self.image,VERMELHO,self.rect.center,self.radius)
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # Se o meteoro passar do final da tela, volta para cima
        if self.rect.top > 564-25 or self.rect.left < 84 or self.rect.right > 396:
            self.rect.x = random.randrange(84,396)
            self.rect.y = 204
            self.speedx = random.randrange(-3, 3)
            self.speedy = random.randrange(3, 6)
            

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
#screen = pygame.display.set_mode((WIDTH,HEIGHT))
#pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Undertail")
clock = pygame.time.Clock()

skn = pygame.display.set_mode((480,600))
pygame.mixer.music.load('naruto.mpeg')
pygame.mixer.music.set_volume(2)
background = pygame.image.load('Chãolava.png').convert()
background1 = pygame.image.load('Cursor.png').convert()
#background2 = pygame.image.load('venom.png').convert()
background_rect = background.get_rect()
gameover=True
all_sprites = pygame.sprite.Group()
coracao = Coracao()
all_sprites.add(coracao)
#while gameover:
    #clock.tick(FPS)
    #mx,my = pygame.mouse.get_pos()
    #if not (mx<90 or mx>392 or my<210 or my>560):
        #gameover=False

chefe = pygame.sprite.Group()
all_sprites.add(Chefe())
chefe.add(Chefe())  

#all_sprites.add(player)
mobs = pygame.sprite.Group()
for i in range(10):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)  
# Loop do jogo
pygame.mixer.music.play(loops=-1)
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
    
    mx,my = pygame.mouse.get_pos()
    if not (mx<90 or mx>392 or my<210 or my>560):
                 
        coracao.x = mx
        coracao.y = my
    
    # Verifica se houve colisão entre nave e meteoro
    hits = pygame.sprite.spritecollide(coracao, mobs, False, pygame.sprite.collide_circle)
    if hits:
            running = False
        
    skn.blit(background, background_rect)
    skn.blit(background1,(72,192))
    #background2.fill(PRETO)
    #skn.blit(background2,(72,192))
    #pygame.display.update()
            
    all_sprites.draw(skn)
      #pygame.display.update()
    pygame.display.flip()
    #updates
    all_sprites.update()

    #gráficos/desenhos
    
    all_sprites.draw(skn)
    # depois de desenhar tudo 
    

pygame.quit()
