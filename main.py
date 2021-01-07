#!/usr/bin/env python3

import pygame
import sys
import time
import random
import math
import os
import random_map
from pygame import mixer
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_w,
    K_DOWN,
    K_s,
    K_LEFT,
    K_a,
    K_RIGHT,
    K_d,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from pygame.locals import *
pygame.init()
pygame.display.set_caption('Farm for Your Life!')
screen = pygame.display.set_mode((900, 900),0,32)
display = pygame.Surface((300, 300))

curr_path = os.path.dirname(__file__)  # Where your .py file is located
assets_path = os.path.join(curr_path, 'assets')  # The assets folder path
grass_path = os.path.join(assets_path, 'background', 'grass')


grass_img = pygame.image.load(os.path.join(f"{grass_path}", "grass.png")).convert_alpha()
#grass_img.set_colorkey((0, 0, 0))

f = open('map-test.txt')
map_data = [[int(c) for c in row] for row in f.read().split('\n')]
f.close()

while True:
    display.fill((0,0,0))
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile:
                #pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                display.blit(grass_img, (150 + x * 7 - y * 7, 100 + x * 4 + y * 4))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
    time.sleep(1)
