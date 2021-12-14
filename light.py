import copy

import pygame
import ground as floor
import os
import csv
import time

from tiles import Tile, Tiles
from tiles import TILES_VERTICAL, TILES_HORIZONTAL
from knight import Knight
from bigtorch import BigTorch

from knight import *
from tiles import TILES_VERTICAL, TILES_HORIZONTAL, TILESIZE

class Light:
    def __init__(self, level_array, original_array, lit_tiles, position):
        self.current = None
        self.tiles = level_array
        self.position = position
        self.lit_tiles = lit_tiles
        self.original_array = original_array
        self.count = 0
        self.previous_tile = 'd'
        self.light()

    def light(self):
        kp_x, kp_y = self.position

        for xIndex in range(kp_x - 1, kp_x + 2):
            for yIndex in range(kp_y - 1, kp_y + 2):
                if -1 < xIndex < TILES_VERTICAL and -1 < yIndex < TILES_HORIZONTAL:
                    if kp_x == xIndex and kp_y == yIndex:
                        if self.original_array[xIndex][yIndex].startswith('h'):
                            self.previous_tile = self.original_array[xIndex][yIndex].replace('h', 'v', 1)
                        elif self.original_array[xIndex][yIndex].startswith('d'):
                            self.previous_tile = self.original_array[xIndex][yIndex].replace('d', 'l', 1)
                        elif self.original_array[xIndex][yIndex].startswith('p'):
                            self.previous_tile = self.original_array[xIndex][yIndex].replace('p', 'l', 1) 
                        else:
                            self.previous_tile = 'l'
                        # an if method to fix a bug about gate
                        if self.previous_tile=="vcg":
                            self.previous_tile="log"
                        self.tiles[xIndex][yIndex] = 'kl'
                        continue
                    if self.tiles[xIndex][yIndex].startswith('h'):
                        self.tiles[xIndex][yIndex] = self.tiles[xIndex][yIndex].replace('h', 'v', 1)
                    elif self.tiles[xIndex][yIndex].startswith('d'):
                        self.tiles[xIndex][yIndex] = self.tiles[xIndex][yIndex].replace('d', 'l', 1)
                    elif self.tiles[xIndex][yIndex].startswith('p'):
                        self.tiles[xIndex][yIndex] = self.tiles[xIndex][yIndex].replace('p', 'l', 1)

    def update(self):
        pass