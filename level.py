import copy
import tkinter
import tkinter.messagebox
import pygame
import ground as floor
import os
import csv
import time
import tkinter
import tkinter.messagebox

from tiles import Tile, Tiles
from scan import Scanner
from light import Light
from tiles import TILES_VERTICAL, TILES_HORIZONTAL, TILESIZE
from knight import Knight
from bigtorch import BigTorch
from utils import WHITE
from rangedenemy import Ranged_Enemy
from pressureplate import PressurePlate
from spider import Spider
from game import State


class Level(State):
    def __init__(self):   
        super().__init__()
        self.BG_COLOR = floor.DARK_PURPLE
        self.keep_looping = True
        self.is_scanned = False
        self.scanned_tiles = []
        self.is_lit = False
        self.lit_tiles = []
        self.ranged_enemies = []
        self.levels = ['demolvl.txt']
        self.reset = False
        self.display_text = False
        self.message = ''
        self.level_number= 0
        self.flag_restart =0;#flag_restart: a flag to trigger the restart function("read_in_level") to reset level 
                             #flag_restart=1 => start trigger; flag_restart=0 => no trigger
        self.scan_label = {}
        self.read_in_level(self.level_number)
        self.end_message = 'You have no lives left!'
        

    # Read user input
    def keydown_events(self, key):
        self.is_scanned = False
        self.is_lit = False

        if key == pygame.K_q:
            self.keep_looping = False
            self.next = floor.MAIN_MENU

        if key == pygame.K_RIGHT or key == pygame.K_LEFT or key == pygame.K_UP or key == pygame.K_DOWN:
            self.scan_label = {}

        # Move right
        if key == pygame.K_RIGHT: 
            safe_move = self.knight.move_right(self.level_array)
            kp_y, kp_x = self.knight.return_position()
            attacked, level = self.check_for_attack()
            if attacked:
                #self.draw()
                self.reset_knight(kp_y, kp_x, "Beware the eyes...", level)
                self.lives_change(kp_y, kp_x)
            if not safe_move:
                self.reset_knight(kp_y, kp_x, "You hit a spider!") 
                self.draw(self.surface, self.time_tick)        
                self.level_array[kp_y][kp_x+1] = 'hs'    
                self.lives_change(kp_y, kp_x)
                

        # Move left 
        if key == pygame.K_LEFT:
            safe_move = self.knight.move_left(self.level_array)
            kp_y, kp_x = self.knight.return_position()
            attacked, level = self.check_for_attack()
            if attacked:
               # self.draw()
                self.reset_knight(kp_y, kp_x, "Beware the eyes...", level)
                self.lives_change(kp_y, kp_x)
            if not safe_move:
                self.reset_knight(kp_y, kp_x, "You hit a spider!") 
                self.draw(self.surface, self.time_tick)                             
                self.level_array[kp_y][kp_x-1] = 'hs'        
                self.lives_change(kp_y, kp_x)
            

        # Move up 
        if key == pygame.K_UP:
            safe_move = self.knight.move_up(self.level_array)
            kp_y, kp_x = self.knight.return_position()
            attacked, level = self.check_for_attack()
            if attacked:
                self.draw(self.surface, self.time_tick)
                self.reset_knight(kp_y, kp_x, "Beware the eyes...", level)
                self.lives_change(kp_y, kp_x)
            if not safe_move:        
                self.reset_knight(kp_y, kp_x, "You hit a spider!")    
                self.draw(self.surface, self.time_tick)                 
                self.level_array[kp_y-1][kp_x] = 'hs'
                   
                self.lives_change(kp_y, kp_x)
        
        # Move down 
        if key == pygame.K_DOWN:
            safe_move = self.knight.move_down(self.level_array)
            kp_y, kp_x = self.knight.return_position()
            attacked, level = self.check_for_attack()
            if attacked:
                self.draw(self.surface, self, time_tick)
                self.reset_knight(kp_y, kp_x, "Beware the eyes...", level)
                self.lives_change(kp_y, kp_x)
            if not safe_move:
                self.reset_knight(kp_y, kp_x, "You hit a spider!")
                self.draw(self.surface, self.time_tick)        
                self.level_array[kp_y+1][kp_x] = 'hs'  
                self.lives_change(kp_y, kp_x)         
        # Scan
        if key == pygame.K_s:
            self.scanner = Scanner(self.level_array, self.original_array, self.scanned_tiles, self.knight.return_position())
            self.is_scanned = True
        
        # Light and Open Gate 
        if key == pygame.K_f:
            kp_y, kp_x = self.knight.return_position() 
            self.light = Light(self.level_array, self.original_array, self.lit_tiles, self.knight.return_position())
            attacked, level = self.check_for_attack()
            #Check to see if the player lit up a spider               
            if self.spider.check_for_lit_spider(kp_y, kp_x):
                self.reset_knight(kp_y, kp_x, "You lit up a spider!")
                self.draw(self.surface, self.time_tick)
                self.spider.reset_spider(kp_y, kp_x)
                self.lives_change(kp_y, kp_x)
            elif attacked:
                #self.draw()
                self.reset_knight(kp_y, kp_x, 'Beware the eyes...', level)
                self.lives_change(kp_y, kp_x)    
            else:
                self.knight.previous_tile = self.light.previous_tile
                print('previous tile: ', self.light.previous_tile)
                self.level_array[kp_y][kp_x] = 'kl'
                self.knight.next_tile = 'l'
                self.is_lit = True

        # Open gate 
        if key == pygame.K_o:
                # open gate(steping on the pressure plate)
                PresurePlate(self.knight.return_position(),self.level_array,self.surface)
        

        # press SPACE to interactive with torch
        if key == pygame.K_SPACE:
            kp_y, kp_x = self.knight.return_position()  # kp_y is knight's row, kp_y is knight's column
            state_torch = self.big_torch.is_torch_lit(self.level_array) # check and retrun the state of troch, also retrun torch's row and column
            
            flag_isnearby = self.big_torch.is_near_torch(self.level_array, kp_x, kp_y) #check eligibility to interact with the torch
            
            flag_finaltorch = self.big_torch.change_torch_state () #change torch's pictures
            self.end_message = 'You lit the torch!'
            self.display_text = True
            self.end_caption_rect = pygame.Rect(self.surface.get_height(), self.surface.get_width(), 100, 100)
            self.draw(self.surface, self.time_tick)
            pygame.time.wait(1000)
            self.keep_looping = False
            self.next = floor.MAIN_MENU
            
            

            # missing: all tiles change into visible

        if key == pygame.K_r:
            self.read_in_level(self.level_number)


    def check_for_attack(self):
        for enemy in self.ranged_enemies: 
            attacked, level = enemy.ranged_attack(self.knight, self.level_array)
            if attacked:
                print("attacked")
                return True, level
        return False, 0
    
    def update(self): 
        if(self.flag_restart==1):
            self.flag_restart=0
            self.read_in_level(self.level_number)

    # a function to change the number of lives
    # plyaer have 3 lives at first, meet a monster -> reduce a lives 
    # when plyer don't have enought lives, this level will be restart.
    def lives_change(self,kp_y,kp_x):
            #get the row number of lives in tiles,true x location for lives tile is x-1
            y, x = self.lives_tile
            h = self.surface.get_height()
            w = self.surface.get_width()
           
            if(self.level_array[y][x]=="ml3"):
                self.level_array[y][x] = self.level_array[y][x].replace("ml3","ml2",1)            #change lives tiles(3lives->2 lives)
            elif(self.level_array[y][x]=="ml2"):
                self.level_array[y][x] = self.level_array[y][x].replace("ml2","ml1",1)            #change lives tiles(2lives->1 lives)
            elif(self.level_array[y][x]=="ml1"):
                self.level_array[y][x] = self.level_array[y][x].replace("ml1","ml3",1)            #change lives tiles(1lives->3 lives)
                self.display_text = True
                self.end_caption_rect = pygame.Rect(self.surface.get_height()/2, self.surface.get_width()/2, 50, 50)
                self.draw(self.surface, self.time_tick)                            #display message1
                pygame.time.wait(1000)
                self.keep_looping = False
                self.next = floor.MAIN_MENU  # a flag to trigger the restart function in "update"

        


# Move knight back to starting square when they hit a spider 
    def reset_knight(self, kp_y, kp_x, message, level=None):
        
        self.caption_rect = pygame.Rect((kp_x+3) * TILESIZE, (kp_y-1) * TILESIZE, TILESIZE, TILESIZE)
        self.reset = True
        self.message = message
        if level != None:
            self.level_array = level


    # Read in level is its own function so that we can call it to read in different levels.
    def read_in_level(self, level_number):
        filepath = os.path.join("levels", self.levels[level_number])
        with open(filepath, "r") as f:
            csv_reader = csv.reader(f, delimiter=';')
            self.level_array = list(csv_reader)
            self.level_array = [x for x in self.level_array if x != []]
            self.original_array = copy.deepcopy(self.level_array)
        for row_num, row in enumerate(self.level_array):
            for col_num, element in enumerate(row):
                if element == 'kd':
                    self.knight = Knight(row_num, col_num)
        for row_num, row in enumerate(self.level_array):
            for col_num, element in enumerate(row):
                if element == 'ml3':
                    self.lives_tile = (row_num, col_num)
        self.spider = Spider(self.level_array)
        self.big_torch = BigTorch(self.level_array)
        self.create_monster_objects()
        #find and save positions for gates and pressure plates
        #self.pressure_plate = PressurePlate(self.knight.return_position(),self.level_array,self.surface)

    # Create array of monster objects
    def create_monster_objects(self):
        self.ranged_enemies.clear()
        for y in range(TILES_VERTICAL):
            for x in range(TILES_HORIZONTAL):
                if self.level_array[y][x] == "hre":
                    self.ranged_enemies.append(Ranged_Enemy(y, x, self.level_array))


# Draw new assets to screen
    def draw(self, surface, time_tick):
        surface.fill(self.BG_COLOR)
        self.tiles = Tiles(surface, self.level_array)
        self.tiles.draw(surface)
        # if self.is_lit:
        #     self.light.draw(self.surface)
        if self.is_scanned:
            self.scan_label = self.scanner.draw(surface)
            self.scan_label['timestamp'] = time_tick
        if self.scan_label and time_tick - self.scan_label['timestamp'] < 3000:
            surface.blit(self.scan_label['text'], self.scan_label['rect'])
        if self.reset:
            font = pygame.font.SysFont("arial", 16)
            caption = font.render(self.message, True, WHITE)
            surface.blit(caption, self.caption_rect)
            pygame.display.flip()
            pygame.time.wait(1000)
            self.knight.reset_knight_position(self.level_array)
            self.reset = False
        if self.display_text:
            font = pygame.font.SysFont("arial", 20)
            caption = font.render(self.end_message, True, WHITE)
            surface.blit(caption, self.end_caption_rect)
            pygame.display.flip()
        font = pygame.font.SysFont('arial', 20)
        for scanned in self.scanned_tiles:
            text = font.render(str(scanned[1]), True, (255, 255, 255))
            self.surface.blit(text, scanned[0])
        pygame.display.update()
      

    def startup(self, game_info):
        self.read_in_level(self.level_number)
        self.scanned_tiles = []

    def update(self, surface, key, time_tick):
        self.surface = surface
        self.time_tick = time_tick
        if not self.reset:
            self.keydown_events(key)
        self.draw(surface, time_tick)
