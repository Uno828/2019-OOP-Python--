import pygame

def num_check(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_4:
            return 4
        elif event.key == pygame.K_5:
            return 5
        elif event.key == pygame.K_6:
            return 6
        elif event.key == pygame.K_7:
            return 7

    return None

def card_show(card_num): #화면에 선택된 카드를 띄워주는 함수
    pass
