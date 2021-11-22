import pygame
import ground as floor
import os
import csv

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
        filepath = os.path.join("levels", "demolvl.txt")
        with open(filepath, "r") as f:
            csv_reader = csv.reader(f, delimiter=';')
            self.level_array = list(csv_reader)
            self.level_array = [x for x in self.level_array if x != []]
        self.knight = Knight(9, 0)

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
                    # kp_y is knight's row, kp_y is knight's column
                    kp_y, kp_x = self.knight.return_position()
                    if kp_x+1 < TILES_HORIZONTAL: 
                        self.level_array[kp_y][kp_x], self.level_array[kp_y][kp_x+1] = self.level_array[kp_y][kp_x+1], self.level_array[kp_y][kp_x]
                        self.knight.update_position(kp_y, kp_x+1)
                # Move left 
                if event.key == pygame.K_LEFT:
                    kp_y, kp_x = self.knight.return_position()
                    if kp_x-1 >= 0: 
                        self.level_array[kp_y][kp_x], self.level_array[kp_y][kp_x-1] = self.level_array[kp_y][kp_x-1], self.level_array[kp_y][kp_x]
                        self.knight.update_position(kp_y, kp_x-1)  

                # Move up 
                if event.key == pygame.K_UP:
                    kp_y, kp_x = self.knight.return_position()
                    if kp_y - 1 >= 0: 
                        self.level_array[kp_y][kp_x], self.level_array[kp_y-1][kp_x] = self.level_array[kp_y-1][kp_x], self.level_array[kp_y][kp_x]
                        self.knight.update_position(kp_y-1, kp_x)

                # Move down 
                if event.key == pygame.K_DOWN:
                    kp_y, kp_x = self.knight.return_position()
                    if kp_y + 1 < TILES_VERTICAL: 
                        self.level_array[kp_y][kp_x], self.level_array[kp_y+1][kp_x] = self.level_array[kp_y+1][kp_x], self.level_array[kp_y][kp_x]
                        self.knight.update_position(kp_y+1, kp_x)
    def update(self):
        pass

# Draw new assets to screen
    def draw(self):
        self.surface.fill(self.BG_COLOR)
        self.tiles = Tiles(self.surface, self.level_array)
        self.tiles.draw(self.surface)
        pygame.display.update()

    def main(self):
        while self.keep_looping:
            self.clock.tick(30)
            self.keydown_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    mygame = Tinder_Box_Knight()
    mygame.main()
