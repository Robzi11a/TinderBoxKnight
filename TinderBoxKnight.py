import pygame
import ground as floor
import os

from tiles import Tile 
from tiles import Tiles

from knight import Knight 
from knight import KnightPlacement

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
        self.MOVEMENT_UP = floor.MOVEMENT_UP
        self.MOVEMENT_RIGHT = floor.MOVEMENT_RIGHT
        self.MOVEMENT_DOWN = floor.MOVEMENT_DOWN
        self.MOVEMENT_LEFT = floor.MOVEMENT_LEFT
        self.MATCH_BUTTON = floor.MATCH_BUTTON
        self.SCAN_BUTTON = floor.SCAN_BUTTON
        self.inner = []
        #Create list of tiles
        self.tiles = Tiles(self.surface)

    # Read user input
    def keydown_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.keep_looping = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.keep_looping = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_up_button(mouse_pos)
                self._check_right_button(mouse_pos)
                self._check_down_button(mouse_pos)
                self._check_left_button(mouse_pos)
                self._check_light_button(mouse_pos)
                self._check_scan_button(mouse_pos)


    def get_tile(self, x, y):
        for elem in self.inner:
            if elem.x == x:
                if elem.y == y:
                    return elem
        return None

    def _check_up_button(self, mouse_pos):
        """player movement up"""
        button_clicked = self.MOVEMENT_UP.rect.collidepoint(mouse_pos)


    def _check_right_button(self, mouse_pos, surface):
        """player movement right"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)


    def _check_down_button(self, mouse_pos, surface):
        """player movement down"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)


    def _check_left_button(self, mouse_pos, surface):
        """player movement left"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)


    def _check_light_button(self, mouse_pos, surface):
        """player light tiles"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)


    def _check_scan_button(self, mouse_pos, surface):
        """player scan tiles"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

    def format_xy(self):
        for elem in self.inner:
            elem.x = round(elem.x)
            elem.y = round(elem.y)

    def has_collided(self, mouse_pos):
        for elem in self.inner:
            myrect = pygame.Rect(elem.x * TILESIZE, elem.y * TILESIZE, TILESIZE, TILESIZE)
            if myrect.collidepoint(mouse_pos[0], mouse_pos[1]) == 1:
                return elem.x, elem.y
        return None, None

    def update(self):
        pass

# Draw new assets to screen
    def draw(self):
        self.surface.fill(self.BG_COLOR)
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
