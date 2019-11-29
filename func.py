import pygame

Black = (0, 0, 0)


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


def card_show(card_num, screen):  # 화면에 선택된 카드를 띄워주는 함수
    card = pygame.image.load("image/" + str(-card_num) + "- 큰 버전.png")
    screen.blit(card, (784, 58))
    pygame.display.flip()


def card_text(n, screen):
    cardWhich = [[248.279, 162.888], [248.279, 267.055], [248.279, 377.222], [629.946, 162.888], [622.946, 267.0550],
                 [629.946, 377.222]]
    fontObj = pygame.font.Font('myfont.ttf', 32)  # 현재 디렉토리로부터 myfont.ttf 폰트 파일을 로딩한다. 텍스트 크기를 32로 한다
    textSurfaceObj = fontObj.render('Hello Font!', True,
                                    Black)  # 텍스트 객체를 생성한다. 첫번째 파라미터는 텍스트 내용, 두번째는 Anti-aliasing 사용 여부, 세번째는 텍스트 컬러를
    # 나타낸다
    textRectObj = textSurfaceObj.get_rect()  # 텍스트 객체의 출력 위치를 가져온다
    textRectObj.center = (cardWhich[n - 1][0], cardWhich[n - 1][1])  # 텍스트 객체의 출력 중심 좌표를 설정한다
    screen.blit(textSurfaceObj, textRectObj)


def current_chip(screen):
    fontObj = pygame.font.Font('myfont.ttf', 32)  # 현재 디렉토리로부터 myfont.ttf 폰트 파일을 로딩한다. 텍스트 크기를 32로 한다
    textSurfaceObj = fontObj.render('Hello Font!', True,
                                    Black)  # 텍스트 객체를 생성한다. 첫번째 파라미터는 텍스트 내용, 두번째는 Anti-aliasing 사용 여부, 세번째는 텍스트 컬러를
    # 나타낸다
    textRectObj = textSurfaceObj.get_rect()  # 텍스트 객체의 출력 위치를 가져온다
    textRectObj.center = (822.2, 386.25)  # 텍스트 객체의 출력 중심 좌표를 설정한다
    screen.blit(textSurfaceObj, textRectObj)


def player_number(screen):
    fontObj = pygame.font.Font('myfont.ttf', 32)  # 현재 디렉토리로부터 myfont.ttf 폰트 파일을 로딩한다. 텍스트 크기를 32로 한다
    textSurfaceObj = fontObj.render('Hello Font!', True,
                                    (0, 0, 255))  # 텍스트 객체를 생성한다. 첫번째 파라미터는 텍스트 내용, 두번째는 Anti-aliasing 사용 여부, 세번째는 텍스트 컬러를
    # 나타낸다
    textRectObj = textSurfaceObj.get_rect()  # 텍스트 객체의 출력 위치를 가져온다
    textRectObj.center = (236.46, 38.22)  # 텍스트 객체의 출력 중심 좌표를 설정한다
    screen.blit(textSurfaceObj, textRectObj)


def remain_card(screen):
    fontObj = pygame.font.Font('myfont.ttf', 32)  # 현재 디렉토리로부터 myfont.ttf 폰트 파일을 로딩한다. 텍스트 크기를 32로 한다
    textSurfaceObj = fontObj.render('Hello Font!', True,
                                    Black)  # 텍스트 객체를 생성한다. 첫번째 파라미터는 텍스트 내용, 두번째는 Anti-aliasing 사용 여부, 세번째는 텍스트 컬러를
    # 나타낸다
    textRectObj = textSurfaceObj.get_rect()  # 텍스트 객체의 출력 위치를 가져온다
    textRectObj.center = (857.44, 495.25)  # 텍스트 객체의 출력 중심 좌표를 설정한다
    screen.blit(textSurfaceObj, textRectObj)


def current_score(screen):
    fontObj = pygame.font.Font('myfont.ttf', 32)  # 현재 디렉토리로부터 myfont.ttf 폰트 파일을 로딩한다. 텍스트 크기를 32로 한다
    textSurfaceObj = fontObj.render('Hello Font!', True,
                                    Black)  # 텍스트 객체를 생성한다. 첫번째 파라미터는 텍스트 내용, 두번째는 Anti-aliasing 사용 여부, 세번째는 텍스트 컬러를
    # 나타낸다
    textRectObj = textSurfaceObj.get_rect()  # 텍스트 객체의 출력 위치를 가져온다
    textRectObj.center = (859.44, 610.25)  # 텍스트 객체의 출력 중심 좌표를 설정한다
    screen.blit(textSurfaceObj, textRectObj)


def my_chip(screen):
    fontObj = pygame.font.Font('myfont.ttf', 32)  # 현재 디렉토리로부터 myfont.ttf 폰트 파일을 로딩한다. 텍스트 크기를 32로 한다
    textSurfaceObj = fontObj.render('Hello Font!', True,
                                    Black)  # 텍스트 객체를 생성한다. 첫번째 파라미터는 텍스트 내용, 두번째는 Anti-aliasing 사용 여부, 세번째는 텍스트 컬러를
    # 나타낸다
    textRectObj = textSurfaceObj.get_rect()  # 텍스트 객체의 출력 위치를 가져온다
    textRectObj.center = (150, 150)  # 텍스트 객체의 출력 중심 좌표를 설정한다
    screen.blit(textSurfaceObj, textRectObj)


# 출처: https://devnauts.tistory.com/61 [devnauts]

def ranking(people, n, screen):
    for i in range(n):
        people[i].calculate()

    people.sort(key=lambda rank: rank.score, reverse=True)

    first = pygame.image.load("p" + str(people[0].player) + "- 큰 결과.png")
    second = pygame.image.load("p" + str(people[1].player) + "- 큰 결과.png")
    third = pygame.image.load("p" + str(people[2].player) + "- 큰 결과.png")
    fourth = pygame.image.load("p" + str(people[3].player) + "- 작은 결과.png")

    if n == 4:
        fifth = pygame.image.load("p_emt- 작은 결과.png")
        sixth = pygame.image.load("p_emt- 작은 결과.png")
        seventh = pygame.image.load("p_emt- 작은 결과.png")

    if n == 5:
        fifth = pygame.image.load("p" + str(people[4].player) + "- 작은 결과.png")
        sixth = ("p_emt- 작은 결과.png")
        seventh = ("p_emt- 작은 결과.png")

    if n == 6:
        fifth = pygame.image.load("p" + str(people[4].player) + "- 작은 결과.png")
        sixth = pygame.image.load("p" + str(people[5].player) + "- 작은 결과.png")
        seventh = ("p_emt- 작은 결과.png")

    if n == 7:
        fifth = pygame.image.load("p" + str(people[4].player) + "- 작은 결과.png")
        sixth = pygame.image.load("p" + str(people[5].player) + "- 작은 결과.png")
        seventh = pygame.image.load("p" + str(people[6].player) + "- 작은 결과.png")

    player_show(first, 403.024, 256.374)
    player_show(second, 202.524, 256.374)
    player_show(third, 603.524, 256.374)
    player_show(fourth, 179.978, 394.752)
    player_show(fifth, 336.978, 394.752)
    player_show(sixth, 503.978, 394.752)
    player_show(seventh, 659.978, 394.752)
