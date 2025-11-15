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

snowman_surface_orig = pygame.image.load('graphics\Snowman.png').convert_alpha()
snowman_width, snowman_height = snowman_surface_orig.get_size()
snowman_surface = pygame.transform.scale(snowman_surface_orig,(snowman_width * 4, snowman_height * 4))
snowman_x_pos = 625
snowman_y_pos = 200
snowman_dir = True

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    
    screen.blit(sky_surface, (0,0)) # blit -> block immage transfer
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface,(300,50))
    if(snowman_x_pos == 600): snowman_dir = False
    if(snowman_x_pos == 650): snowman_dir = True
    if(snowman_dir): snowman_x_pos -= 1 
    else: snowman_x_pos +=1


    screen.blit(snowman_surface,(snowman_x_pos,snowman_y_pos))
    

    pygame.display.update()
    clock.tick(60) #not more than 60 loop cycles per sec



