import pygame.font

from tiles import TILES_VERTICAL, TILES_HORIZONTAL, TILESIZE
from utils import WHITE
import ground as c

pygame.font.init()


class Scanner:
    def __init__(self, level_array, original_array, scanned_tiles, position):
        self.current = None
        self.tiles = level_array
        self.position = position
        self.scanned_tiles = scanned_tiles
        self.original_array = original_array
        self.count = 0
        self.scan()

    def scan(self):
        kp_y, kp_x = self.position
        print("now position:", kp_y, kp_x, TILESIZE)
        horizontal = (c.WINDOW_WIDTH - TILES_HORIZONTAL * TILESIZE) / 2 + (kp_x + 0.2) * TILESIZE
        vertical = (kp_y + 0.5) * TILESIZE
        self.tip = pygame.Rect(horizontal, vertical, TILESIZE, TILESIZE)
        self.rect = pygame.Rect(horizontal, vertical - TILESIZE * 0.8, TILESIZE, TILESIZE)
        for yIndex in range(kp_y - 2, kp_y + 3):
            for xIndex in range(kp_x - 2, kp_x + 3):
                if -1 < yIndex < TILES_VERTICAL and -1 < xIndex < TILES_HORIZONTAL:
                    if kp_x == xIndex and kp_y == yIndex:
                        continue
                    if self.original_array[yIndex][xIndex] == 'hs':
                        self.count += 1
                    if self.tiles[yIndex][xIndex] == 'vs':
                        continue
                    # self.tiles[xIndex][yIndex] = 'st'
        self.scanned_tiles.append([self.tip, self.count])

    def update(self):
        pass

    def draw(self, surface):
        font = pygame.font.SysFont('arial', 16)
        label = ""
        if self.count > 1:
            label = "There are " + str(self.count) + " enemies around."
        else:
            label = "There is " + str(self.count) + " enemy around."

        return {'text': font.render(label, True, WHITE), 'rect': self.rect}
