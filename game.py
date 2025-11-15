import pygame
from sys import exit

pygame.init() #starts pygame 
screen = pygame.display.set_mode((800, 400))

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()

    



