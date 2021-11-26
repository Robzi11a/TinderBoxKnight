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

TITLE = "Tinder Box Knight"

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
                    if not safe_move:
                        kp_y, kp_x = self.knight.return_position()
                        self.reset_knight(kp_y, kp_x)                            

                # Move left 
                if event.key == pygame.K_LEFT:
                    safe_move = self.knight.move_left(self.level_array)
                    if not safe_move:
                        kp_y, kp_x = self.knight.return_position()
                        self.reset_knight(kp_y, kp_x)                  

                # Move up 
                if event.key == pygame.K_UP:
                    safe_move = self.knight.move_up(self.level_array)
                    if not safe_move:
                        kp_y, kp_x = self.knight.return_position()
                        self.reset_knight(kp_y, kp_x)
                
                # Move down 
                if event.key == pygame.K_DOWN:
                    safe_move = self.knight.move_down(self.level_array)
                    if not safe_move:
                        kp_y, kp_x = self.knight.return_position()
                        self.reset_knight(kp_y, kp_x)
                
                # Scan
                if event.key == pygame.K_s:
                    self.scanner = Scanner(self.level_array, self.original_array, self.scanned_tiles, self.knight.return_position())
                    self.is_scanned = True
                
                # Light
                if event.key == pygame.K_f:
                    kp_y, kp_x = self.knight.return_position() 
                    self.light = Light(self.level_array, self.original_array, self.lit_tiles, self.knight.return_position())
                    self.level_array[kp_y][kp_x] = 'kl'
                    self.knight.next_tile = 'l'
                    self.knight.previous_tile = 'l'
                    self.is_lit = True


                # press SPACE to interactive with torch
                if event.key == pygame.K_SPACE:
                    kp_y, kp_x = self.knight.return_position()  # kp_y is knight's row, kp_y is knight's column
                    xlocation_torch,ylocation_torch,sate_torch = BigTorch().is_torch_lit(self.level_array) # check and retrun the state of troch, also retrun torch's row and column
                    flag_isnearby=BigTorch().is_near_torch(xlocation_torch,ylocation_torch,kp_x, kp_y) #check eligibility to interact with the torch
                    flag_finaltorch=BigTorch().change_torch_state (sate_torch,xlocation_torch,ylocation_torch,self.level_array,flag_isnearby) #change torch's pictures
                    if (flag_finaltorch==True): # if lit torch, play a related cutscene
                        BigTorch().play_lightcutscene()
                    # missing: all tiles change into visible


    def update(self):
        pass

# Move knight back to starting square when they hit a spider 
    def reset_knight(self, kp_y, kp_x):
        font = pygame.font.SysFont("arial", 16)
        caption = font.render("You hit a spider!", True, WHITE)
        '''self.screen.fill((0,0,0))'''
        '''self.screen.blit(caption,[self.wINDOW_WIDTH/2,self.wINDOW_HEIGHT/2])'''
        self.caption_rect = pygame.Rect((kp_x + 6) * TILESIZE, kp_y * TILESIZE, TILESIZE, TILESIZE)
        self.screen.blit(caption, self.caption_rect)
        pygame.display.flip()
        pygame.time.wait(1000)
        self.knight.reset_knight_position(self.level_array)


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
        # Read in the level file. This is placed in main rather than init so that the game can be reset.
        filepath = os.path.join("levels", "demolvl.txt")
        with open(filepath, "r") as f:
            csv_reader = csv.reader(f, delimiter=';')
            self.level_array = list(csv_reader)
            self.level_array = [x for x in self.level_array if x != []]
            self.original_array = copy.deepcopy(self.level_array)
        self.knight = Knight(9, 0)

        while self.keep_looping:
            self.clock.tick(30)
            self.keydown_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    mygame = Tinder_Box_Knight()
    mygame.main()
