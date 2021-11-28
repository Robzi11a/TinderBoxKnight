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

class Ranged_enemy:
    def __init__(self, level_array, original_array, scanned_tiles, position):
        self.current = None
        self.tiles = level_array
        self.position = position
        self.scanned_tiles = scanned_tiles
        self.original_array = original_array


    def attack(self, level_array):
        if level_array[1][0] == 'lk':
            level_array[1][0] == 'pk'
            level_array[1][1] == 'p'
            level_array[1][2] == 'psa'
            level_array[1][3] == 'psr'
            level_array[1][4] == 'pss'
            level_array[1][5] == 'p'
            level_array[1][6] == 'pre'
            reset_knight_poison(self, kp_y, kp_x)
        if level_array[1][1] == 'lk':
            level_array[1][0] == 'p'
            level_array[1][1] == 'pk'
            level_array[1][2] == 'psa'
            level_array[1][3] == 'psr'
            level_array[1][4] == 'pss'
            level_array[1][5] == 'p'
            level_array[1][6] == 'pre'
            reset_knight_poison(self, kp_y, kp_x)
        if level_array[1][2] == 'lk':
            level_array[1][0] == 'p'
            level_array[1][1] == 'p'
            level_array[1][2] == 'pk'
            level_array[1][3] == 'psr'
            level_array[1][4] == 'pss'
            level_array[1][5] == 'p'
            level_array[1][6] == 'pre'
            reset_knight_poison(self, kp_y, kp_x)
        if level_array[1][3] == 'lk':
            level_array[1][0] == 'p'
            level_array[1][1] == 'p'
            level_array[1][2] == 'psa'
            level_array[1][3] == 'pk'
            level_array[1][4] == 'pss'
            level_array[1][5] == 'p'
            level_array[1][6] == 'pre'
            reset_knight_poison(self, kp_y, kp_x)
        if level_array[1][4] == 'lk':
            level_array[1][0] == 'p'
            level_array[1][1] == 'pk'
            level_array[1][2] == 'psa'
            level_array[1][3] == 'psr'
            level_array[1][4] == 'pk'
            level_array[1][5] == 'p'
            level_array[1][6] == 'pre'
            reset_knight_poison(self, kp_y, kp_x)
        if level_array[1][5] == 'lk':
            level_array[1][0] == 'p'
            level_array[1][1] == 'pk'
            level_array[1][2] == 'psa'
            level_array[1][3] == 'psr'
            level_array[1][4] == 'pss'
            level_array[1][5] == 'pk'
            level_array[1][6] == 'pre'
            reset_knight_poison(self, kp_y, kp_x)

    def reset_knight_poison(self, kp_y, kp_x):
        font = pygame.font.SysFont("arial", 16)
        caption = font.render("Beware the eyes...", True, WHITE)
        '''self.screen.fill((0,0,0))'''
        '''self.screen.blit(caption,[self.wINDOW_WIDTH/2,self.wINDOW_HEIGHT/2])'''
        self.caption_rect = pygame.Rect((kp_x + 6) * TILESIZE, kp_y * TILESIZE, TILESIZE, TILESIZE)
        self.screen.blit(caption, self.caption_rect)
        pygame.display.flip()
        pygame.time.wait(1000)
        self.knight.reset_knight_position(self.level_array)

