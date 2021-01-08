#!/usr/bin/env python3

import pygame
import sys
import time
import random
import math
import os
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

#local imports
import random_map

from pygame.locals import *
pygame.init()
pygame.display.set_caption('Farm for Your Life!')
screen = pygame.display.set_mode((900, 900),0,32)
display = pygame.Surface((300, 300))

curr_path = os.path.dirname(__file__)  # Where your .py file is located
assets_path = os.path.join(curr_path, 'assets')  # The assets folder path
grass_path = os.path.join(assets_path, 'background', 'grass')
dirt_path = os.path.join(assets_path, 'background', 'dirt')
seed_path = os.path.join(assets_path, 'background', 'seed')
icon = pygame.image.load(os.path.join(f"{assets_path}", "icon.png"))
pygame.display.set_icon(icon)

grass_img = pygame.image.load(os.path.join(f"{grass_path}", "dark-grass.png")).convert_alpha()
dirt_img = pygame.image.load(os.path.join(f"{dirt_path}", "dark-dirt.png")).convert_alpha()
seed_img = pygame.image.load(os.path.join(f"{seed_path}", "dark-seed.png")).convert_alpha()
#grass_surf = grass_img
#grass_rect = pygame.transform.rotozoom((grass_surf), 1, 2)
#grass_img.set_colorkey((0, 0, 0))

#f = open('map.txt')
f = open('map-test.txt')
map_data = [[int(c) for c in row] for row in f.read().split('\n')]
f.close()

while True:
    display.fill((0,0,0))
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile:
                if tile == 1:
                    #pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                    display.blit(grass_img, (150 + x * 8 - y * 8, 100 + x * 4 + y * 4))
                if tile == 2:
                    display.blit(dirt_img, (150 + x * 8 - y * 8, 100 + x * 4 + y * 4))
                if tile == 3:
                    display.blit(seed_img, (150 + x * 8 - y * 8, 100 + x * 4 + y * 4))

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
