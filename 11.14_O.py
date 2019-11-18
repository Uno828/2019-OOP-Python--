import random


class human:
    def __init__(self, player, coin):
        self.player = player + 1
        self.coin = coin
        self.card = []
        self.score = 0


def rule():
    print("1) 본 게임은 1p ~ np 순서대로 진행되며 미리 순서를 정해주세요.")
    print("2) -3 ~ -35 의 숫자를 모두 경매하며 각 턴마다 랜덤한 숫자로 진행됩니다.")
    print("3) 개인은 모두 20개의 칩을 갖고 시작하며 숫자를 패스할시에는 칩을 하나씩 소모하여 숫자에 쌓습니다.")
    print("4) 어떤 숫자가 낙찰되면, 그 숫자에 쌓인 칩을 숫자와 함께 가져갑니다.")
    print("5) 칩이 없으면 무조건 낙찰받아야 합니다.")
    print("6) 다른사람의 칩 개수는 알 수 없으며, 다른 사람이 소유한 카드는 볼 수 있습니다.")
    print("7) 이렇게 경매가 끝나면 정산이 시작됩니다.")
    print("8) 정산은 기본적으로 각 숫자들과 칩의 개수를 합하여 계산합니다.")
    print("9) 즉, 카드를 -3,-8,-21을 소유하고, 칩은 2개가 남았으면, 점수는 -3-8-21+2 = -30 점이 됩니다.")
    print("10) 이때, 특별한 룰이 적용됩니다. 연속한 숫자는 크기가 가장 작은 숫자로만 계산합니다.")
    print("11) 즉, 카드를 -3,-21,-22,-23을 소유하고, 칩은 1개가 남았으면, 점수는 -3-21+1 = -23 점이 됩니다.")
    print("12) 작은 점수를 가진 사람이 승자가 됩니다. 마지막에는 순위가 출력됩니다.")


print("안녕하세요. 오노예들의 게임을 시작하겠습니다.")
print("룰은 다음과 같습니다.")
rule()
print("ZG(즐거운 게임)")

people = []

n = input("몇명이에요?\n>")

n = int(n)

for i in range(n):  # n명 가정, 0~n-1
    people.append(human(i, 20))

a = []
for i in range(-35, -2):
    a.append(i)

turn = 0  # 0 ~ n-1

while len(a):
    num = random.choice(a)  # 현재 숫자 결정
    chk = 1  # 1은 패스, 0은 낙찰
    stacked_coin = 0
    turn -= 1
    while chk:  # 낙찰받는 사람 결정
        turn += 1  # 다음 사람으로 넘기기
        turn = turn % n  # 계산
        if not people[turn].coin:  # 칩없으면 바로 끝
            print("{0}p님, 당신은 칩이 없습니다.".format(turn + 1), end=' ')
            break
        while not (chk == "0" or chk == "1"):
            chk = input(
                "{0}p님, 당신의 칩 개수는 {1}개이고, 현재 숫자는 {2}, {3}개의 칩이 쌓여있습니다.\n낙찰하시겠습니까?(패스:1,낙찰:0,도움말:help)".format(
                    people[turn].player, people[turn].coin, num, stacked_coin))
            if chk == "help":
                print("누군가의 카드가 궁금하면 card 를 입력하세요.\n규칙이 궁금하시다면 rule 을 입력하세요.\n다른 사람의 칩 개수는 알 수 없습니다.")
            if chk == "card":
                who = input("누구의 카드를 보시겠습니다? 1p~{0}p".format(n))
                print("{0}p의 카드 : ".format(who), end='')
                who = int(who)
                for i in range(len(people[who - 1].card)):
                    print("{0} ".format(people[who - 1].card[i]), end='')
                print("")
            if chk == "rule":
                print("<RULE>")
                rule()

        chk = int(chk)

        if chk:
            stacked_coin += 1  # 패스하면, 칩 개수 올리고
            people[turn].coin -= 1  # 가진 칩 줄이기
    print("{0}p님, 낙찰되었습니다.".format(turn + 1))  # 낙찰된 상황
    people[turn].coin += stacked_coin  # 칩 개수만큼 올렺고
    people[turn].card.append(num)  # 갖고 있는 카드에 추가
    a.remove(num)  # 방금 카드 지워버리기

for i in range(n):
    people[i].card.sort()
    people[i].score = people[i].coin

back_num = 0

for i in range(n):
    for j in range(len(people[i].card)):
        if people[i].card[j] == back_num + 1:
            pass
        else:
            people[i].score += people[i].card[j]
        back_num = people[i].card[j]

ranking = []

for i in range(n):
    ranking.append(people[i].score)

ranking.sort(reverse=True)

print("-----RANKING-----")
for i in range(n):
    for j in range(n):
        if ranking[i] == people[j].score:
            print("{0}.{1}p : {2}점".format(i + 1, people[j].player, people[j].score))
