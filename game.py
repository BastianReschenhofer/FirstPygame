import pygame
from sys import exit

pygame.init() #starts pygame 
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('FirstWindow')
clock = pygame.time.Clock()
test_fond = pygame.font.Font('graphics\Fonts\PixelFont.ttf', 50)

sky_surface = pygame.image.load('graphics\Sky.png')
ground_surface = pygame.image.load('graphics\Ground.png')
text_surface = test_fond.render('TestTxT', False, 'Black')


#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    screen.blit(sky_surface, (0,0)) # blit -> block immage transfer
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface,(300,50))
    

    pygame.display.update()
    clock.tick(60) #not more than 60 loop cycles per sec



