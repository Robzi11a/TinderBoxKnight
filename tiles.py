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
        if kind_of_tile == "d": filename = floor.DARK_TILE_EMPTY
        elif kind_of_tile == "l" : filename = floor.LIGHT_TILE_EMPTY
        elif kind_of_tile == "kd" : filename = floor.KNIGHT_DARK_BACKGROUND
        elif kind_of_tile == "kl" : filename = floor.KNIGHT_LIGHT_BACKGROUND
        elif kind_of_tile == "ht" : filename = floor.HIDDEN_TORCH
        elif kind_of_tile == "hs" : filename = floor.HIDDEN_SPIDER
        elif kind_of_tile == "hcu" : filename = floor.HIDDEN_CLUE_UP
        elif kind_of_tile == "hcd" : filename = floor.HIDDEN_CLUE_DIAGONAL
        elif kind_of_tile == "vut" : filename = floor.VISIBLE_UNLIT_TORCH
        elif kind_of_tile == "vlt" : filename = floor.VISIBLE_LIT_TORCH
        elif kind_of_tile == "sk" : filename = floor.SCAN_KNIGHT
        elif kind_of_tile == "st" : filename = floor.SCAN_TILE
        elif kind_of_tile == "mu" : filename = floor.MOVEMENT_UP
        elif kind_of_tile == "mr" : filename = floor.MOVEMENT_RIGHT
        elif kind_of_tile == "md" : filename = floor.MOVEMENT_DOWN
        elif kind_of_tile == "ml" : filename = floor.MOVEMENT_LEFT
        elif kind_of_tile == "mb" : filename = floor.MATCH_BUTTON
        elif kind_of_tile == "sb" : filename = floor.SCAN_BUTTON
        elif kind_of_tile == "qc" : filename = floor.QUIT_CONTROL 
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

    def draw(self, surface):
        if len(self.inner) == 0:
            raise ValueError("Specify tile to display")
        for elem in self.inner:
            self.screen.blit(elem.image, elem.rect)

    def debug_print(self):
        for elem in self.inner:
            elem.debug_print()