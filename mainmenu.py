import os

import pygame

import ground as c
from game import State
from utils import WHITE


class Menu(State):

    def __init__(self):
        super().__init__()
        self.BG_COLOR = c.DARK_PURPLE
        self.stickers = []
        self.menu = []
        self.index = 0
        self.start_pos = {}
        self.setup_stickers()
        self.setup_title()
        self.setup_cursor()

    def keydown_events(self, key):
        pass

    def setup_stickers(self):
        image_path = os.path.join("levels", "menu")

        knight = "knight.png"
        knight_image = pygame.image.load(os.path.join(image_path, knight)).convert_alpha()
        knight_image = pygame.transform.scale(knight_image, (c.WINDOW_HEIGHT / 3, c.WINDOW_HEIGHT / 3))
        knight_rect = knight_image.get_rect()
        knight_rect.x, knight_rect.y = (c.WINDOW_WIDTH / 15, c.WINDOW_HEIGHT * 5 / 9)
        self.stickers.append((knight_image, knight_rect))

        cross = "cross.png"
        cross_image = pygame.image.load(os.path.join(image_path, cross)).convert_alpha()
        cross_image = pygame.transform.scale(cross_image, (c.WINDOW_HEIGHT / 5, c.WINDOW_HEIGHT / 5))
        circle = "circle.png"
        circle_image = pygame.image.load(os.path.join(image_path, circle)).convert_alpha()
        circle_image = pygame.transform.scale(circle_image, (c.WINDOW_HEIGHT / 9, c.WINDOW_HEIGHT / 9))
        question = "question.png"
        question_image = pygame.image.load(os.path.join(image_path, question)).convert_alpha()
        question_image = pygame.transform.scale(question_image, (c.WINDOW_HEIGHT / 7, c.WINDOW_HEIGHT / 7))

        cross_rect = knight_image.get_rect()
        cross_rect.x, cross_rect.y = (c.WINDOW_WIDTH * 14 / 15
                                      - cross_image.get_width() - circle_image.get_width() - question_image.get_width(),
                                      c.WINDOW_HEIGHT * 5 / 9 + (knight_image.get_height() - cross_image.get_height()))
        self.stickers.append((cross_image, cross_rect))

        circle_rect = knight_image.get_rect()
        circle_rect.x, circle_rect.y = (cross_rect.x + cross_image.get_width(),
                                        c.WINDOW_HEIGHT * 5 / 9 + (
                                                    knight_image.get_height() - circle_image.get_height()))
        self.stickers.append((circle_image, circle_rect))

        question_rect = question_image.get_rect()
        question_rect.x, question_rect.y = (circle_rect.x + circle_image.get_width(),
                                            c.WINDOW_HEIGHT * 5 / 9 + (
                                                    knight_image.get_height() - question_image.get_height()))
        self.stickers.append((question_image, question_rect))

    def setup_title(self):
        image_path = os.path.join("levels", "menu")
        title = "title.png"
        title_image = pygame.image.load(os.path.join(image_path, title)).convert_alpha()
        title_image = pygame.transform.scale(title_image, (c.WINDOW_WIDTH * 2 / 3, c.WINDOW_WIDTH * 2 / 3 / 6.1))
        title_rect = title_image.get_rect()
        title_rect.x, title_rect.y = ((c.WINDOW_WIDTH - title_image.get_width()) / 2, c.WINDOW_HEIGHT * 1 / 8)
        self.stickers.append((title_image, title_rect))

        start = "startgame.png"
        start_image = pygame.image.load(os.path.join(image_path, start)).convert_alpha()
        start_image = pygame.transform.scale(start_image, (c.WINDOW_WIDTH * 1 / 5, c.WINDOW_WIDTH * 1 / 5 / 9))
        start_rect = start_image.get_rect()
        start_rect.x, start_rect.y = (
        (c.WINDOW_WIDTH - start_image.get_width()) / 2, title_image.get_height() + c.WINDOW_HEIGHT * 3 / 8)
        self.menu.append((start_image, start_rect, c.LEVEL))

        exit = "exit.png"
        exit_image = pygame.image.load(os.path.join(image_path, exit)).convert_alpha()
        exit_image = pygame.transform.scale(exit_image,
                                            (c.WINDOW_WIDTH * 1 / 5 / 2.73, c.WINDOW_WIDTH * 1 / 5 / 2.73 / 3.29))
        exit_rect = exit_image.get_rect()
        exit_rect.x, exit_rect.y = (
            (c.WINDOW_WIDTH - start_image.get_width()) / 2,
            title_image.get_height() + start_image.get_height() * 2 + c.WINDOW_HEIGHT * 3 / 8)
        self.menu.append((exit_image, exit_rect, c.QUIT))

    def setup_cursor(self):
        self.cursor = pygame.sprite.Sprite()
        image_path = os.path.join("levels", "menu")
        cursor = "spider.png"
        cursor_image = pygame.image.load(os.path.join(image_path, cursor)).convert_alpha()
        cursor_image = pygame.transform.scale(cursor_image,
                                              (c.WINDOW_WIDTH * 1 / 5 / 7.3, c.WINDOW_WIDTH * 1 / 5 / 7.3 / 1.23))
        rect = cursor_image.get_rect()
        rect.x, rect.y = (self.menu[0][1].x - cursor_image.get_width() - 20, self.menu[0][1].y)
        self.cursor.image = cursor_image
        self.cursor.rect = rect
        self.cursor.state = self.menu[0][2]

    def update_cursor(self, key):
        if key == pygame.K_UP:
            self.index = (self.index - 1) % len(self.menu)
            print(self.index)
            self.cursor.rect.y = self.menu[self.index][1].y
            self.cursor.state = self.menu[self.index][2]
        elif key == pygame.K_DOWN:
            self.index = (self.index + 1) % len(self.menu)
            print(self.index)
            self.cursor.rect.y = self.menu[self.index][1].y
            self.cursor.state = self.menu[self.index][2]
        elif key == pygame.K_RETURN:
            self.next = self.cursor.state
            self.keep_looping = False



    def draw(self, surface):
        surface.fill(self.BG_COLOR)
        surface.blits(self.stickers)
        for m in self.menu:
            surface.blit(m[0], m[1])
        surface.blit(self.cursor.image, self.cursor.rect)

    def startup(self, game_info):
        pass

    def update(self, surface, keys):
        self.update_cursor(keys)
        self.draw(surface)
