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

def ranking(people, n):
    for i in range(n):
        people[i].calculate()

    people.sort(key=lambda rank: rank.score, reverse=True)

    player1 = pygame.image.load("p1")
    player2 = pygame.image.load("p2")
    player3 = pygame.image.load("p3")
    player4 = pygame.image.load("p4")
    player5 = pygame.image.load("p5")
    player6 = pygame.image.load("p6")
    player7 = pygame.image.load("p7")
    player_empty = pygame.image.load("p_emt")

    """
    for i in range(len(people)):
        print("{0}등 - {1}p : {2}points ".format(i + 1, people[i].player, people[i].score))
    """