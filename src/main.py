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
    K_SPACE,
    KEYDOWN,
    QUIT,
)

#local imports
import random_map

# classes

class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        cursorimage = pygame.image.load(os.path.join(f"{assets_path}", "cursor.png"))
        super(Cursor, self).__init__()
        self.surf = cursorimage.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(166,120))

def read_map():
    load_map = str(random_map.main())
    map_data = [[int(c) for c in row] for row in load_map.split('\n')]
    map_pos = []
    map_tile = []

    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile:
                location_var = (150 + x * x_offset - y * x_offset, 100 + x * y_offset + y * y_offset)
                if tile:
                    map_pos.append(location_var)
                    map_tile.append(tile)
    return map_tile, map_pos

from pygame.locals import *
pygame.init()
pygame.display.set_caption('Farm for Your Life!')
screen = pygame.display.set_mode((900, 900),0,32)
display = pygame.Surface((300, 300))
clock = pygame.time.Clock()
pygame.mixer.pre_init(frequency = 44100, size = -16, channels = 1, buffer = 512)
x_offset = 16
y_offset = 8

joysticks = []

curr_path = os.path.dirname(__file__)
assets_path = os.path.join(curr_path, 'assets')
grass_path = os.path.join(assets_path, 'background', 'grass')
dirt_path = os.path.join(assets_path, 'background', 'dirt')
seed_path = os.path.join(assets_path, 'background', 'seed')
bgm_path = os.path.join(assets_path, 'audio', 'bgm')
icon = pygame.image.load(os.path.join(f"{assets_path}", "icon.png"))
pygame.display.set_icon(icon)

grss_img = pygame.image.load(os.path.join(f"{grass_path}", "grass.png")).convert_alpha()
dirt_img = pygame.image.load(os.path.join(f"{dirt_path}", "dirt.png")).convert_alpha()
seed_img = pygame.image.load(os.path.join(f"{seed_path}", "seed.png")).convert_alpha()
bgm = pygame.mixer.Sound(os.path.join(f"{bgm_path}", 'evening.wav'))

# set up the  map
random_map.main()
map_returns = read_map()
map_pos = map_returns[1]
map_tile = map_returns[0]
tile_count = (len(map_tile) - 80)

cursor = Cursor()

for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init

while True:
    display.fill((0,0,0))
    
    # play bgm during the loop
    bgm.play()

    # actually print the map
    tile_count = (len(map_tile) - 80)
    while tile_count < 80:
        if int(map_tile[tile_count]) == 1:
            display.blit(grss_img, map_pos[tile_count])
        if int(map_tile[tile_count]) == 2:
            display.blit(dirt_img, map_pos[tile_count])
        if int(map_tile[tile_count]) == 3:
            display.blit(seed_img, map_pos[tile_count])
        tile_count += 1

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                print(map_pos)
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                if (cursor.rect.left -x_offset, cursor.rect.top -y_offset) not in map_pos:
                    pass
                else:
                    cursor.rect.move_ip(-x_offset, -y_offset)
            if event.key == K_RIGHT or event.key == K_d:
                if (cursor.rect.left + x_offset, cursor.rect.top + y_offset) not in map_pos:
                    pass
                else:
                    cursor.rect.move_ip(x_offset, y_offset)
            if event.key == K_DOWN or event.key == K_s:
                if (cursor.rect.left -x_offset, cursor.rect.top + y_offset) not in map_pos:
                    pass
                else:
                    cursor.rect.move_ip(-x_offset, y_offset)
            if event.key == K_UP or event.key == K_w:
                if (cursor.rect.left + x_offset, cursor.rect.top -y_offset) not in map_pos:
                    pass
                else:
                    cursor.rect.move_ip(x_offset, -y_offset)
            if event.key == K_SPACE:
                # update map_data here
                map_tile[(map_pos.index(cursor.rect.topleft))] = 3

        # if (cursor.rect.centerx
        #     cursor.rect.move_ip(-x_offset, -y_offset)


        # if event.type == JOYHATMOTION:
        #     if joysticks[0].get_hat(0) == (-1,0): #left
        #         cursor.rect.move_ip(-x_offset, -y_offset)
        #     if joysticks[0].get_hat(0) == (1,0): #right
        #         cursor.rect.move_ip(x_offset, y_offset)
        #     if joysticks[0].get_hat(0) == (0,1): #down
        #         cursor.rect.move_ip(-x_offset, y_offset)
        #     if joysticks[0].get_hat(0) == (0,-1): #up
        #         cursor.rect.move_ip(x_offset, -y_offset)
        # if event.type == pygame.MOUSEMOTION:
        #     mouse_position = pygame.mouse.get_pos()
        #     cursor.rect.move(mouse_position[0], mouse_position[1])

    display.blit(cursor.surf, cursor.rect)

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
    clock.tick(60)

pygame.joystick.quit()