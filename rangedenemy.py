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

        if level_array[3][4] == 'kl' and (level_array[3][10] == 'hre' or 'pre'):
            print("0")
            level_array[3][4] = 'pk'
            level_array[3][5] = 'p'
            level_array[3][6] = 'psa'
            level_array[3][7] = 'psr'
            level_array[3][8] = 'pss'
            level_array[3][9] = 'p'
            level_array[3][10] = 'pre'   

        if level_array[3][5] == 'kl' and (level_array[3][10] == 'hre' or 'pre'):
            print("1")
            level_array[3][4] = 'p'
            level_array[3][5] = 'pk'
            level_array[3][6] = 'psa'
            level_array[3][7] = 'psr'
            level_array[3][8] = 'pss'
            level_array[3][9] = 'p'
            level_array[3][10] = 'pre'
            
        if level_array[3][6] == 'kl' and (level_array[3][10] == 'hre' or 'pre'):
            print("2")
            level_array[3][4] = 'p'
            level_array[3][5] = 'p'
            level_array[3][6] = 'pk'
            level_array[3][7] = 'psr'
            level_array[3][8] = 'pss'
            level_array[3][9] = 'p'
            level_array[3][10] = 'pre'
        
        if level_array[3][7] == 'kl' and (level_array[3][10] == 'hre' or 'pre'):
            print("3")
            level_array[3][4] = 'p'
            level_array[3][5] = 'p'
            level_array[3][6] = 'psa'
            level_array[3][7] = 'pk'
            level_array[3][8] = 'pss'
            level_array[3][9] = 'p'
            level_array[3][10] = 'pre'  
        
        if level_array[3][8] == 'kl' and (level_array[3][10] == 'hre' or 'pre'):
            print("4")
            level_array[3][4] = 'p'
            level_array[3][5] = 'pk'
            level_array[3][6] = 'psa'
            level_array[3][7] = 'psr'
            level_array[3][8] = 'pk'
            level_array[3][9] = 'p'
            level_array[3][10] = 'pre'
        
        if level_array[3][9] == 'kl' and (level_array[3][10] == 'hre' or 'pre'):
            print("5")
            level_array[3][4] = 'p'
            level_array[3][5] = 'p'
            level_array[3][6] = 'psa'
            level_array[3][7] = 'psr'
            level_array[3][8] = 'pss'
            level_array[3][9] = 'pk'
            level_array[3][10] = 'pre'

        if level_array[3][10] == 'lre':
            print("5")
            level_array[3][4] = 'l'
            level_array[3][5] = 'l'
            level_array[3][6] = 'lsa'
            level_array[3][7] = 'lsr'
            level_array[3][8] = 'lss'
            level_array[3][9] = 'l'
            level_array[3][10] = 'l'