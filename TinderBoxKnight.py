import copy

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
from pressureplate import PresurePlate
from spider import Spider

TITLE = "Tinder Box Knightf"

# Main game object
class Tinder_Box_Knight:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Tinder Box Knight")
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        WINDOW_WIDTH = self.screen.get_rect().width
        WINDOW_HEIGHT = self.screen.get_rect().height
        self.surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.BG_COLOR = floor.DARK_PURPLE
        self.keep_looping = True
        self.is_scanned = False
        self.scanned_tiles = []
        self.is_lit = False
        self.lit_tiles = []
        self.ranged_enemies = []
        self.level_number= 0
        self.flag_restart =0;#flag_restart: a flag to trigger the restart function("read_in_level") to reset level 
                             #flag_restart=1 => start trigger; flag_restart=0 => no trigger
        

    # Read user input
    def keydown_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.keep_looping = False
            elif event.type == pygame.KEYDOWN:
                self.is_scanned = False
                self.is_lit = False
                if event.key == pygame.K_q: 
                  self.keep_looping = False

                # Move right
                if event.key == pygame.K_RIGHT: 
                    safe_move = self.knight.move_right(self.level_array)
                    kp_y, kp_x = self.knight.return_position()
                    attacked, level = self.check_for_attack()
                    if attacked:
                        self.draw()
                        self.reset_knight(kp_y, kp_x, "Beware the eyes...", level)
                        self.lives_change(kp_y, kp_x)       #change the number of lives 
                    if not safe_move:
                        self.reset_knight(kp_y, kp_x, "You hit a spider!") 
                        self.level_array[kp_y][kp_x+1] = 'hs' 
                        self.lives_change(kp_y, kp_x)       #change the number of lives 
                        

                # Move left 
                if event.key == pygame.K_LEFT:
                    safe_move = self.knight.move_left(self.level_array)
                    kp_y, kp_x = self.knight.return_position()
                    attacked, level = self.check_for_attack()
                    if attacked:
                        self.draw()
                        self.reset_knight(kp_y, kp_x, "Beware the eyes...", level)
                        self.lives_change(kp_y, kp_x)       #change the number of lives 
                    if not safe_move:
                        self.reset_knight(kp_y, kp_x, "You hit a spider!")                      
                        self.level_array[kp_y][kp_x-1] = 'hs'  
                        self.lives_change(kp_y, kp_x)       #change the number of lives 
                    

                # Move up 
                if event.key == pygame.K_UP:
                    safe_move = self.knight.move_up(self.level_array)
                    kp_y, kp_x = self.knight.return_position()
                    attacked, level = self.check_for_attack()
                    if attacked:
                        self.draw()
                        self.reset_knight(kp_y, kp_x, "Beware the eyes...", level)
                        self.lives_change(kp_y, kp_x)       #change the number of lives 
                    if not safe_move:                     
                        self.reset_knight(kp_y, kp_x, "You hit a spider!") 
                        self.level_array[kp_y-1][kp_x] = 'hs' 
                        self.lives_change(kp_y, kp_x)       #change the number of lives 
                
                # Move down 
                if event.key == pygame.K_DOWN:
                    safe_move = self.knight.move_down(self.level_array)
                    kp_y, kp_x = self.knight.return_position()
                    attacked, level = self.check_for_attack()
                    if attacked:
                        self.draw()
                        self.reset_knight(kp_y, kp_x, "Beware the eyes...", level)
                        self.lives_change(kp_y, kp_x)       #change the number of lives 
                    if not safe_move:
                        self.reset_knight(kp_y, kp_x, "You hit a spider!")
                        self.level_array[kp_y+1][kp_x] = 'hs'
                        self.lives_change(kp_y, kp_x)       #change the number of lives 
                # Scan
                if event.key == pygame.K_s:
                    self.scanner = Scanner(self.level_array, self.original_array, self.scanned_tiles, self.knight.return_position())
                    self.is_scanned = True
                
                # Light and Open Gate 
                if event.key == pygame.K_f:
                    kp_y, kp_x = self.knight.return_position() 
                    self.light = Light(self.level_array, self.original_array, self.lit_tiles, self.knight.return_position())
                 
                    #Check to see if the player lit up a spider               
                    if self.spider.check_for_lit_spider(kp_y, kp_x):
                        self.reset_knight(kp_y, kp_x, "You lit up a spider!")
                        self.spider.reset_spider(kp_y, kp_x)
                        self.lives_change(kp_y, kp_x)       #change the number of lives
                        
                    else:
                        self.knight.previous_tile = self.light.previous_tile
                        print('previous tile: ', self.light.previous_tile)
                        self.level_array[kp_y][kp_x] = 'kl'
                        self.knight.next_tile = 'l'
                        self.is_lit = True

                # Open gate 
                if event.key == pygame.K_o:
                      # open gate(steping on the pressure plate)
                      PresurePlate(self.knight.return_position(),self.level_array,self.surface)
                

                # press SPACE to interactive with torch
                if event.key == pygame.K_SPACE:
                    kp_y, kp_x = self.knight.return_position()  # kp_y is knight's row, kp_y is knight's column
                    xlocation_torch,ylocation_torch,sate_torch = BigTorch().is_torch_lit(self.level_array) # check and retrun the state of troch, also retrun torch's row and column
                    flag_isnearby=BigTorch().is_near_torch(xlocation_torch,ylocation_torch,kp_x, kp_y) #check eligibility to interact with the torch
                    flag_finaltorch=BigTorch().change_torch_state (sate_torch,xlocation_torch,ylocation_torch,self.level_array,flag_isnearby) #change torch's pictures
                    if (flag_finaltorch==True): # if lit torch, play a related cutscene
                        BigTorch().play_lightcutscene()
                    # missing: all tiles change into visible

                if event.key == pygame.K_r:
                    self.read_in_level(self.level_number)


    def check_for_attack(self):
        for enemy in self.ranged_enemies: 
            attacked, level = enemy.ranged_attack(self.knight, self.level_array)
            if attacked:
                print("attacked")
                return True, level
        return False, 0

     # a function to change the number of lives
     # plyaer have 3 lives at first, meet a monster -> reduce a lives 
     # when plyer don't have enought lives, this level will be restart.
    def lives_change(self,kp_y,kp_x):
            y=len(self.level_array)      #get the column number of lives in tiles,true y location for lives tile is y-1
            x=len(self.level_array[y-1]) #get the row number of lives in tiles,true x location for lives tile is x-1
            w=self.screen.get_rect().width
            h=self.screen.get_rect().height
            root=tkinter.Tk()   #makesure only one accurate pop-up
            root.withdraw()     #makesure only one accurate pop-up
            if(self.level_array[y-1][x-1]=="ml3"):
                self.level_array[y-1][x-1] = self.level_array[y-1][x-1].replace("ml3","ml2",1)            #change lives tiles(3lives->2 lives)
            elif(self.level_array[y-1][x-1]=="ml2"):
                self.level_array[y-1][x-1] = self.level_array[y-1][x-1].replace("ml2","ml1",1)            #change lives tiles(2lives->1 lives)
            elif(self.level_array[y-1][x-1]=="ml1"):
                self.level_array[y-1][x-1] = self.level_array[y-1][x-1].replace("ml1","ml3",1)            #change lives tiles(1lives->3 lives)
                T=tkinter.messagebox.askokcancel("Tips","You have no lives! Do you want to retry a new level?")       #display a pop-up(option1)
                if(T):
                    self.flag_restart=1  # a flag to trigger the restart function in "update" (choose yes option)
                else:                    
                    self.flag_restart=1  ##!!!! if player choose no , it should return start or finish menu. delete this row code (else:) and write your connect code for menu 



    def update(self): 
        #flag_restart: a flag to trigger the restart function("read_in_level") to reset level 
        #flag_restart=1 => start trigger; flag_restart=0 => no trigger
        if(self.flag_restart==1):
            self.flag_restart=0
            self.read_in_level(self.level_number)
   

# Move knight back to starting square when they hit a spider 
    def reset_knight(self, kp_y, kp_x, message, level=None):
        self.draw() # to show whatever the player walked in to
        font = pygame.font.SysFont("arial", 16)
        caption = font.render(message, True, WHITE)
        self.caption_rect = pygame.Rect((kp_x+6) * TILESIZE, kp_y * TILESIZE, TILESIZE, TILESIZE)
        self.screen.blit(caption, self.caption_rect)
        pygame.display.flip()
        pygame.time.wait(1000)
        if level != None:
            self.level_array = level
        self.knight.reset_knight_position(self.level_array)


    # Read in level is its own function so that we can call it to read in different levels.
    def read_in_level(self, level_number):
        filepath = os.path.join("levels", self.levels[level_number])
        with open(filepath, "r") as f:
            csv_reader = csv.reader(f, delimiter=';')
            self.level_array = list(csv_reader)
            self.level_array = [x for x in self.level_array if x != []]
            self.original_array = copy.deepcopy(self.level_array)
        self.knight = Knight(11, 4)
        self.spider = Spider(self.level_array)
        self.create_monster_objects()
        #find and save positions for gates and pressure plates
        PresurePlate(self.knight.return_position(),self.level_array,self.surface)

    # Create array of monster objects
    def create_monster_objects(self):
        self.ranged_enemies.clear()
        for y in range(TILES_VERTICAL):
            for x in range(TILES_HORIZONTAL):
                if self.level_array[y][x] == "hre":
                    self.ranged_enemies.append(Ranged_Enemy(y, x, self.level_array))


# Draw new assets to screen
    def draw(self):
        self.surface.fill(self.BG_COLOR)
        self.tiles = Tiles(self.surface, self.level_array)
        self.tiles.draw(self.surface)
        # if self.is_lit:
        #     self.light.draw(self.surface)
        if self.is_scanned:
            self.scanner.draw(self.surface)
        font = pygame.font.SysFont('arial', 20)
        for scanned in self.scanned_tiles:
            text = font.render(str(scanned[1]), True, (255, 255, 255))
            self.surface.blit(text, scanned[0])
        pygame.display.update()

    def main(self):   
        #Level names are stored in a list
        self.levels = ['demolvl.txt']     
        #Call read_in_level with the index of the level that should be loaded.
        self.read_in_level(self.level_number)
        while self.keep_looping:
            self.clock.tick(30)
            self.keydown_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    mygame = Tinder_Box_Knight()
    mygame.main()
