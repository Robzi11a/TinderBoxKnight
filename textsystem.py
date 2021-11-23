import pygame
import ground as floor
import os
import csv
import time
from pygame import mixer

pygame.init()
from tiles import Tile, Tiles
from tiles import TILES_VERTICAL, TILES_HORIZONTAL

from knight import Knight

TITLE = "Tinder Box Knight"


# Main game object
class Tinder_Box_Knight:
    mixer.music.load('background2.wav')
    """ mixer.music bcos of bg music, for something short we will use mixer.sound"""
    mixer.music.play(-1)
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Tinder Box Knight")
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.wINDOW_WIDTH = self.screen.get_rect().width
        self.wINDOW_HEIGHT = self.screen.get_rect().height
        self.surface = pygame.display.set_mode((self.wINDOW_WIDTH, self.wINDOW_HEIGHT))
        self.BG_COLOR = floor.DARK_PURPLE
        
        self.keep_looping = True
        
    
    # Read user input
    def keydown_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.keep_looping = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.keep_looping = False

                    # Move right
                if event.key == pygame.K_RIGHT:
                    kp_y, kp_x = self.knight.return_position()  # kp_y is knight's row, kp_y is knight's column
                    if kp_x + 1 < TILES_HORIZONTAL:  # Check that the knight is not moving into a wall
                        movement_code = self.knight.check_move("right",
                                                               self.level_array)  # Check that the knight is making a valid move.
                        #  check_move returns 0 if the move is valid, 1 if the player has hit an enemy, and 2 if there is an object in the way.
                        if movement_code == 0:
                            self.level_array[kp_y][kp_x], self.level_array[kp_y][kp_x + 1] = "d", \
                                                                                             self.level_array[kp_y][
                                                                                                 kp_x]
                            self.knight.update_position(kp_y, kp_x + 1)
                        elif movement_code == 1:
                            self.level_array[kp_y][kp_x + 1] = 'ls'
                            self.reset_knight(kp_y, kp_x)
                            
                            
                            

                # Move left
                if event.key == pygame.K_LEFT:
                    kp_y, kp_x = self.knight.return_position()
                    if kp_x - 1 >= 0:
                        movement_code = self.knight.check_move("left", self.level_array)
                        if movement_code == 0:
                            self.level_array[kp_y][kp_x], self.level_array[kp_y][kp_x - 1] = "d", \
                                                                                             self.level_array[kp_y][
                                                                                                 kp_x]
                            self.knight.update_position(kp_y, kp_x - 1)
                        elif movement_code == 1:
                            self.level_array[kp_y][kp_x - 1] = 'ls'
                            self.reset_knight(kp_y, kp_x)

                # Move up
                if event.key == pygame.K_UP:
                    kp_y, kp_x = self.knight.return_position()
                    if kp_y - 1 >= 0:
                        movement_code = self.knight.check_move("up", self.level_array)
                        if movement_code == 0:
                            self.level_array[kp_y][kp_x], self.level_array[kp_y - 1][kp_x] = 'd', \
                                                                                             self.level_array[kp_y][
                                                                                                 kp_x]
                            self.knight.update_position(kp_y - 1, kp_x)
                        elif movement_code == 1:
                            self.level_array[kp_y - 1][kp_x] = 'ls'
                            self.reset_knight(kp_y, kp_x)

                # Move down
                if event.key == pygame.K_DOWN:
                    kp_y, kp_x = self.knight.return_position()
                    if kp_y + 1 < TILES_VERTICAL:
                        movement_code = self.knight.check_move("down", self.level_array)
                        if movement_code == 0:
                            self.level_array[kp_y][kp_x], self.level_array[kp_y + 1][kp_x] = 'd', \
                                                                                             self.level_array[kp_y][
                                                                                                 kp_x]
                            self.knight.update_position(kp_y + 1, kp_x)
                        elif movement_code == 1:
                            self.level_array[kp_y + 1][kp_x] = 'ls'
                            self.reset_knight(kp_y, kp_x)
    def gamename(self):
        font = pygame.font.SysFont("comicsansms", 30)
        caption = font.render("Welcome To The Game", True ,(255,255,255))
        '''self.screen.fill((0,0,0))'''
        self.screen.blit(caption,[self.wINDOW_WIDTH/2,self.wINDOW_HEIGHT/2])
        '''self.screen.blit(caption,[100,100])'''
        
        

    def rules(self):
        pygame.display.update()
        font = pygame.font.SysFont("verdana", 20)
        caption1 = font.render("E - EXIT", True ,(255,255,255))
        caption2 = font.render("S - SCAN", True ,(255,255,255))
        caption3 = font.render("P - PLAY", True ,(255,255,255))
        caption4 = font.render("R - RETRY ", True ,(255,255,255))
        caption5 = font.render("T - TRY ", True ,(255,255,255))
        self.screen.blit(caption1,[100,150])
        self.screen.blit(caption2,[100,190])
        self.screen.blit(caption3,[100,230])
        self.screen.blit(caption4,[100,270])
        self.screen.blit(caption5,[100,310])
        '''self.screen.fill((0,0,0))'''
        '''self.screen.blit(caption,[self.wINDOW_WIDTH/2,self.wINDOW_HEIGHT/2])'''
        '''self.screen.blit(caption,[100,100])'''
            
           
        
    def update(self):
        pass

    def reset_knight(self, kp_y, kp_x):
        
        
        font = pygame.font.SysFont("verdana", 20)
        caption = font.render("I'm hitting a spider", True ,(255,255,255))
        '''self.screen.fill((0,0,0))'''
        '''self.screen.blit(caption,[self.wINDOW_WIDTH/2,self.wINDOW_HEIGHT/2])'''
        self.screen.blit(caption,[100,100])
        pygame.display.flip()
        pygame.time.wait(1000)
        self.knight.update_position(9, 0)
        self.level_array[kp_y][kp_x], self.level_array[9][0] = self.level_array[9][0], self.level_array[kp_y][kp_x]

    # Draw new assets to screen
    def draw(self):
        self.surface.fill(self.BG_COLOR)
        self.tiles = Tiles(self.surface, self.level_array)
        self.tiles.draw(self.surface)
        
        
        pygame.display.update()

    def main(self):
        # Read in the level file. This is placed in main rather than init so that the game can be reset.
        filepath = os.path.join("levels", "demolvl.txt")
        with open(filepath, "r") as f:
            csv_reader = csv.reader(f, delimiter=';')
            self.level_array = list(csv_reader)
            self.level_array = [x for x in self.level_array if x != []]
        self.knight = Knight(9, 0)

        while self.keep_looping:
            self.clock.tick(30)
            self.keydown_events()
            self.update()
            self.draw()
a=Tinder_Box_Knight()
b=Tinder_Box_Knight()
a.gamename()
pygame.display.update()
''' update screen so name will be appearead'''
'''now that to stop it on screen put .wait'''
pygame.time.wait(3000)
b.rules()
pygame.display.flip()
pygame.time.wait(5000)
if __name__ == "__main__":
    mygame = Tinder_Box_Knight()
    mygame.main()
