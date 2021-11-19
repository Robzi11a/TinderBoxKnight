import pygame
import ground as floor
import os

TILES_HORIZONTAL = 7
TILES_VERTICAL = 10
TILESIZE = 100
WINDOW_WIDTH = TILESIZE * TILES_HORIZONTAL
WINDOW_HEIGHT = TILESIZE * TILES_VERTICAL

class Tile:
    """A class to store all settings for Tinder Box Knight Tiles."""
    def __init__(self, id, x, y, kind_of_tile):
        filename = ""
        self.id = id
        self.x = int(x + 6)
        self.y = int(y)
        self.kind_of_tile = kind_of_tile
        # ----
        if kind_of_tile == "t": filename = floor.UNLIT_TORCH
        elif kind_of_tile == "d" : filename = floor.DARK
        elif kind_of_tile == "k" : filename = floor.KNIGHT_DARK_BACKGROUND
        elif kind_of_tile == "s" : filename = floor.SPIDER_DARK_BACKGROUND
        else: raise ValueError("Error, unkown tile: ", kind_of_tile)
        # ---------------------
        self.rect = pygame.Rect(self.x * TILESIZE, self.y * TILESIZE, TILESIZE, TILESIZE)
        image_path = os.path.join("levels", "images")
        self.image = pygame.image.load(os.path.join(image_path, filename)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))

    def debug_print(self):
        s = "id: {}, x: {}, y: {}, kind: {}"
        s = s.format(self.id, self.x, self.y, self.kind_of_tile)
        print(s)

class Tiles:
    def __init__(self, screen):
        self.screen = screen
        self.inner = []
        self.current_tile = None
        self._load_data()

    def _load_data(self):
        self.inner = []
        filepath = os.path.join("levels", "demolvl.txt")
        with open(filepath, "r") as f:
            mylines = f.readlines()
            mylines = [i.strip() for i in mylines if len(i.strip()) > 0]
        id = 0
        for count_i, myline in enumerate(mylines):
            temp_list = myline.split(";")
            temp_list = [i.strip() for i in temp_list if len(i.strip()) > 0]
            for count_j, elem in enumerate(temp_list):
                new_tile = Tile(id, count_j, count_i, elem)
                self.inner.append(new_tile)
                id += 1

    def get_tile(self, x, y):
        for elem in self.inner:
            if elem.x == x:
                if elem.y == y:
                    return elem
        return None

    def has_collided(self, mouse_pos):
        for elem in self.inner:
            if elem.rect.collidepoint(mouse_pos) == 1:
                return elem.x, elem.y
        return None, None
    
    def draw(self, surface):
        if len(self.inner) == 0:
            raise ValueError("Specify tile to display")
        for elem in self.inner:
            self.screen.blit(elem.image, elem.rect)

    def debug_print(self):
        for elem in self.inner:
            elem.debug_print()