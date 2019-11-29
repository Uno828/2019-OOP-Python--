import random
import time
import pygame
from function import *

class human:
    def __init__(self, player, coin):
        self.player = player + 1        # player 몇번째 사람인가? ->
        self.coin = coin        # 칩의 개수
        self.card = []          # 보유한 카드
        self.score = 0          # 최종 스코어
        

    def calculate(self):        # 스코어 계산 과정
        self.card.sort(reverse=True)    # 크기 역순으로 정렬 ex) 8 7 6 5
        self.score = self.coin          # 칩 개수부터 스코어 계산
        back_num = 0                    # 연속한 수 체크하는 tmp

        for i in range(len(self.card)):
            if self.card[i] == back_num - 1:
                pass
            else:
                self.score += self.card[i]
            back_num = self.card[i]

if __name__ == '__main__':

    pygame.init()
    chip = pygame.image.load("image/chip.png")
    board = pygame.image.load("image/board.png")
    start_screen = pygame.image.load("image/start.png")
    main_screen = pygame.image.load("image/main.png")
    run = True
    width, height = 960, 720
    screen = pygame.display.set_mode((width, height))

    n = None

    while run:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False

        screen.blit(start_screen, (0, 0))
        pygame.display.flip()

        people = [] # 본격적인 사람의 수

        n = n if n != None else num_check(event)

        if n is not None:
            n = int(n)
            print(n)
            screen.blit(main_screen,(0,0))
            pygame.display.flip()
            for i in range(n):  # n명 가정, 0~n-1
                people.append(human(i, 20))

            deck = []   # 턴에 결정될 카드
            for i in range(-35, -2):    # 현재 카드가 -3 ~ -35까지 모두 append
                deck.append(i)

            turn = 0  # 0 ~ n-1     # 몇번째 플레이어의 순서인가

            while len(deck) and False:  # 카드가 더 이상 남아있지 않을때까지
                num = random.choice(deck) # 현재 카드 결정
                card_show(num)#결정된 현재 숫자를 화면에 띄워 주는 함수

                chk = 1  # 1은 패스, 0은 낙찰
                stacked_coin = 0    # 현재 카드에 쌓인 칩의 개수
                turn -= 1
                while chk:  # 낙찰받는 사람 결정
                    turn += 1  # 다음 사람으로 넘기기
                    turn = turn % n  # 계산
                    if not people[turn].coin:  # 칩없으면 바로 끝
                        print("%dp님, 당신은 칩이 없습니다." % (turn + 1), end=' ')
                        break
                    while not (chk == 0 or chk == 1):
                        pass # 왼쪽:0, 매수|오른쪽:1, 패스


                    if chk:
                        stacked_coin += 1  # 패스하면, 칩 개수 올리고
                        people[turn].coin -= 1  # 가진 칩 줄이기
                print("%dp님, 낙찰되었습니다." % (turn + 1))  # 낙찰된 상황
                people[turn].coin += stacked_coin  # 칩 개수만큼 올렺고
                people[turn].card.append(num)  # 갖고 있는 카드에 추가
                deck.remove(num)  # 방금 카드 지워버리기

            ranking(people, n)

    pygame.quit()