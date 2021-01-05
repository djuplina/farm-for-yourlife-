#!/usr/bin/env python3

import sys
import pygame


class UserInterface:
    def __init__(self):
        pass


    def main_view(self, text_pos_x, text_pos_y):
        main_view_rect = pygame.Rect(10, 10, screen_width - 20, screen_height - 20)
        pygame.draw.rect(screen, (30,30,30), main_view_rect, 0)
        pygame.draw.rect(screen, (100,100,100), main_view_rect, 5)


    def left_menu(self, text_pos_x, text_pos_y):
        left_menu_rect = pygame.Rect(text_pos_x - 10, text_pos_y - 10, screen_width / 2, screen_height / 4)
        pygame.draw.rect(screen, (30,30,30), left_menu_rect, 0)
        pygame.draw.rect(screen, (100,100,100), left_menu_rect, 5)


class Director:
    def __init__(self):
        self.state = "intro"

    def quit_game(self):
        print("[Director] Cut! Take 5 People.")
        pygame.quit()
        sys.exit()


    def intro(self):
        txt_1 = rendered_text("Q: Nevan was right, wasn't he?")
        txt_2 = rendered_text("1. Yes.")
        txt_3 = rendered_text("2. Probably Not.")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit_game()
                if event.key == pygame.K_1:
                    print("[Director] Load the Main Game!")
                    self.state = "main_game"
                if event.key == pygame.K_2:
                    print("[Director] Load the Main Game!")
                    self.state = "main_game"

        screen.fill((100, 0, 0))
        ui.left_menu(default_text_pos_x, default_text_pos_y)
        screen.blit(txt_1, (default_text_pos_x, default_text_pos_y))
        screen.blit(txt_2, (default_text_pos_x, default_text_pos_y + txt_2.get_height()))
        screen.blit(txt_3, (default_text_pos_x, default_text_pos_y + (txt_2.get_height() + txt_1.get_height())))

        pygame.display.flip()


    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit_game()
                if event.key == pygame.K_RETURN:
                    print("[Director] Load the Intro!")
                    self.state = "intro"

        screen.fill((100, 0, 0))
        ui.main_view(default_text_pos_x, default_text_pos_y)
        txt_1 = rendered_text("If you say so...")
        screen.blit(txt_1, (default_text_pos_x, default_text_pos_y))
        pygame.display.flip()


    def manage(self):
        if self.state == "intro":
            self.intro()
        if self.state == "main_game":
            self.main_game()


### Setup the Game ###
pygame.init()
clock = pygame.time.Clock()
director = Director()
ui = UserInterface()
# Set Screen
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
default_text_pos_x = screen_width / 10
default_text_pos_y = screen_height / 10
default_font_size = 24


def rendered_text(message, font_color=None, font_size=None):
    global default_font_size
    if font_size == None:
        font_size = default_font_size
    if font_color == None:
        font_color = (255,255,255)
    base_font = pygame.font.Font(None, font_size)
    text_surface = base_font.render(message, True, font_color)
    return text_surface


def main():
    # Start the game.
    while True:
        director.manage()

        # Set the refresh rate.
        pygame.display.update()  # Full Screen Update.
        clock.tick(120)


main()
