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
        self.light()

    def light(self):
        kp_x, kp_y = self.position
        print("now position:", self.position)
        self.tip = pygame.Rect((kp_y + 6.4) * TILESIZE, (kp_x + 0.4) * TILESIZE, TILESIZE, TILESIZE)
        self.rect = pygame.Rect((kp_y + 6) * TILESIZE, kp_x * TILESIZE, TILESIZE, TILESIZE)
        for xIndex in range(kp_x - 1, kp_x + 2):
            for yIndex in range(kp_y - 1, kp_y + 2):
                    if self.original_array[xIndex][yIndex] == 'd':
                        self.tiles[xIndex][yIndex] = 'l'
                    elif self.original_array[xIndex][yIndex] == 'hs':
                        self.tiles[xIndex][yIndex] = 'ls'
                    # elif self.original_array[xIndex][yIndex] == 'kd':
                    #     self.tiles[xIndex][yIndex] = 'kl'
                    elif self.tiles[xIndex][yIndex] == 'ht':
                        self.tiles[xIndex][yIndex] = 'vlt'
                    continue
                    # self.tiles[xIndex][yIndex] = 'st'
        self.lit_tiles.append([self.tip, self.count])

    def update(self):
        pass
