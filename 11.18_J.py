import pygame
from pygame.locals import *


if __name__ == '__main__':
    pygame.init()
    chip = pygame.image.load("image/chip.png")
    board = pygame.image.load("image/board.png")
    start_screen = pygame.image.load("image/start.png")
    main_screen = pygame.image.load("image/main.png")
    run = True
    width, height = 960, 720
    screen = pygame.display.set_mode((width, height))
    while run:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False

        screen.blit(start_screen, (0, 0))
        pygame.display.flip()


    pygame.quit()

