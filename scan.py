import pygame.font

from tiles import TILES_VERTICAL, TILES_HORIZONTAL, TILESIZE

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
        kp_x, kp_y = self.position
        print("now position:", self.position)
        self.tip = pygame.Rect((kp_y + 6.4) * TILESIZE, (kp_x + 0.4) * TILESIZE, TILESIZE, TILESIZE)
        self.rect = pygame.Rect((kp_y + 6) * TILESIZE, kp_x * TILESIZE, TILESIZE, TILESIZE)
        for xIndex in range(kp_x - 1, kp_x + 1):
            for yIndex in range(kp_y - 1, kp_y + 1):
                print(xIndex, yIndex)
                if -1 < xIndex < TILES_VERTICAL and -1 < yIndex < TILES_HORIZONTAL:
                    if kp_x == xIndex and kp_y == yIndex:
                        continue
                    print("yes, ", xIndex, " < ", TILES_VERTICAL, " ", yIndex, " < ", TILES_HORIZONTAL)
                    if self.original_array[xIndex][yIndex] == 'hs':
                        self.count += 1
                    if self.tiles[xIndex][yIndex] == 'ls':
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

        text = font.render(label, True, (255, 255, 255))

        surface.blit(text, self.rect)
