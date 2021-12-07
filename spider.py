from tiles import TILES_VERTICAL, TILES_HORIZONTAL

class Spider:
    def __init__(self, level_array):
        self.level_array = level_array
        self.spider_row = 0
        self.spider_column = 0

    def check_for_lit_spider(self, kp_y, kp_x):
        for yIndex in range(kp_y - 1, kp_y + 2):
            for xIndex in range(kp_x - 1, kp_x + 2):
                if -1 < yIndex < TILES_VERTICAL and -1 < xIndex < TILES_HORIZONTAL:
                    if self.level_array[yIndex][xIndex] == 'vs':
                        return True
        return False

    def reset_spider(self, kp_y, kp_x):
        for yIndex in range(kp_y - 1, kp_y + 2):
            for xIndex in range(kp_x - 1, kp_x + 2):
                if -1 < yIndex < TILES_VERTICAL and -1 < xIndex < TILES_HORIZONTAL:
                    if self.level_array[yIndex][xIndex] == 'vs':
                        self.level_array[yIndex][xIndex] = 'hs'
        return

