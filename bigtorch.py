# -*- coding: utf-8 -*-
import pygame
import os
import ctypes
import cv2  # a PyPl called opencv to play video (need download)
import math

from tiles import TILES_HORIZONTAL,TILES_VERTICAL


class BigTorch:
    def __init__(self):
        pass

    # check the state of troch: ulit->torch_state=0; lit->torch_state=1
    def is_torch_lit(self,level_array):
        count=0     # count number of light: init number = 0
        torch_state=-1
        self.level_array=level_array
        for i, myline in enumerate(self.level_array):     # divide into samll lines in 2-dimensional list
            for j, elem in enumerate(myline):     # divide into samll elements in 1 line
                if(count<1):        # permitted number of torch = 1
                    if elem == "vut":  # now state is visible unlit torch 
                        count=count+1   # the number of torches that have been operated +1
                        torch_xlocation = j
                        torch_ylocation = i
                        torch_state=0
                        return torch_xlocation,torch_ylocation, torch_state
                    elif elem == "vlt":
                        count=count+1   # the number of torches that have been operated +1
                        torch_xlocation = j
                        torch_ylocation = i
                        torch_state=1
                        return torch_xlocation,torch_ylocation, torch_state
                    else : return -1,-1,-1 #represent no related torch
                

    # check the knight is near the troch: nearby->return True; not nearby->return Flase
    def is_near_torch(self,torch_xlocation,torch_ylocation,kight_xlocation,kight_ylocation):
        self.torch_xlocation=torch_xlocation
        self.torch_ylocation=torch_ylocation
        self.kight_xlocation=kight_xlocation
        self.kight_ylocation=kight_ylocation
        if((self.torch_xlocation==self.kight_xlocation) and (self.torch_ylocation+1==self.kight_ylocation))\
          or ((self.torch_xlocation==self.kight_xlocation) and (self.torch_ylocation-1==self.kight_ylocation))\
          or ((self.torch_xlocation+1==self.kight_xlocation) and (self.torch_ylocation==self.kight_ylocation))\
          or ((self.torch_xlocation+1==self.kight_xlocation) and (self.torch_ylocation+1==self.kight_ylocation))\
          or ((self.torch_xlocation+1==self.kight_xlocation) and (self.torch_ylocation-1==self.kight_ylocation))\
          or ((self.torch_xlocation-1==self.kight_xlocation) and (self.torch_ylocation==self.kight_ylocation))\
          or ((self.torch_xlocation-1==self.kight_xlocation) and (self.torch_ylocation+1==self.kight_ylocation))\
          or ((self.torch_xlocation-1==self.kight_xlocation) and (self.torch_ylocation-1==self.kight_ylocation)):
            return True
        else : return False

    # change pictures and data of torch: 1. from ulit to lit 2.from lit to ulit
    def change_torch_state(self,torch_state,torch_xlocation,torch_ylocation,level_array,flag_isnearby):
        self.torch_state=torch_state
        self.torch_xlocation=torch_xlocation
        self.torch_ylocation=torch_ylocation
        self.level_array=level_array
        self.flag_isnearby=flag_isnearby
        if (self.torch_state>=0) and (self.flag_isnearby==True):    
            i= self.level_array[self.torch_ylocation]
            del i[self.torch_xlocation]
            if self.torch_state == 0:
                i.insert(self.torch_xlocation,"vlt")
                return True
            elif (self.torch_state == 1):
                i.insert(self.torch_xlocation,"vut")
            else: return False

   # after lit torch, play a related cutscene (must add opencv PyPl then import cv2)
    def play_lightcutscene(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        WINDOW_WIDTH = self.screen.get_rect().width
        WINDOW_HEIGHT = self.screen.get_rect().height
        video_path = os.path.join("levels", "cutscenes","LightTorch.mp4")  #500X300(WIDTH X HEIGHT)
        cap = cv2.VideoCapture(video_path)
        while(cap.isOpened()): 
            ret,frame = cap.read()
            ret_flag=0
            if((ret == True) and (ret_flag == 0)):
                cv2.imshow('lit torch',frame) 
                cv2.moveWindow('lit torch',math.ceil(WINDOW_WIDTH/3),math.ceil(WINDOW_HEIGHT/3))
                k = cv2.waitKey(30)
                #press q and quit
                if (k & 0xff == ord('q')): 
                    ret = False
                    break
            elif((ret == False) or (ret_flag == 1)):
                ret_flag=0
                cap.release()
                cv2.destroyAllWindows()
            else: print("light_torch video meets error! ")
                

        
