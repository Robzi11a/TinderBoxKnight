import pygame
import copy

from tiles import Tile, Tiles
from tiles import TILES_VERTICAL, TILES_HORIZONTAL, TILESIZE
from knight import Knight
from bigtorch import BigTorch


class Ranged_Enemy:
    def __init__(self, row, column, level_array):
        self.row = row
        self.column = column
        self.level_array = level_array
        self.original_array = level_array
        self.lit = False
    
    def ranged_attack(self, knight, level):
        if self.level_array[self.row][self.column] == 'vre':
            return False, 0

        wall = False
        kp_y, kp_x = knight.return_position()
        self.original_array = copy.deepcopy(level)
        
        # If enemy is on same row as player
        if kp_y == self.row:
            # Check if there is a wall in the way
            if kp_x > self.column:
                for i in range(self.column, kp_x):
                    if level[self.row][i] == 'hw' or level[self.row][i] =='vw':
                        wall = True
            if kp_x < self.column:
                for i in range (kp_x, self.column):
                    if level[self.row][i] == 'hw' or level[self.row][i] == 'vw':
                        wall = True
            
            
            if not wall and level[kp_y][kp_x] == 'kl':
                level[self.row][self.column] = 'pre'
                level[kp_y][kp_x] = 'kp'
                return True, self.original_array
                
        #if enemy is on same column as player
        elif kp_x == self.column:
            # Check if there is a wall in the way
            if kp_y > self.row:
                for i in range(self.row, kp_y):
                    if level[i][self.column] == 'hw' or level[i][self.column] == 'vw':
                        wall = True
            elif kp_y < self.row:
                for i in range (kp_y, self.row):
                    if level[i][self.column] == 'hw' or level[i][self.column] == 'vw':
                        wall = True
            
            if not wall and self.level_array[kp_y][kp_x] == 'kl':
                level[self.row][self.column] = 'pre'
                level[kp_y][kp_x] = 'kp'
                return True, self.original_array
        
        return False, 0