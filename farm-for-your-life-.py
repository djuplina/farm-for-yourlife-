import pygame
import sys
import random
import math
import os
from pygame import mixer
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
# test
curr_path = os.path.dirname(__file__)  # Where your .py file is located
assets_path = os.path.join(curr_path, 'assets')  # The assets folder path


class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        cursorimage = pygame.image.load(
            os.path.join(f"{assets_path}", "cursor.png"))
        super(Cursor, self).__init__()
        self.surf = cursorimage.convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()

    # update the sprite based on keypress
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -132)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 132)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-132, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(132, 0)

            # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# TILL THE SOIL

# PLANT THE SEEDS

# WATER THE STUFF

# HARVEST THE CROPS

# class GrowthState

# class GameTimer

# class Inventory


pygame.init()

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT))  # , pygame.RESIZABLE)
# screen = pygame.display.set_mode((1024, 768), pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.display.set_caption('farm for your life!')
icon = pygame.image.load(os.path.join(f"{assets_path}", "icon.png"))
pygame.display.set_icon(icon)
bg = pygame.image.load(os.path.join(f"{assets_path}", "tileable_grass_00.png"))

cursor = Cursor()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 80)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            # get all the keys pressed
            pressed_keys = pygame.key.get_pressed()

            # update the cursor sprite every keypress
            cursor.update(pressed_keys)

    # blit the background
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    screen.blit(bg, (512, 0))
    screen.blit(bg, (0, 512))
    screen.blit(bg, (512, 512))

    # blit the player
    screen.blit(cursor.surf, cursor.rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
