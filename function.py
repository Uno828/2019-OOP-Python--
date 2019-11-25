import pygame

def num_check(event):
    while True:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_4:
                return 4
            elif event.key == pygame.K_5:
                return 5
            elif event.key == pygame.K_6:
                return 6
            elif event.key == pygame.K_7:
                return 7

def card_add(card_num, loc):
    pass

