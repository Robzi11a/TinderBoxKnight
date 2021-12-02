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
        
        if level_array[1][6] == 'kl' and (level_array[1][12] == 'hre' or 'pre'):
            print("0")
            level_array[1][6] = 'pk'
            level_array[1][7] = 'p'
            level_array[1][8] = 'psa'
            level_array[1][9] = 'psr'
            level_array[1][10] = 'pss'
            level_array[1][11] = 'p'
            level_array[1][12] = 'pre'   

        if level_array[1][7] == 'kl' and (level_array[1][12] == 'hre' or 'pre'):
            print("1")
            level_array[1][6] = 'p'
            level_array[1][7] = 'pk'
            level_array[1][8] = 'psa'
            level_array[1][9] = 'psr'
            level_array[1][10] = 'pss'
            level_array[1][11] = 'p'
            level_array[1][12] = 'pre'
            
        if level_array[1][8] == 'kl' and (level_array[1][12] == 'hre' or 'pre'):
            print("2")
            level_array[1][6] = 'p'
            level_array[1][7] = 'p'
            level_array[1][8] = 'pk'
            level_array[1][9] = 'psr'
            level_array[1][10] = 'pss'
            level_array[1][11] = 'p'
            level_array[1][12] = 'pre'
        
        if level_array[1][9] == 'kl' and (level_array[1][12] == 'hre' or 'pre'):
            print("3")
            level_array[1][6] = 'p'
            level_array[1][7] = 'p'
            level_array[1][8] = 'psa'
            level_array[1][9] = 'pk'
            level_array[1][10] = 'pss'
            level_array[1][11] = 'p'
            level_array[1][12] = 'pre'  
        
        if level_array[1][10] == 'kl' and (level_array[1][12] == 'hre' or 'pre'):
            print("4")
            level_array[1][6] = 'p'
            level_array[1][7] = 'pk'
            level_array[1][8] = 'psa'
            level_array[1][9] = 'psr'
            level_array[1][10] = 'pk'
            level_array[1][11] = 'p'
            level_array[1][12] = 'pre'
        
        if level_array[1][11] == 'kl' and (level_array[1][12] == 'hre' or 'pre'):
            print("5")
            level_array[1][6] = 'p'
            level_array[1][7] = 'p'
            level_array[1][8] = 'psa'
            level_array[1][9] = 'psr'
            level_array[1][10] = 'pss'
            level_array[1][11] = 'pk'
            level_array[1][12] = 'pre'

        if level_array[1][12] == 'lre':
            print("5")
            level_array[1][6] = 'l'
            level_array[1][7] = 'l'
            level_array[1][8] = 'lsa'
            level_array[1][9] = 'lsr'
            level_array[1][10] = 'lss'
            level_array[1][11] = 'l'
            level_array[1][12] = 'l'