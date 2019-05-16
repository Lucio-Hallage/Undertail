import pygame
pygame.init()

win = pygame.display.set_mode((500,500))

screenWidth = 500

#walkRight = [pygame.image.load("")] 
#walkLeft = [pygame.image.load("")]
bg = pygame.image.load("mapagame.png")
#char = pygame.image.load("")

x = 50
y = 425
width = 64
height = 64
vel = 30

def redrawGameWindow():
    win.fill((0,0,0))
    win.blit(bg, (0, 0))
    
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()       
    



run = True
while run:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:
        x-= vel
    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < 500 - height - vel:
        y += vel
    
    win.blit(bg, (0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()      
    
    redrawGameWindow()        
            
            
            
pygame.quit()

#ainda sem o background e a skin do char
