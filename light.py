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
                    
                if kp_x == xIndex and kp_y == yIndex:
                    self.tiles[xIndex][yIndex] = 'kl'
                    continue   
                elif self.original_array[xIndex][yIndex] == 'd':
                    self.tiles[xIndex][yIndex] = 'l'
                elif self.tiles[xIndex][yIndex].startswith('h'):
                    self.tiles[xIndex][yIndex] = self.tiles[xIndex][yIndex].replace('h', 'v', 1)
                elif self.tiles[xIndex][yIndex].startswith('d'):
                    self.tiles[xIndex][yIndex] = self.tiles[xIndex][yIndex].replace('d', 'l', 1)
                # elif self.tiles[xIndex][yIndex] == 'vs':
                #     self.knight.update_position(9, 0)
                #     self.level_array[kp_y][kp_x], self.level_array[9][0] = self.level_array[9][0], self.level_array[kp_y][kp_x]
        self.lit_tiles.append([self.tip, self.count]) 

    #def reset_knight(self, kp_y, kp_x):
     #   font = pygame.font.SysFont("arial", 20)
      #  caption = font.render("You lit a spider!", True , WHITE)
       # '''self.screen.fill((0,0,0))'''
        #'''self.screen.blit(caption,[self.wINDOW_WIDTH/2,self.wINDOW_HEIGHT/2])'''
        #self.screen.blit(caption,[100,100])
        #pygame.display.flip()
        #pygame.time.wait(1000)
        #self.knight.update_position(9, 0)
        #self.level_array[kp_y][kp_x], self.level_array[9][0] = self.level_array[9][0], self.level_array[kp_y][kp_x]    

    #def reset_knight_position(self):
     #    if self.original_array[xIndex][yIndex] == 'ls': 
      #      return True

    #def check_for_enemy(self, square):
     #   if square == 'hs':
      #      return True
       # return False
         
    #def return_position(self):
     #   return self.row, self.column

#    def check_for_spider(self, square):
 #       if square == 'ls':
  #          return True
   #     return False    

    def update(self):
        pass