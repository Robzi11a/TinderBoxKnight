import pygame
import ground as floor
import os

from tiles import Tile 
from tiles import Tiles

TITLE = "Tinder Box Knight"

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
        self.tiles = Tiles(self.surface)

    def keydown_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.keep_looping = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.keep_looping = False

    def update(self):
        pass

    def draw(self):
        self.surface.fill(self.BG_COLOR)
        self.tiles.draw(self.surface)
        pygame.display.update()

    def main(self):
        while self.keep_looping:
            self.keydown_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    mygame = Tinder_Box_Knight()
    mygame.main()
