import pygame.font

from tiles import TILES_VERTICAL, TILES_HORIZONTAL, TILESIZE

pygame.font.init()


class Scanner:
    def __init__(self, level_array, original_array, position, surface):
        self.current = None
        self.tiles = level_array
        self.position = position
        self.surface = surface
        self.original_array = original_array
        self.count = 0
        self.scan()

    def scan(self):
        kp_x, kp_y = self.position
        print("now position:", self.position)
        self.rect = pygame.Rect((kp_y + 6) * TILESIZE, (kp_x) * TILESIZE, TILESIZE, TILESIZE)
        for xIndex in range(kp_x - 2, kp_x + 3):
            for yIndex in range(kp_y - 2, kp_y + 3):
                print(xIndex, yIndex)
                if -1 < xIndex < TILES_VERTICAL and -1 < yIndex < TILES_HORIZONTAL + 1:
                    if kp_x == xIndex and kp_y == yIndex:
                        continue
                    print("yes, ", xIndex, " < ", TILES_VERTICAL, " ", yIndex, " < ", TILES_HORIZONTAL)
                    if self.original_array[xIndex][yIndex] == 'hs':
                        self.count += 1
                    self.tiles[xIndex][yIndex] = 'st'

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

        self.surface.blit(text, self.rect)
