import pygame
from sys import exit

pygame.init() #starts pygame 
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('FirstWindow')
clock = pygame.time.Clock()

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60) #not more than 60 loop cycles per sec

    



