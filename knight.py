import pygame
import ground as floor
import os
import ground as floor
import utils

from tiles import Tile 
from tiles import Tiles

TILES_HORIZONTAL = 7
TILES_VERTICAL = 10
TILESIZE = 100

class Knight:
    def __init__(self, id, x, y, knight_kind):
        self.id = id
        self.x, self.y = int(x+6), int(y)
        self.myinc = .05
        self.knight_image = ""
        if knight_kind == "k":
            self.knight_image = floor.KNIGHT_DARK_BACKGROUND
        else:
            s = "Sorry, I don't recognize that: {}".format(knight_kind)
            raise ValueError(s)
        
        image_path = os.path.join("levels", "images")
        self.image = pygame.image.load(os.path.join(image_path, self.knight_image)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))

    def move(self, x, y):
        if not utils.in_range(self.x, x, .05):
            if self.x < x:
                self.x += self.myinc
            elif self.x > x:
                self.x -= self.myinc
            else:
                self.x = x

        if not utils.in_range(self.y, y, .05):
            if self.y < y:
                self.y += self.myinc
            elif self.y > y:
                self.y -= self.myinc
            else:
                self.y = y
        

    def debug_print(self):
        s = "id: {}, x: {}, y: {}".format(self.id, self.x, self.y)
        print(s)

class KnightPlacement:
    def __init__(self, surface):
        self.surface = surface
        self.inner = [] 
        self.current_knight = None

        id = 0
        filepath = os.path.join("levels", "demolvl.txt")
        with open(filepath, "r") as f:
            mylines = f.readlines()
            mylines = [i.strip() for i in mylines if len(i.strip()) > 0]
        for count_i, line in enumerate(mylines):
            for count_j, elem in enumerate(line):
                if elem == "k":
                    new_knight = Knight(id, count_j, count_i, elem)
                    self.inner.append(new_knight)
                    id += 1

    def get_knight(self, x, y):
        for elem in self.inner:
            if elem.x == x and elem.y == y:
                return elem
        return None

    def format_xy(self):
        for elem in self.inner:
            elem.x = round(elem.x)
            elem.y = round(elem.y)

    def has_collided(self, mouse_pos):
        for elem in self.inner:
            myrect = pygame.Rect(elem.x * TILESIZE, elem.y * TILESIZE, TILESIZE, TILESIZE)
            if myrect.collidepoint(mouse_pos[0], mouse_pos[1]) == 1:
                return elem.x, elem.y
        return None, None

    def draw(self, surface):
        if len(self.inner) == 0:
            raise ValueError("Error, unkown tile")
        for elem in self.inner:
            myrect = pygame.Rect(elem.x * TILESIZE, elem.y * TILESIZE, TILESIZE, TILESIZE)
            self.surface.blit(elem.image, myrect)

    def debug_print(self):
        for elem in self.inner:
            elem.debug_print()