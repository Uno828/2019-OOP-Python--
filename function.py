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

def card_show(card_num,screen): #화면에 선택된 카드를 띄워주는 함수
    card = pygame.image.load("image/"+str(-card_num)+".png")
    screen.blit(card, (784, 58))
    pygame.display.flip()

def auction(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            return 0
        elif event.key == pygame.K_RIGHT:
            return 1
    return None

