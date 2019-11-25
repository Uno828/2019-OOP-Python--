import pygame

def num_check():
    while True:
        key = pygame.key.get_pressed()
        if key[pygame.K_4]:
            return 4
        elif key[pygame.K_5]:
            return 5
        elif key[pygame.K_6]:
            return 6
        elif key[pygame.K_7]:
            return 7

def card_add(card_num, loc):
    pass

def