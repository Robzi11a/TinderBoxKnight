#!/usr/bin/env python

# -*- coding: utf-8 -*

"""

pressureplate

~~~~~~~~~~~~~~~~

Function: A module to open the gates when players steps on the pressure plate tile. 

Current button design: Using keyborad 'o' to interactive with the pressure plate tile when player stand at the pressure plate tile.    

Tips: Can add more than 1 gate in a level.
      But the number of gate tiles must equal the number of the pressure plate tiles

"""
import pygame
from tiles import TILES_VERTICAL, TILES_HORIZONTAL, TILESIZE
from utils import WHITE

# a list to store the location data (y,x) for pressure plates
PP_LOCATION=[]
# a list to store the location data (y,x) for gates
G_LOCATION=[]
# max number of gates in one level
MAX_GATENUMBER=1 
# a flag to count dealed number for gates: start from 0 and less than MAX_GATENUMBER
COUNT_GATENUMBER=0 


class PressurePlate:
    """
    Provides a interaction for pressure plate tiles to open gates.
    def __init__(self, position,level_array,surface): stores transferd data and performs the "find_position()" and the "check_pressure()". no return.
    def check_pressure(self): checks whether the player stands at and steps on the pressure plates. if yes, carrys on the "open_gate(i)". no return.
    def open_gate(self,i): changes the current closed gate tile into the related open gate tile and performs the "draw()".no return.
    def find_position(self):finds and stores x,y positions for the pressure plates and the gates. no return.
    def draw(self): add text when open the gate, no return.
    """

    def __init__(self, position, level_array):
        # a list to store the location data (y,x) for pressure plates
        self.PP_LOCATION=[]
        
        # a list to store the location data (y,x) for gates
        self.G_LOCATION=[]
        
        # max number of gates in one level
        self.MAX_GATENUMBER=1 
        
        # a flag to count dealed number for gates: start from 0 and less than MAX_GATENUMBER
        self.COUNT_GATENUMBER=0 
        
        # a current x,y location data for player (knight)
        self.py, self.px= position
        # a list to store the data for a level
        self.level_array=level_array
        self.is_gate_open = False
        # a return param from initialized display interface
       # self.surface=surface
        # only when dealed number for gates < max mumber for gates, finding position for the pressure plates and gates
        if (self.COUNT_GATENUMBER<self.MAX_GATENUMBER):
            self.find_position()
            self.COUNT_GATENUMBER+=1
        #self.check_pressure(kp_y, kp_x)

    #check whether satify the conditions to open gate.
    #2condiitons: 1.plyaer's x,ylocation = pressureplate's x,yloacation
    #             2.this pressure plate should be visible
    def check_pressure(self, kp_y, kp_x):
        for i in range(len(self.G_LOCATION)):
            if (kp_x==self.PP_LOCATION[i][1]) and (kp_y==self.PP_LOCATION[i][0]):
                self.open_gate(i)

    # change data for gate tiles. 
    # 2 options: 1.when the current gate tile is "vcg"=>changes into "log"
    #            2.when the current gate tile is "hcg"=>changes into "hog"
    def open_gate(self,i):
        if self.level_array[self.G_LOCATION[i][0]][self.G_LOCATION[i][1]]=="vcg":
            self.level_array[self.G_LOCATION[i][0]][self.G_LOCATION[i][1]] = self.level_array[self.G_LOCATION[i][0]][self.G_LOCATION[i][1]].replace("vcg","log",1)
            self.is_gate_open = True
        elif self.level_array[self.G_LOCATION[i][0]][self.G_LOCATION[i][1]]=="hcg":
            self.level_array[self.G_LOCATION[i][0]][self.G_LOCATION[i][1]] = self.level_array[self.G_LOCATION[i][0]][self.G_LOCATION[i][1]].replace("hcg","dog",1)
            self.is_gate_open = True
        else: pass
        #self.draw()
    
    #find and store the x,y position for gates and pressure plates
    def find_position(self):
        # ppx,ppy are x,y loacation for pressure plates
        #gx,gy are x,y loacation for gates
        ppx,ppy,gx,gy=-1,-1,-1,-1
        #county: now is the number of list (y direction)
        county = -1
        for line in self.level_array:
            county += 1
            #countx: now is the number of row (x direction)
            countx =-1
            for j in line:
                countx += 1
                if (j=="dpp") or (j=="lpp"):
                    ppx = countx
                    ppy = county
                    self.PP_LOCATION.append([ppy,ppx])
                    #print("ppx is",self.ppx,"ppy is",self.ppy)
                if (j=="hcg") or (j=="vcg"):
                    gx = countx
                    gy = county
                    self.G_LOCATION.append([gy,gx])

    # add text when the player steps the pressure plate to open the gate
    """
    def draw(self):
        pygame.font.init()
        font = pygame.font.SysFont('arial', 16)
        label = "The gate is opened!"
        text = font.render(label, True, WHITE)
        self.rect = pygame.Rect((self.px + 3) * TILESIZE, (self.py-1) * TILESIZE, TILESIZE, TILESIZE)
        self.surface.blit(text, self.rect)
        pygame.display.flip()
        pygame.time.wait(1000)
        """