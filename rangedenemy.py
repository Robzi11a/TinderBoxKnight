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
                    if 'w' in level[self.row][i]:
                        wall = True
            if kp_x < self.column:
                for i in range (kp_x, self.column):
                    if 'w' in level[self.row][i]:
                        wall = True
            
            
            if not wall and level[kp_y][kp_x] == 'kl':
                level[self.row][self.column] = 'pre'
                level[kp_y][kp_x] = 'kp'
                return True, self.original_array
                
                #Not all tiles have poison variant
                """
                if kp_x > self.column:
                    for i in range (self.column, kp_x):
                        level[self.row][i] = level[self.row][i].replace('l', 'p')
                        level[self.row][i] = level[self.row][i].replace('d', 'p')
                    return True, self.original_array 
                    
                if kp_x < self.column:      
                    for i in range (kp_x, self.column):
                        level[self.row][i] = level[self.row][i].replace('l', 'p')
                        level[self.row][i] = level[self.row][i].replace('d', 'p')
                    return True, self.original_array 
                """

        #if enemy is on same column as player
        elif kp_x == self.column:
            # Check if there is a wall in the way
            if kp_y > self.row:
                for i in range(self.row, kp_y):
                    if 'w' in self.level_array[i][self.column]:
                        wall = True
                        print(wall, i)
            elif kp_y < self.row:
                for i in range (kp_y, self.row):
                    if 'w' in self.level_array[i][self.column]:
                        wall = True
            
            if not wall and self.level_array[kp_y][kp_x] == 'kl':
                level[self.row][self.column] = 'pre'
                level[kp_y][kp_x] = 'kp'
                return True, self.original_array
                

                """
                if kp_y > self.row:
                    print("greater")
                    for i in range (self.row, kp_y):
                        level[i][self.column] = level[i][self.column].replace('l', 'p')
                        level[i][self.column] = level[i][self.column].replace('d', 'p')
                        level[i][self.column] = level[i][self.column].replace('l', 'p')
                        level[i][self.column] = level[i][self.column].replace('d', 'p')

                    return True, self.original_array 
                    
                if kp_y < self.row:      
                    for i in range (kp_y, self.row):
                        level[i][self.column] = level[i][self.column].replace('l', 'p')
                        level[i][self.column] = level[i][self.column].replace('d', 'p')
                    return True, self.original_array 
                """
        return False, self.level_array
       
       
        """
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
            level_array[3][6] = 'psa'
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
            """