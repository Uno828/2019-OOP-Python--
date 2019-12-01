import random
import time
import pygame
from func import *

current_player_loc = [90, 426]
current_chip_loc = [181.69, 665]
current_card_loc = [[340.725, 440], [410.903, 440], [480.904, 440], [550.904, 440], [620.904, 440],
                    [690.904, 440], [270.904, 533], [340.725, 533], [410.904, 533], [480.904, 533],
                    [550.904, 533], [620.904, 533], [690.904, 533], [270.904, 625], [340.725, 625],
                    [410.903, 625], [480.904, 625], [550.904, 625], [620.904, 625], [690.904, 625], [0, 0], [0, 0]]
player_loc = [[18.544, 114.832], [18.544, 219.832], [18.544, 320.832], [401.794, 114.832], [401.794, 219.832],
              [401.794, 320.832]]
player_card_loc = [[248.279, 162.888], [248.279, 267.055], [248.279, 377.222], [629.946, 162.888], [629.946, 267.055],
                   [629.946, 377.222]]
current_score_loc = [859.44, 610.25]
show_title_loc = [237, 36]

class base:
    def __init__(self, x, y):
        self.remain_card = x
        self.remain_coin = y

    def image_show(self,image, x, y, screen):
        screen.blit(image, (x, y))

    def card_show(self,card_num, screen):
        card = pygame.image.load("image/" + str(-card_num) + "- 큰 버전.png")
        self.image_show(card, 790, 58, screen)

    def text_show(self,txt, size, x, y, screen):  # 출처: https://devnauts.tistory.com/61 [devnauts]
        fontObj = pygame.font.Font('맑은고딕.ttf', size)  # 현재 디렉토리로부터 폰트 파일을 로딩한다. 텍스트 크기를 size로 한다
        textSurfaceObj = fontObj.render(txt, True, Black)
        # 텍스트 객체를 생성한다. 첫번째 파라미터는 텍스트 내용, 두번째는 Anti-aliasing 사용 여부, 세번째는 텍스트 컬러
        textRectObj = textSurfaceObj.get_rect()  # 텍스트 객체의 출력 위치를 가져온다
        textRectObj.center = (x, y)  # 텍스트 객체의 출력 중심 좌표를 설정한다
        screen.blit(textSurfaceObj, textRectObj)

    def turn_base(self, screen):
        self.text_show(str(self.remain_coin), 50, 853, 386.25, screen)  # 배당된 칩 수
        self.text_show(str(self.remain_card), 50, 857.44, 495.25, screen)  # 남은 카드의 수

class human(base):
    def __init__(self, player, coin, x, y):
        base.__init__(self, x, y)
        self.player = player + 1  # player 몇번째 사람인가?
        self.coin = coin  # 칩의 개수
        self.card = []  # 보유한 카드
        self.score = 0  # 최종 스코어

    def turn_change(self, turn, screen, n):
        if self.player == turn+1:
            main_screen = pygame.image.load("image/ing_v3.png")
            self.image_show(main_screen, 0, 0, screen)
            card_list = []

            for i in self.card:
                card_list.append(pygame.image.load("image/" + str(-i) + "- 작은버전.png"))

            for i in range(len(self.card)):
                self.image_show(card_list[i], current_card_loc[i][0], current_card_loc[i][1], screen)

            player_logo = pygame.image.load("image/p" + str(self.player) + "- 큰 버전.png")
            self.image_show(player_logo, current_player_loc[0], current_player_loc[1], screen)

            self.text_show(str(self.coin), 50, current_chip_loc[0], current_chip_loc[1], screen)
            self.calculate()
            self.text_show(str(self.score), 50, current_score_loc[0], current_score_loc[1], screen)

            self.text_show(str(self.player), 38, show_title_loc[0], show_title_loc[1], screen)

        elif self.player != turn+1:
            num = (self.player-turn-2)%n
            player_logo = pygame.image.load("image/p" + str(self.player) + "- 작은 버전.png")
            self.image_show(player_logo, player_loc[num][0], player_loc[num][1], screen)
            A = ''
            B = ''
            C = ''
            for i in self.card:
                if len(B) > 25:
                    C = C + str(i) + '  '
                elif len(A) > 25:
                    B = B + str(i) + '  '
                else:
                    A = A + str(i) + '  '
            if len(A) <= 25:
                self.text_show(str(A), 18, player_card_loc[num][0], player_card_loc[num][1], screen)
            elif len(B) <= 25:
                self.text_show(str(A), 18, player_card_loc[num][0], player_card_loc[num][1] - 15, screen)
                self.text_show(str(B), 18, player_card_loc[num][0], player_card_loc[num][1] + 15, screen)

            else:
                self.text_show(str(A), 18, player_card_loc[num][0], player_card_loc[num][1] - 30, screen)
                self.text_show(str(B), 18, player_card_loc[num][0], player_card_loc[num][1], screen)
                self.text_show(str(C), 18, player_card_loc[num][0], player_card_loc[num][1] + 30, screen)




    def calculate(self):  # 스코어 계산 과정
        self.card.sort(reverse=True)  # 크기 역순으로 정렬 ex) 8 7 6 5
        self.score = self.coin  # 칩 개수부터 스코어 계산
        back_num = 0  # 연속한 수 체크하는 tmp

        for i in range(len(self.card)):
            if self.card[i] == back_num - 1:
                pass
            else:
                self.score += self.card[i]
            back_num = self.card[i]

