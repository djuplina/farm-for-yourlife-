#!/usr/bin/env python3

import pygame
import sys
import time
import random
import math
import os
from pygame import mixer
from pygame.locals import (RLEACCEL, K_UP, K_e, K_DOWN, K_s, K_LEFT, K_f, K_RIGHT, K_d, K_ESCAPE, K_SPACE, KEYDOWN, QUIT, K_PAGEDOWN, K_PAGEUP, K_w, K_r,)

#local imports
import random_map

# classes and objects

class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        cursorimage = pygame.image.load(os.path.join(f"{assets_path}", "cursor", "cursor_0.png"))
        super(Cursor, self).__init__()
        self.surf = cursorimage.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(166,120))
        self.particles = []

    def emit(self):
        if self.particles:
            self.delete_particles()
            part_color = pygame.Color(13,183,109)
            for particle in self.particles:
                particle[0][1] += particle[2][0]
                particle[0][0] += particle[2][1]
                particle[1] -= 0.2
                pygame.draw.circle(display, part_color, particle[0], int(particle[1]))

    def add_particles(self):
        pos_x = self.rect.center[0] + random.randint(-6, 6)
        pos_y = self.rect.center[1] - y_offset - random.randint(-3,3)
        radius = 2
        direction_y = 0 #random.randint(-3, 3)
        direction_x = random.randint(-3, 0)
        particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y]]
        self.particles.append(particle_circle)

    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy

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

def print_map():
    tile_count = (len(map_tile) - 80)
    while tile_count < 80:
        if int(map_tile[tile_count]) == 1:
            display.blit(grss_img, map_pos[tile_count])
        if int(map_tile[tile_count]) == 2:
            display.blit(dirt_img, map_pos[tile_count])
        if int(map_tile[tile_count]) == 3:
            display.blit(till_img, map_pos[tile_count])
        tile_count += 1

class invCursor(pygame.sprite.Sprite):
    def __init__(self):
        cursorimage = pygame.image.load(os.path.join(f"{assets_path}", "inv", "inv-cursor.png"))
        super(invCursor, self).__init__()
        self.surf = cursorimage.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(topleft=(102, 10))

def inventory():
    display.blit(inv0, [102, 10])
    display.blit(inv1, [133, 10])
    display.blit(inv2, [164, 10])

def check_inputs():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE: 
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_s:
                if (cursor.rect.left -x_offset, cursor.rect.top -y_offset) not in map_pos:
                    pass
                else:
                    cursor.rect.move_ip(-x_offset, -y_offset)
            if event.key == K_RIGHT or event.key == K_f:
                if (cursor.rect.left + x_offset, cursor.rect.top + y_offset) not in map_pos:
                    pass
                else:
                    cursor.rect.move_ip(x_offset, y_offset)
            if event.key == K_DOWN or event.key == K_d:
                if (cursor.rect.left -x_offset, cursor.rect.top + y_offset) not in map_pos:
                    pass
                else:
                    cursor.rect.move_ip(-x_offset, y_offset)
            if event.key == K_UP or event.key == K_e:
                if (cursor.rect.left + x_offset, cursor.rect.top -y_offset) not in map_pos:
                    pass
                else:
                    cursor.rect.move_ip(x_offset, -y_offset)
            if event.key == K_r or event.key == K_PAGEDOWN:
                if (invCursor.rect.topleft == (164, 10)):
                    invCursor.rect.move_ip(-62, 0)
                else:
                    invCursor.rect.move_ip(31, 0)
            if event.key == K_w  or event.key == K_PAGEUP:
                if (invCursor.rect.topleft == (102, 10)):
                    invCursor.rect.move_ip(62, 0)
                else:
                    invCursor.rect.move_ip(-31, 0)
            if event.key == K_SPACE:
                # update map_data here
                if map_tile[(map_pos.index(cursor.rect.topleft))] == 1:
                    cursor.add_particles()
                    cursor.add_particles()
                    cursor.add_particles()
                    cursor.add_particles()
                    cursor.add_particles()
                    cursor.add_particles()
                    map_tile[(map_pos.index(cursor.rect.topleft))] = 3
                if map_tile[(map_pos.index(cursor.rect.topleft))] == 2:
                    cursor.add_particles()
                    cursor.add_particles()
                    cursor.add_particles()
                    cursor.add_particles()
                    cursor.add_particles()
                    cursor.add_particles()
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

def display_out():
    display.blit(cursor.surf, cursor.rect)
    display.blit(invCursor.surf, invCursor.rect)
    cursor.emit()
    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
    clock.tick(40)

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

#Set Paths
curr_path = os.path.dirname(__file__)
assets_path = os.path.join(curr_path, 'assets')
grass_path = os.path.join(assets_path, 'background', 'grass')
dirt_path = os.path.join(assets_path, 'background', 'dirt')
till_path = os.path.join(assets_path, 'background', 'till')
bgm_path = os.path.join(assets_path, 'audio', 'bgm')

#Load Assets
icon = pygame.image.load(os.path.join(f"{assets_path}", "icon.png"))
inv0 = pygame.image.load(os.path.join(f"{assets_path}", "inv", "inv_0.png")).convert()
inv0.get_rect()
inv1 = pygame.image.load(os.path.join(f"{assets_path}", "inv", "inv_1.png")).convert()
inv1.get_rect()
inv2 = pygame.image.load(os.path.join(f"{assets_path}", "inv", "inv_2.png")).convert()
inv2.get_rect()
pygame.display.set_icon(icon)
grss_img = pygame.image.load(os.path.join(f"{grass_path}", "grass.png")).convert_alpha()
dirt_img = pygame.image.load(os.path.join(f"{dirt_path}", "dirt.png")).convert_alpha()
till_img = pygame.image.load(os.path.join(f"{till_path}", "till.png")).convert_alpha()
grss_img = pygame.transform.scale(grss_img, (32, 40))
till_img = pygame.transform.scale(till_img, (32, 40))
dirt_img = pygame.transform.scale(dirt_img, (32, 40))
bgm = pygame.mixer.Sound(os.path.join(f"{bgm_path}", 'evening.wav'))

# set up the  map
random_map.main()
map_returns = read_map()
map_tile = map_returns[0]
map_pos = map_returns[1]
tile_count = (len(map_tile) - 80)

cursor = Cursor()
invCursor = invCursor()

for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init

while True:
    display.fill((0,0,0))

    # inventory
    inventory()
    
    # play bgm during the loop
    bgm.play()

    # actually print the map
    print_map()

    #event loop
    check_inputs()

    display_out()

pygame.joystick.quit()