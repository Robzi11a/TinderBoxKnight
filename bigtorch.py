# -*- coding: utf-8 -*-
import pygame
import os
import ctypes
import math

from tiles import TILES_HORIZONTAL,TILES_VERTICAL, TILES_HORIZONTAL, TILES_VERTICAL


class BigTorch:

    yIndex = 0
    xIndex = 0
    is_nearby = False

    def __init__(self, level_array):
        self.level_array = level_array

    # check the state of troch: ulit->torch_state=0; lit->torch_state=1
    def is_torch_lit(self, level_array):
        #count=0     # count number of light: init number = 0
        torch_state=-1
        for row_num, row in enumerate(level_array):
            for col_num, tile in enumerate(row):
                # divide into small elements in 1 line
                #if(count<1):        # permitted number of torch = 1
                if tile == 'vt':  # now state is visible unlit torch 
                    #count=count+1   # the number of torches that have been operated +1
                    self.xIndex = col_num
                    self.yIndex = row_num
                    torch_state = 0
                    return torch_state
            
        return -1 #represent no related torch
                

    # check the knight is near the troch: nearby->return True; not nearby->return Flase
    def is_near_torch(self, level_array, kp_x, kp_y):
        for yIndex in range(kp_y - 1, kp_y + 2):
            for xIndex in range(kp_x - 1, kp_x + 2):
                if -1 < yIndex < TILES_VERTICAL and -1 < xIndex < TILES_HORIZONTAL:
                    if level_array[yIndex][xIndex] == 'vt':
                        return True
        return False

    # change pictures and data of torch: 1. from ulit to lit 2.from lit to ulit
    def change_torch_state(self):
        self.level_array[self.yIndex][self.xIndex] = 'vlt'
        return True

                
# load level 2 when lit the torch
#    def next_level(self):
#        if self.torch_state == 'lit torch'
#                load lvl2
#           else: return False
        
