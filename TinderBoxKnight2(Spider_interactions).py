import copy

import pygame
import ground as floor
import os
import csv
import time

from tiles import Tile, Tiles
from scan import Scanner
from light import Light
from tiles import TILES_VERTICAL, TILES_HORIZONTAL, TILESIZE
from knight import Knight
from bigtorch import BigTorch
from utils import WHITE
from rangedenemy import Ranged_Enemy
from pressureplate import PresurePlate

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
        self.Ranged_Enemy = Ranged_Enemy(0, 0)
        self.ranged_enemies = []
        

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
                    if self.check_for_attack():
                        self.draw()
                    if not safe_move :
                        
                        kp_y, kp_x = self.knight.return_position()
                        self.reset_knight(kp_y, kp_x, "You hit a spider!")
                        self.draw()
                        pygame.time.wait(500)
                        self.level_array[kp_y][kp_x+1] = 'hs'#HIDING SPIDER
                        retryimg= pygame.image.load("Retrybutton.png") #RETRY IMAGE ADDED FOR LEFT UP RIGHT DOWN
                        resetx = self.screen.get_rect().width/2
                        resety = self.screen.get_rect().height/2
                        self.screen.blit(retryimg,(resetx,resety))
                        pygame.display.flip()
                        pygame.time.wait(2000)
                        '''self.keep_looping = False '''
                        '''to quit the game'''

                    self.check_for_attack()

                # Move left 
                if event.key == pygame.K_LEFT:
                    safe_move = self.knight.move_left(self.level_array)
                    if self.check_for_attack():
                        self.draw()
                    if not safe_move:
                        kp_y, kp_x = self.knight.return_position()
                        self.reset_knight(kp_y, kp_x, "You hit a spider!")   
                        self.draw()
                        pygame.time.wait(500)
                        self.level_array[kp_y][kp_x-1] = 'hs'  #HIDING SPIDER
                        retryimg= pygame.image.load("Retrybutton.png") #RETRY IMAGE ADDED FOR LEFT UP RIGHT DOWN
                        resetx = self.screen.get_rect().width/2
                        resety = self.screen.get_rect().height/2
                        self.screen.blit(retryimg,(resetx,resety))
                        pygame.display.flip()
                        pygame.time.wait(2000)        
                    self.check_for_attack()

                # Move up 
                if event.key == pygame.K_UP:
                    safe_move = self.knight.move_up(self.level_array)
                    kp_y, kp_x = self.knight.return_position()
                    if self.check_for_attack():
                        self.draw()
                        self.reset_knight(kp_y, kp_x, "Beware the eyes...")
                    if not safe_move:                     
                        self.reset_knight(kp_y, kp_x, "You hit a spider!")
                        self.draw()
                        pygame.time.wait(500)
                        self.level_array[kp_y-1][kp_x] = 'hs'  #HIDING SPIDER
                        retryimg= pygame.image.load("Retrybutton.png") #RETRY IMAGE ADDED FOR LEFT UP RIGHT DOWN
                        resetx = self.screen.get_rect().width/2
                        resety = self.screen.get_rect().height/2
                        self.screen.blit(retryimg,(resetx,resety))
                        pygame.display.flip()
                        pygame.time.wait(2000)
                        
                    
                
                # Move down 
                if event.key == pygame.K_DOWN:
                    safe_move = self.knight.move_down(self.level_array)
                    if self.check_for_attack():
                        self.draw()
                    if not safe_move:
                        kp_y, kp_x = self.knight.return_position()
                        self.reset_knight(kp_y, kp_x, "You hit a spider!") 
                        self.draw()
                        pygame.time.wait(500)
                        self.level_array[kp_y+1][kp_x] = 'hs'  #HIDING SPIDER
                        retryimg= pygame.image.load("Retrybutton.png") #RETRY IMAGE ADDED FOR LEFT UP RIGHT DOWN
                        resetx = self.screen.get_rect().width/2
                        resety = self.screen.get_rect().height/2
                        self.screen.blit(retryimg,(resetx,resety))
                        pygame.display.flip()
                        pygame.time.wait(2000)

                # RETRY BUTTON       
                if event.key == pygame.K_r:
                    self.draw()
                    self.knight.reset_knight_position(self.level_array)
                    self.is_scanned = False
                    self.scanned_tiles = []
                    self.is_lit = False
                    self.lit_tiles = []
                    self.Ranged_Enemy = Ranged_Enemy(0, 0)
                    self.ranged_enemies = []  
                    ''' Ranged enemy , lit tiles will need help '''
                         
                                    
                # Scan
                if event.key == pygame.K_s:
                    self.scanner = Scanner(self.level_array, self.original_array, self.scanned_tiles, self.knight.return_position())
                    self.is_scanned = True
                
                # Light and Open Gate 
                if event.key == pygame.K_f:
                    safe_moveup = self.knight.move_up(self.level_array)
                    safe_movedown = self.knight.move_down(self.level_array)
                    safe_moveleft = self.knight.move_left(self.level_array)
                    safe_moveright = self.knight.move_right(self.level_array)
                    kp_y, kp_x = self.knight.return_position() 
                    self.light = Light(self.level_array, self.original_array, self.lit_tiles, self.knight.return_position())
                    self.knight.previous_tile = self.light.previous_tile
                    print('previous tile: ', self.light.previous_tile)
                    self.level_array[kp_y][kp_x] = 'kl'
                    self.knight.next_tile = 'l'
                    self.is_lit = True
                    # open gate(steping on the pressure plate)
                    PresurePlate(self.knight.return_position(),self.level_array,self.surface)
                    presureplate = PresurePlate(self.knight.return_position(),self.level_array,self.surface)
                    
                    

                        
                    
                        
                    '''if(self.level_array[kp_y+1][kp_x] == 'vs'):
                    self.draw()
                    self.tiles.draw(self.surface)
                    kp_y, kp_x = self.knight.return_position()
                    self.reset_knight(kp_y, kp_x, "YOU LIT'UP A SPIDER")
                    resetimg = pygame.image.load("Retrybutton.png")
                    resetx = self.screen.get_rect().width/2
                    resety = self.screen.get_rect().height/2
                    self.screen.blit(resetimg,(resetx,resety))'''

                        
                        
                

                # press SPACE to interactive with torch
                if event.key == pygame.K_SPACE:
                    kp_y, kp_x = self.knight.return_position()  # kp_y is knight's row, kp_y is knight's column
                    xlocation_torch,ylocation_torch,sate_torch = BigTorch().is_torch_lit(self.level_array) # check and retrun the state of troch, also retrun torch's row and column
                    flag_isnearby=BigTorch().is_near_torch(xlocation_torch,ylocation_torch,kp_x, kp_y) #check eligibility to interact with the torch
                    flag_finaltorch=BigTorch().change_torch_state (sate_torch,xlocation_torch,ylocation_torch,self.level_array,flag_isnearby) #change torch's pictures
                    if (flag_finaltorch==True): # if lit torch, play a related cutscene
                        BigTorch().play_lightcutscene()
                    # missing: all tiles change into visible


    def check_for_attack(self):
        for i in range(6):
            if self.level_array[1][i] == "kl":
                self.Ranged_Enemy.ranged_attack(self.level_array, self.knight)
                return True

    def update(self): 
        pass

# Move knight back to starting square when they hit a spider 
    def reset_knight(self, kp_y, kp_x, message):
        font = pygame.font.SysFont("arial", 16)
        caption = font.render(message, True, WHITE)
        '''self.screen.fill((0,0,0))'''
        '''self.screen.blit(caption,[self.wINDOW_WIDTH/2,self.wINDOW_HEIGHT/2])'''
        self.caption_rect = pygame.Rect((kp_x + 6) * TILESIZE, kp_y * TILESIZE, TILESIZE, TILESIZE)
        self.screen.blit(caption, self.caption_rect)
        pygame.display.flip()
        pygame.time.wait(1000)
        self.knight.reset_knight_position(self.level_array)
        


    # Read in level is its own function so that we can call it to read in different levels.
    def read_in_level(self, level_number):
        filepath = os.path.join("levels", self.levels[level_number])
        with open(filepath, "r") as f:
            csv_reader = csv.reader(f, delimiter=';')
            self.level_array = list(csv_reader)
            self.level_array = [x for x in self.level_array if x != []]
            self.original_array = copy.deepcopy(self.level_array)
        self.knight = Knight(9, 0)
        self.create_monster_objects()
        #find and save positions for gates and pressure plates
        PresurePlate(self.knight.return_position(),self.level_array,self.surface)

    # Create array of monster objects
    def create_monster_objects(self):
        self.ranged_enemies.clear()
        for y in range(TILES_VERTICAL):
            for x in range(TILES_HORIZONTAL):
                if self.level_array[y][x] == "hre":
                    self.ranged_enemies.append(Ranged_Enemy(y, x))


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
        self.read_in_level(0)
        while self.keep_looping:
            self.clock.tick(30)
            self.keydown_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    mygame = Tinder_Box_Knight()
    mygame.main()
