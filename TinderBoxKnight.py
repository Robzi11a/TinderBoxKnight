import pygame
import ground as floor
import os
import csv
import time

from tiles import Tile 
from tiles import Tiles
from tiles import TILES_VERTICAL, TILES_HORIZONTAL

from knight import Knight

TITLE = "Tinder Box Knight"

#Main game object
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
                    kp_y, kp_x = self.knight.return_position() # kp_y is knight's row, kp_y is knight's column
                    if kp_x+1 < TILES_HORIZONTAL: # Check that the knight is not moving into a wall
                        movement_code = self.knight.check_move("right", self.level_array) #Check that the knight is making a valid move.
                         #  check_move returns 0 if the move is valid, 1 if the player has hit an enemy, and 2 if there is an object in the way.
                        if movement_code == 0: 
                            self.level_array[kp_y][kp_x], self.level_array[kp_y][kp_x+1] = "d", self.level_array[kp_y][kp_x]
                            self.knight.update_position(kp_y, kp_x+1)
                        elif movement_code == 1:
                            self.end_game()
                
                # Move left 
                if event.key == pygame.K_LEFT:
                    kp_y, kp_x = self.knight.return_position()
                    if kp_x-1 >= 0: 
                        movement_code = self.knight.check_move("left", self.level_array)
                        if movement_code == 0:
                            self.level_array[kp_y][kp_x], self.level_array[kp_y][kp_x-1] = "d", self.level_array[kp_y][kp_x]
                            self.knight.update_position(kp_y, kp_x-1)  
                        elif movement_code == 1:
                            self.end_game()

                # Move up 
                if event.key == pygame.K_UP:
                    kp_y, kp_x = self.knight.return_position()
                    if kp_y - 1 >= 0: 
                        movement_code = self.knight.check_move("up", self.level_array)
                        if movement_code == 0:    
                            self.level_array[kp_y][kp_x], self.level_array[kp_y-1][kp_x] = 'd', self.level_array[kp_y][kp_x]
                            self.knight.update_position(kp_y-1, kp_x)
                        elif movement_code == 1:
                            self.end_game()
                                
                # Move down 
                if event.key == pygame.K_DOWN:
                    kp_y, kp_x = self.knight.return_position()
                    if kp_y + 1 < TILES_VERTICAL: 
                        movement_code = self.knight.check_move("down", self.level_array)
                        if movement_code == 0:
                            self.level_array[kp_y][kp_x], self.level_array[kp_y+1][kp_x] = 'd', self.level_array[kp_y][kp_x]
                            self.knight.update_position(kp_y+1, kp_x)
                        elif movement_code == 1:
                            self.end_game()
                            
    def update(self):
        pass

    def end_game(self):
        self.main()

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

if __name__ == "__main__":
    mygame = Tinder_Box_Knight()
    mygame.main()
