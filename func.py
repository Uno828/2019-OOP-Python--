import pygame
import make_class
import time

Black = (50, 50, 50)

locx = [403.024, 202.524, 603.524, 179.978, 336.978, 503.978, 659.978]
locy = [256.374, 256.374, 256.374, 394.752, 394.752, 394.752, 394.752]



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


def auction(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            return 1
        elif event.key == pygame.K_LEFT:
            return 0
    return -1


def endgame(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            return 1
    return 0

def ranking(people, n, screen):
    for i in range(n):
        people[i].calculate()

    people.sort(key=lambda rank: rank.score, reverse=True)

    rank_img = []
    for i in range(3):
        rank_img.append(pygame.image.load("image/p" + str(people[i].player) + "- 큰 결과.png"))
    for i in range(3, n):
        rank_img.append(pygame.image.load("image/p" + str(people[i].player) + "- 작은 결과.png"))
    for i in range(n, 7):
        rank_img.append(pygame.image.load("image/p_emt- 작은 결과.png"))

    for i in range(7):
        screen.blit(rank_img[i], (locx[i], locy[i]))
        pygame.display.flip()


