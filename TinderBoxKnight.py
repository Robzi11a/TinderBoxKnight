import pygame
import ground as floor
import os

from tiles import Tile 
from tiles import Tiles

from knight import Knight 
from knight import KnightPlacement

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
        self.knight = KnightPlacement(self.surface)

    def _current_knight_recorded(self, knight, x, y):
        # a knight is recorded 
        if not knight is None:
            self.knight.current_knight = knight
            self.tiles.current_tile = None
        else:
            self.tiles.current_tile = self.tiles.get_tile(x, y)

    def _not_current_knight_recorded(self, knight, x, y):
        # no monster is recorded
        if not knight is None:
            self.knight.current_knight = knight
            self.tiles.current_tile = None
        else:
            self.knight.current_knight = None
            self.tiles.current_tile = None

    def keydown_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.keep_looping = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.keep_looping = False
            elif event.type == pygame.MOUSEBUTTONUP:
                # check that x, y coord of knight
                self.knight.format_xy()

                mouse_pos = pygame.mouse.get_pos()
                x, y = self.tiles.has_collided(mouse_pos)
                knights = self.knight.get_knight(x, y)
                if not self.knight.current_knight is None:
                    self._current_knight_recorded(knights, x, y)
                else:
                    self._not_current_knight_recorded(knights, x, y)
                self.knight.debug_print()

    def update(self):
        if self.knight.current_knight == None or self.tiles.current_tile == None: return False
        self.knight.current_knight.move(self.tiles.current_tile.x, self.tiles.current_tile.y)

    def draw(self):
        self.surface.fill(self.BG_COLOR)
        self.tiles.draw(self.surface)
        self.knight.draw(self.surface)
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
