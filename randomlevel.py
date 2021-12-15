import csv
import os
import random

from tiles import TILES_HORIZONTAL, TILES_VERTICAL


class RandomLevel:
    def __init__(self, difficulty, levels):
        self.difficulty = difficulty
        self.spider_num = 0
        self.spider_clue = 0
        self.range_num = 0
        self.range_clue = 0
        self.levels = levels
        self.level_array = []
        self.empty_tile = []

        self.set_enemy_num()
        self.read_random_level()
        self.set_enemy()

    def read_random_level(self):
        level_number = random.randint(0, len(self.levels) - 1)
        # level_number = 1
        filepath = os.path.join("levels", self.levels[level_number])
        spider_and_clue = ["lss", "lsr", "lsa", "lwsr", "lwsa", "hs"]
        ranged_and_clue = ["lwsa", "hre"]
        with open(filepath, "r") as f:
            csv_reader = csv.reader(f, delimiter=';')
            self.level_array = list(csv_reader)
            self.level_array = [x for x in self.level_array if x != []]
        for row_num, row in enumerate(self.level_array):
            for col_num, element in enumerate(row):
                if element in spider_and_clue or element in ranged_and_clue:
                    self.level_array[row_num][col_num] = "d"
                    self.empty_tile.append([row_num, col_num])
                elif element == "d":
                    self.empty_tile.append([row_num, col_num])

    def set_enemy_num(self):
        if self.difficulty == -1:
            self.spider_num = 5
            self.spider_clue = 2
            self.range_num = 1
            self.range_clue = 1
        elif self.difficulty == -2:
            self.spider_num = 7
            self.spider_clue = 3
            self.range_num = 2
            self.range_clue = 1
        elif self.difficulty == -3:
            self.spider_num = 9
            self.spider_clue = 4
            self.range_num = 3
            self.range_clue = 1

    def set_enemy(self):
        for i in range(0, self.spider_num):
            flag = False
            while not flag and len(self.empty_tile) > 0:
                index = random.randrange(0, len(self.empty_tile))
                x = self.empty_tile[index][0]
                y = self.empty_tile[index][1]
                flag = self.check_can_put_enemy(x, y)
                if flag:
                    self.level_array[x][y] = "hs"
                    self.empty_tile.remove(self.empty_tile[index])
                    i = i - 1
                    spider_clue = ["lss", "lsr", "lsa", "lwsr", "lwsa"]
                    if self.spider_clue > 0:
                        if x - 1 > 0 and self.empty_tile.count([x - 1, y]) > 0:
                            self.level_array[x - 1][y] = random.choice(spider_clue)
                            self.empty_tile.remove([x - 1, y])
                            self.spider_clue = self.spider_clue - 1
                        elif x + 1 < TILES_VERTICAL and self.empty_tile.count([x + 1, y]) > 0:
                            self.level_array[x + 1][y] = random.choice(spider_clue)
                            self.empty_tile.remove([x + 1, y])
                            self.spider_clue = self.spider_clue - 1
                        elif y - 1 > 0 and self.empty_tile.count([x, y - 1]) > 0:
                            self.level_array[x][y - 1] = random.choice(spider_clue)
                            self.empty_tile.remove([x, y - 1])
                            self.spider_clue = self.spider_clue - 1
        # for j in range(0, self.range_num):
        #     flag = False
        #     while not flag and len(self.empty_tile) > 0:
        #         index = random.randint(0, len(self.empty_tile))
        #         x = self.empty_tile[index][0]
        #         y = self.empty_tile[index][1]
        #         flag = self.check_can_put_enemy(x, y)
        #         if flag:
        #             self.level_array[x][y] = "hre"
        #             self.empty_tile.remove(self.empty_tile[index])
        #             j = j - 1

    def check_can_put_enemy(self, x, y):
        gtd = ["hcg", "ht", "dpp"]
        ll = y == 0 or x == TILES_VERTICAL - 2 \
             or self.level_array[x + 1][y - 1].startswith('h') or self.level_array[x + 1][y - 1].startswith('v') \
             or self.level_array[x + 1][y - 1] in gtd
        lr = y == TILES_HORIZONTAL - 1 or x == TILES_VERTICAL - 2 \
             or self.level_array[x + 1][y + 1].startswith('h') or self.level_array[x + 1][y + 1].startswith('v') \
             or self.level_array[x + 1][y + 1] in gtd
        ul = y == 0 or x == 0 \
             or self.level_array[x - 1][y - 1].startswith('h') or self.level_array[x - 1][y - 1].startswith('v') \
             or self.level_array[x - 1][y - 1] in gtd
        ur = y == TILES_HORIZONTAL - 1 or x == 0 \
             or self.level_array[x - 1][y + 1].startswith('h') or self.level_array[x - 1][y + 1].startswith('v') \
             or self.level_array[x - 1][y + 1] in gtd
        lower = x == TILES_VERTICAL - 2 \
                or self.level_array[x + 1][y].startswith('h') or self.level_array[x + 1][y].startswith('v') \
                or self.level_array[x + 1][y] in gtd
        upper = x == 0 \
                or self.level_array[x - 1][y].startswith('h') or self.level_array[x - 1][y].startswith('v') \
                or self.level_array[x - 1][y] in gtd
        left = y == 0 or self.level_array[x][y - 1].startswith('h') or self.level_array[x][y - 1].startswith('v') \
                or self.level_array[x][y - 1] in gtd
        right = y == TILES_HORIZONTAL - 1 \
                or self.level_array[x][y + 1].startswith('h') or self.level_array[x][y + 1].startswith('v') \
                or self.level_array[x][y - 1] in gtd
        if (ll and lr) or (ul and ur) or (lower and upper) or (left and right):
            return False
        else:
            return True
