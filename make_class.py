import random
import time
import pygame
from func import *


class human:
    def __init__(self, player, coin):
        self.player = player + 1  # player 몇번째 사람인가? ->
        self.coin = coin  # 칩의 개수
        self.card = []  # 보유한 카드
        self.score = 0  # 최종 스코어

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
