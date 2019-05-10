#programa do cursor
import pygame,sys
from pygame.locals import *
import random

#determinar tamanho tela
WIDTH = 480
HEIGHT = 600
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

class Coracao(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("coracao.png").convert_alpha()
        #image.fill(AMARELO)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2 , HEIGHT/2)
        self.x = 0
        self.y = 0
    def update(self):
        self.rect.x = self.x-25
        self.rect.y = self.y-20
#Classe Mob que representa os meteoros
class Mob(pygame.sprite.Sprite):
    
    # Construtor da classe.
    def __init__(self):
        
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        # Carregando a imagem de fundo.
        mob_img = pygame.image.load("Chão colorido.png").convert()
        
        # Diminuindo o tamanho da imagem.
        self.image = pygame.transform.scale(mob_img, (50, 38))
        
        # Deixando transparente.
        self.image.set_colorkey(PRETO)
        
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        
        # Sorteia um lugar inicial em x
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        # Sorteia um lugar inicial em y
        self.rect.y = random.randrange(-100, -40)
        # Sorteia uma velocidade inicial
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(2, 9)
        
        # Melhora a colisão estabelecendo um raio de um circulo
        self.radius = int(self.rect.width * .85 / 2)
        
    # Metodo que atualiza a posição da navinha
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        # Se o meteoro passar do final da tela, volta para cima
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedx = random.randrange(-3, 3)
            self.speedy = random.randrange(2, 6)
            

# initialize pyagme and create window
pygame.init()
pygame.mixer.init()
#screen = pygame.display.set_mode((WIDTH,HEIGHT))
#pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Undertail")
clock = pygame.time.Clock()

skn = pygame.display.set_mode((480,600))
background = pygame.image.load('ChãoLava.png').convert()
background1 = pygame.image.load('Cursor.png').convert()
background_rect = background.get_rect()

all_sprites = pygame.sprite.Group()
player = Jogador()

coracao = Coracao()
all_sprites.add(coracao)
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
    mx,my = pygame.mouse.get_pos()
    if not (mx<84 or mx>396 or my<204 or my>564):
        print("entrou")          
        coracao.x = mx
        coracao.y = my
    else:
        print("fora") 
        
    skn.blit(background, background_rect)
    skn.blit(background1,(72,192))
    #pygame.display.update()
    mobs = pygame.sprite.Group()
    for i in range(1):
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)          
    all_sprites.draw(skn)
      #pygame.display.update()
    pygame.display.flip()
    #updates
    all_sprites.update()

    #gráficos/desenhos
    
    all_sprites.draw(skn)
    # depois de desenhar tudo 
    

pygame.quit()
