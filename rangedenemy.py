import pygame

from tiles import Tile, Tiles
from tiles import TILES_VERTICAL, TILES_HORIZONTAL, TILESIZE
from knight import Knight
from bigtorch import BigTorch


class Ranged_Enemy:
    def __init__(self, row, column):
        self.row = row
        self.column = column
    
    def ranged_attack(self, level_array, knight):
        
        if level_array[1][0] == 'kl' and (level_array[1][6] == 'hre' or 'pre'):
            print("0")
            level_array[1][0] = 'pk'
            level_array[1][1] = 'p'
            level_array[1][2] = 'psa'
            level_array[1][3] = 'psr'
            level_array[1][4] = 'pss'
            level_array[1][5] = 'p'
            level_array[1][6] = 'pre'   

        if level_array[1][1] == 'kl' and (level_array[1][6] == 'hre' or 'pre'):
            print("1")
            level_array[1][0] = 'p'
            level_array[1][1] = 'pk'
            level_array[1][2] = 'psa'
            level_array[1][3] = 'psr'
            level_array[1][4] = 'pss'
            level_array[1][5] = 'p'
            level_array[1][6] = 'pre'
            
        if level_array[1][2] == 'kl' and (level_array[1][6] == 'hre' or 'pre'):
            print("2")
            level_array[1][0] = 'p'
            level_array[1][1] = 'p'
            level_array[1][2] = 'pk'
            level_array[1][3] = 'psr'
            level_array[1][4] = 'pss'
            level_array[1][5] = 'p'
            level_array[1][6] = 'pre'
        
        if level_array[1][3] == 'kl' and (level_array[1][6] == 'hre' or 'pre'):
            print("3")
            level_array[1][0] = 'p'
            level_array[1][1] = 'p'
            level_array[1][2] = 'psa'
            level_array[1][3] = 'pk'
            level_array[1][4] = 'pss'
            level_array[1][5] = 'p'
            level_array[1][6] = 'pre'  
        
        if level_array[1][4] == 'kl' and (level_array[1][6] == 'hre' or 'pre'):
            print("4")
            level_array[1][0] = 'p'
            level_array[1][1] = 'pk'
            level_array[1][2] = 'psa'
            level_array[1][3] = 'psr'
            level_array[1][4] = 'pk'
            level_array[1][5] = 'p'
            level_array[1][6] = 'pre'
        
        if level_array[1][5] == 'kl' and (level_array[1][6] == 'hre' or 'pre'):
            print("5")
            level_array[1][0] = 'p'
            level_array[1][1] = 'p'
            level_array[1][2] = 'psa'
            level_array[1][3] = 'psr'
            level_array[1][4] = 'pss'
            level_array[1][5] = 'pk'
            level_array[1][6] = 'pre'

        if level_array[1][6] == 'lre':
            print("5")
            level_array[1][0] = 'l'
            level_array[1][1] = 'l'
            level_array[1][2] = 'lsa'
            level_array[1][3] = 'lsr'
            level_array[1][4] = 'lss'
            level_array[1][5] = 'l'
            level_array[1][6] = 'l'