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
                        print('ppp', self.previous_tile)
                        self.tiles[xIndex][yIndex] = 'kl'
                        continue
                    if self.tiles[xIndex][yIndex].startswith('h'):
                        print(xIndex, yIndex, 2)
                        self.tiles[xIndex][yIndex] = self.tiles[xIndex][yIndex].replace('h', 'v', 1)
                        print(self.tiles[xIndex][yIndex])
                    elif self.tiles[xIndex][yIndex].startswith('d'):
                        print(xIndex, yIndex, 3)
                        self.tiles[xIndex][yIndex] = self.tiles[xIndex][yIndex].replace('d', 'l', 1)
                    elif self.tiles[xIndex][yIndex].startswith('p'):
                        print(xIndex, yIndex, 3)
                        self.tiles[xIndex][yIndex] = self.tiles[xIndex][yIndex].replace('p', 'l', 1)
                    # elif self.tiles[xIndex][yIndex] == 'vs':
                    #     self.knight.update_position(9, 0)
                    #     self.level_array[kp_y][kp_x], self.level_array[9][0] = self.level_array[9][0], self.level_array[kp_y][kp_x]

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