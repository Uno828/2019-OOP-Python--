import threading
import pygame
import time
from main import main_game


def music():
    while True:
        blueming.play()
        time.sleep(249.0)
        time_out.play()
        time.sleep(330.0)
        love_poem.play()
        time.sleep(268.0)


pygame.mixer.init()
blueming = pygame.mixer.Sound("Blueming.wav")
time_out = pygame.mixer.Sound("시간의 바깥.wav")
love_poem = pygame.mixer.Sound("Love Poem.wav")

songA = threading.Thread(target=music)
mainA = threading.Thread(target=main_game)

songA.start()
mainA.start()
