import pygame
import time
from make_class import *
import func

if __name__ == '__main__':

    pygame.init()
    start_screen = pygame.image.load("image/Title_v1.png")
    rule_screen = pygame.image.load("image/Rule_v1.png")
    main_screen = pygame.image.load("image/ing_v3.png")
    result_screen = pygame.image.load("image/result_v4.png")
    warning_1 = pygame.image.load("image/warning_1.png")
    warning_2 = pygame.image.load("image/warning_2.png")
    wait_1_screen = pygame.image.load("image/wait_1.png")
    wait_2_screen = pygame.image.load("image/wait_2.png")
    wait_3_screen = pygame.image.load("image/wait_3.png")

    run = True
    width, height = 960, 720
    screen = pygame.display.set_mode((width, height))

    n = None
    flag = False

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if not flag:
            screen.blit(start_screen, (0, 0))
            pygame.display.flip()
            pygame.time.delay(2000)

            flag = True



        screen.blit(rule_screen, (0, 0))
        pygame.display.flip()

        people = []  # 본격적인 사람의 수

        if n != None:
            n = n
        else:
            n = num_check(event)

        if n is not None:
            n = int(n)
            for i in range(4):
                loading =  pygame.image.load("image/loading_"+str(i+1)+".png")
                screen.blit(loading, (0,0))
                pygame.display.flip()
                pygame.time.delay(1000)

            screen.blit(main_screen, (0, 0))
            pygame.display.flip()
            for i in range(n):  # n명 가정, 0~n-1
                people.append(human(i, 9, 0, 0))

            deck = []  # 턴에 결정될 카드
            for i in range(-35, -2):  # 현재 카드가 -3 ~ -35까지 모두 append
                deck.append(i)

            turn = 0  # 0 ~ n-1     # 몇번째 플레이어의 순서인가

            while len(deck):  # 카드가 더 이상 남아있지 않을때까지
                num = random.choice(deck)  # 현재 카드 결정
                func.card_show(num, screen)  # 결정된 현재 숫자를 화면에 띄워 주는 함수

                chk = -1  # 1은 패스, 0은 낙찰
                stacked_coin = 0  # 현재 카드에 쌓인 칩의 개수
                turn -= 1
                while chk:  # 낙찰받는 사람 결정
                    turn += 1  # 다음 사람으로 넘기기
                    turn = turn % n  # 계산

                    turn_change(turn, people, len(deck), stacked_coin, screen, n)
                    func.card_show(num, screen)

                    if not people[turn].coin:  # 칩없으면 바로 끝
                        screen.blit(warning_1, (44.5,212.5))
                        pygame.display.flip()
                        pygame.time.delay(2000)
                        break

                    while not (chk == 0 or chk == 1):
                        for event in pygame.event.get():  # auction 함수를 통해 낙찰 여부 입력
                            if chk != -1:
                                chk = chk
                            else:
                                chk = func.auction(event)

                    if chk:  # chk가 1일때, 즉 패스한 경우
                        stacked_coin += 1  # 패스하면, 칩 개수 올리고
                        people[turn].coin -= 1  # 가진 칩 줄이기
                        chk = -1
                        screen.blit(wait_3_screen, (0, 0))
                        pygame.display.flip()
                        pygame.time.delay(1000)
                        screen.blit(wait_2_screen, (0, 0))
                        pygame.display.flip()
                        pygame.time.delay(1000)
                        screen.blit(wait_1_screen, (0, 0))
                        pygame.display.flip()
                        pygame.time.delay(1000)

                # chk가 0일 때, 즉 숫자 카드를 낙찰받은 경우
                if len(people[turn].card)>=20:
                    screen.blit(warning_2, (44.5,166))
                    pygame.display.flip()
                    res = 0
                    while not res == 1:
                        for event in pygame.event.get():
                            if res != 0:
                                res = res
                            else:
                                res = func.endgame(event)
                    run = False
                    break

                people[turn].coin += stacked_coin  # 칩 개수만큼 올렺고
                people[turn].card.append(num)  # 갖고 있는 카드에 추가
                deck.remove(num)  # 방금 카드 지워버리기
                # 여기서 띄우기 - 피플 클래스에 추가해서 하자, 휴먼 클래스에서는 현재 보유 카드 띄우기


            screen.blit(result_screen, (0, 0))
            pygame.display.flip()

            ranking(people, n, screen)
            # pygame.time.delay(2000)

            res = 0
            while not res == 1:
                for event in pygame.event.get():
                    if res != 0:
                        res = res
                    else:
                        res = func.endgame(event)
            run = False
    pygame.quit()