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

    pn_1 = []
    pn_2 = []
    pn_3 = []
    pn_4 = []

    for i in range(1,8):
        pn_1.append( pygame.image.load("p"+str(i+1)+"- 작은 결과.png"))

    for i in range(1,8):
        pn_1.append( pygame.image.load("p"+str(i+1)+"- 작은 결과.png"))

    for i in range(1,8):
        pn_1.append( pygame.image.load("p"+str(i+1)+"- 작은 결과.png"))

    for i in range(1,8):
        pn_1.append( pygame.image.load("p"+str(i+1)+"- 작은 결과.png"))


    p1 = pygame.image.load("p1")
    p2 = pygame.image.load("p2")
    p3 = pygame.image.load("p3")
    p4 = pygame.image.load("p4")
    p5 = pygame.image.load("p5")
    p6 = pygame.image.load("p6")
    p7 = pygame.image.load("p7")
    player_empty = pygame.image.load("p_emt")

    """
    for i in range(len(people)):
        print("{0}등 - {1}p : {2}points ".format(i + 1, people[i].player, people[i].score))
    """
