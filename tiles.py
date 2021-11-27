import pygame
import ground as floor
import os
 
TILES_HORIZONTAL = 7
TILES_VERTICAL = 10
TILESIZE = 100
WINDOW_WIDTH = TILESIZE * TILES_HORIZONTAL
WINDOW_HEIGHT = TILESIZE * TILES_VERTICAL

# Class for each individual tile
class Tile:
    """A class to store all settings for Tinder Box Knight Tiles."""
    def __init__(self, id, x, y, kind_of_tile):
        filename = ""
        self.id = id
        self.x = int(x + 6)
        self.y = int(y)
        self.kind_of_tile = kind_of_tile
        # ----
        #Base tiles
        if kind_of_tile == "d": filename = floor.DARK_TILE_EMPTY
        elif kind_of_tile == "l" : filename = floor.LIGHT_TILE_EMPTY

        #Knight tiles
        elif kind_of_tile == "kd" : filename = floor.KNIGHT_DARK_BACKGROUND
        elif kind_of_tile == "kl" : filename = floor.KNIGHT_LIGHT_BACKGROUND

        #Wall and gate tiles
        elif kind_of_tile == "w" : filename = floor.WALL
        elif kind_of_tile == "hw" : filename = floor.HIDDEN_WALL
        elif kind_of_tile == "vcg" : filename = floor.LIT_CLOSED_GATE
        elif kind_of_tile == "hcg" : filename = floor.HIDDEN_CLOSED_GATE

        #Environmental tiles
        elif kind_of_tile == "lss" : filename = floor.LIT_SKELETON_SKULL
        elif kind_of_tile == "lsr" : filename = floor.LIT_SKELETON_RIBS
        elif kind_of_tile == "lsa" : filename = floor.LIT_SKELETON_ARMS
        elif kind_of_tile == "vb" : filename = floor.LIT_BOOKSHELF
        elif kind_of_tile == "hb" : filename = floor.HIDDEN_BOOKSHELF
        elif kind_of_tile == "lj" : filename = floor.LIT_JOURNAL
        elif kind_of_tile == "bl" : filename = floor.BROKEN_LAMP
        
        #Monster tiles
        elif kind_of_tile == "vre" : filename = floor.LIT_RANGED_ENEMY
        elif kind_of_tile == "hre" : filename = floor.DARK_RANGED_ENEMY
        elif kind_of_tile == "hrea" : filename = floor.DARK_RANGED_ENEMY_ANGRY
        elif kind_of_tile == 'vs' : filename = floor.LIT_SPIDER
        
        #Pressure plate tiles
        elif kind_of_tile == "lpp" : filename = floor.LIT_PRESSURE_PLATE
        elif kind_of_tile == "dpp" : filename = floor.HIDDEN_PRESSUREPLATE

        #Clue tiles
        elif kind_of_tile == "lcd" : filename = floor.LIT_CLUE_DIAGONAL
        elif kind_of_tile == "lcu" : filename = floor.LIT_CLUE_UP
        elif kind_of_tile == "lcr" : filename = floor.LIT_CLUE_RIGHT
        elif kind_of_tile == "lsc" : filename = floor.LIT_SPIDER_CLUE
        elif kind_of_tile == "dcr" : filename = floor.HIDDEN_CLUE_RIGHT
        elif kind_of_tile == "dcs" : filename = floor.HIDDEN_CLUE_SPIDER
        elif kind_of_tile == "dcu" : filename = floor.HIDDEN_CLUE_UP
        elif kind_of_tile == "dcd" : filename = floor.HIDDEN_CLUE_DIAGONAL

        #Torch tiles     
        elif kind_of_tile == "ht" : filename = floor.HIDDEN_TORCH
        elif kind_of_tile == "vut" : filename = floor.VISIBLE_UNLIT_TORCH
        elif kind_of_tile == "vlt" : filename = floor.VISIBLE_LIT_TORCH   
        
        # Info tiles
        elif kind_of_tile == "sk" : filename = floor.SCAN_KNIGHT
        elif kind_of_tile == "st" : filename = floor.SCAN_TILE
        elif kind_of_tile == "mu" : filename = floor.MOVEMENT_UP
        elif kind_of_tile == "mr" : filename = floor.MOVEMENT_RIGHT
        elif kind_of_tile == "md" : filename = floor.MOVEMENT_DOWN
        elif kind_of_tile == "ml" : filename = floor.MOVEMENT_LEFT
        elif kind_of_tile == "mb" : filename = floor.MATCH_BUTTON
        elif kind_of_tile == "sb" : filename = floor.SCAN_BUTTON
        elif kind_of_tile == "qc" : filename = floor.QUIT_CONTROL 
        elif kind_of_tile == "c" : filename = floor.CONTROLS
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

# Class for all tiles
class Tiles:
    def __init__(self, screen, level_array):
        self.screen = screen
        self.level_array = level_array
        self.inner = []
        self.current_tile = None
        self._load_data()

    # Load list of all tiles in game - list is one level.
    def _load_data(self):
        self.inner = []
        id = 0
        for count_i, myline in enumerate(self.level_array):
            for count_j, elem in enumerate(myline):
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
                # print("**** YES !!!!!! ****")
                # if s.rect.collidepoint(mouse_pos):
                return elem.x, elem.y
        return None, None

    # Draw tiles on to screen
    def draw(self, surface):
        if len(self.inner) == 0:
            raise ValueError("Specify tile to display")
        for elem in self.inner:
            self.screen.blit(elem.image, elem.rect)

    def debug_print(self):
        for elem in self.inner:
            elem.debug_print()
