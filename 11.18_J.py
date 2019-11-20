import pygame
from pygame.locals import *

white = (255, 255, 255)


if __name__ == '__main__':
    pygame.init()
    chip = pygame.image.load("image/chip.png")
    board = pygame.image.load("image/board.png")
    start_screen = pygame.image.load("image/시작화면.png")
    run = True
    while run:
        width, height = 1280, 960
        screen = pygame.display.set_mode((width, height))
        screen.fill(white)

        screen.blit(start_screen,(170,126))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:

        key = pygame.key.get_pressed()
        if key == :
            pygame.display.flip()

