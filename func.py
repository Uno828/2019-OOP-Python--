import pygame
import make_class

Black = (100, 100, 100)


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


def card_show(card_num, screen):
    card = pygame.image.load("image/" + str(-card_num) + "- 큰 버전.png")
    image_show(card, 784, 58, screen)


def image_show(image, x, y, screen):
    screen.blit(image, (x, y))
    pygame.display.flip()


def text_show(txt, size, x, y, screen):
    locus = [(822.2, 386.25), (857.44, 495.25), (859.44, 610.25), (150, 150)]
    fontObj = pygame.font.Font('맑은고딕.ttf', size)  # 현재 디렉토리로부터 myfont.ttf 폰트 파일을 로딩한다. 텍스트 크기를 size로 한다
    textSurfaceObj = fontObj.render(txt, True,Black)  # 텍스트 객체를 생성한다. 첫번째 파라미터는 텍스트 내용, 두번째는 Anti-aliasing 사용 여부, 세번째는 텍스트 컬러를
    # 나타낸다
    textRectObj = textSurfaceObj.get_rect()  # 텍스트 객체의 출력 위치를 가져온다
    textRectObj.center = (x, y)  # 텍스트 객체의 출력 중심 좌표를 설정한다
    screen.blit(textSurfaceObj, textRectObj)


def player_number(nowPlaying, screen):
    text_show(nowPlaying, 20, 236.46, 38.22, screen)


# 출처: https://devnauts.tistory.com/61 [devnauts]

def ranking(people, n, screen):
    for i in range(n):
        people[i].calculate()

    people.sort(key=lambda rank: rank.score, reverse=True)

    lank = []
    for i in range(n):
        lank.append(pygame.image.load("p" + str(people[i].player) + "- 큰 결과.png"))
    for i in range(7 - n):
        lank.append(pygame.image.load("p_emt- 작은 결과.png"))

    locx = [403.024, 202.524, 603.524, 179.978, 336.978, 503.978, 659.978]
    locy = [256.374, 256.374, 256.374, 394.752, 394.752, 394.752, 394.752]
    for i in range(7):
        image_show(lank[i], locx[i], locy[i], screen)


current_player_loc = [85, 429.4]
current_chip_loc = [181.69, 668.75]
current_card_loc = [[340.725, 446.833], [410.903, 446.833], [480.904, 446.833], [550.904, 446.833], [620.904, 446.833],
                    [690.904, 446.833], [270.904, 530.333], [340.725, 530.333], [410.904, 530.333], [480.904, 530.333],
                    [550.904, 530.333], [620.904, 530.333], [690.904, 530.333], [270.904, 623.833], [340.725, 623.833],
                    [410.903, 623.833], [480.904, 623.833], [550.904, 623.833], [620.904, 623.833], [690.904, 623.833]]
player_loc = [[18.544, 114.832], [18.544, 219.832], [18.544, 820.832], [401.794, 114.832], [401.794, 219.832],
              [401.794, 320.832]]
player_card_loc = [[248.279, 162.888], [248.279, 267.055], [248.279, 377.222], [629.946, 162.888], [629.946, 267.055],
                   [629.946, 377.222]]
current_score_loc = [859.44, 610.25]
show_title_loc = [236.46,38.22]

def turn_change(turn, people, remain_card, remain_coin,screen,n):  # turn은 바뀐 턴을 받는 것임
    main_screen = pygame.image.load("image/ing.png")
    image_show(main_screen,0,0,screen)
    changed_player = make_class.human(turn, people[turn].coin, remain_card, remain_coin)
    card_list=[]
    a=0
    for i in people[turn].card:
        card_list.append(pygame.image.load("image/" + str(-i) + "- 작은버전.png"))
        a+=1
    for i in range(a):
        image_show(card_list[i],current_card_loc[i][0],current_card_loc[i][1],screen)

    player_logo = pygame.image.load("image/p"+str(turn+1)+"- 작은 버전.png")
    image_show(player_logo,current_player_loc[0],current_player_loc[1], screen)

    text_show(str(changed_player.coin), 40,current_chip_loc[0],current_chip_loc[1],screen)
    people[turn].calculate()
    text_show(str(people[turn].score), 40, current_score_loc[0],current_score_loc[1],screen)

    text_show(str(turn+1),40, show_title_loc[0],show_title_loc[1],screen)

    text_show(str(remain_coin), 50, 822.2, 386.25, screen)

    text_show(str(remain_card), 50, 857.44, 495.25, screen)

    # for i in range(n):
    #     if i != turn:
    #



