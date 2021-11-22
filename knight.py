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
    # Initilise knight to store the knight's starting row and column
    def __init__(self, row, column):
        self.row = row
        self.column = column

    #Updates the row and column stored for the knight. Called whenever the knight moves to new position.
    def update_position(self, row, column):
        self.row = row
        self.column = column
        print(self.row, self.column)
    
    def return_position(self):
        return self.row, self.column
    
    #Check that the knight is not moving into a barrier
    def check_move():
        return 0


        
        

# not sure what this code is doing - left it in just in case        

"""        
        self.id = id
        self.x, self.y = int(x+6), int(y)
        self.myinc = .05
        self.knight_image = ""
        if knight_kind == "k":
            self.knight_image = floor.KNIGHT_DARK_BACKGROUND
        else:
            s = "unrecognized format: {}".format(knight_kind)
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
"""
