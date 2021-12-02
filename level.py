import copy
import csv
import os

import pygame
import ground as floor
from bigtorch import BigTorch

from game import State
from knight import Knight
from light import Light
from rangedenemy import Ranged_Enemy
from scan import Scanner
from tiles import TILESIZE, TILES_VERTICAL, TILES_HORIZONTAL, Tiles
from utils import WHITE


class Level(State):
    def __init__(self):
        super().__init__()
        self.BG_COLOR = floor.DARK_PURPLE
        self.keep_looping = True
        self.is_scanned = False
        self.scanned_tiles = []
        self.is_lit = False
        self.lit_tiles = []
        self.Ranged_Enemy = Ranged_Enemy(0, 0)
        self.ranged_enemies = []
        self.levels = ['demolvl.txt']
        self.reset = False
        self.message = ''
        self.next = floor.LEVEL
        self.scan_label = {}

        self.read_in_level(0)

    # Read user input
    def keydown_events(self, key):
        self.is_scanned = False
        self.is_lit = False

        if key == pygame.K_q:
            self.keep_looping = False
            self.next = floor.MAIN_MENU

        if key == pygame.K_RIGHT or key == pygame.K_LEFT or key == pygame.K_UP or key == pygame.K_DOWN:
            self.scan_label = {}

        # Move right
        if key == pygame.K_RIGHT:
            safe_move = self.knight.move_right(self.level_array)
            if self.check_for_attack():
                self.draw()
            if not safe_move:
                kp_y, kp_x = self.knight.return_position()
                self.reset_knight(kp_y, kp_x, "You hit a spider!")
            self.check_for_attack()

        # Move left
        if key == pygame.K_LEFT:

            safe_move = self.knight.move_left(self.level_array)
            if self.check_for_attack():
                self.draw()
            if not safe_move:
                kp_y, kp_x = self.knight.return_position()
                self.reset_knight(kp_y, kp_x, "You hit a spider!")
            self.check_for_attack()

        # Move up
        if key == pygame.K_UP:
            safe_move = self.knight.move_up(self.level_array)
            kp_y, kp_x = self.knight.return_position()
            if self.check_for_attack():
                self.reset_knight(kp_y, kp_x, "Beware the eyes...")
            if not safe_move:
                self.reset_knight(kp_y, kp_x, "You hit a spider!")

        # Move down
        if key == pygame.K_DOWN:
            safe_move = self.knight.move_down(self.level_array)
            if self.check_for_attack():
                self.reset_knight(kp_y, kp_x, "Beware the eyes...")
            if not safe_move:
                kp_y, kp_x = self.knight.return_position()
                self.reset_knight(kp_y, kp_x, "You hit a spider!")

        # Scan
        if key == pygame.K_s:
            self.scanner = Scanner(self.level_array, self.original_array, self.scanned_tiles,
                                   self.knight.return_position())
            self.is_scanned = True

        # Light
        if key == pygame.K_f:
            kp_y, kp_x = self.knight.return_position()
            self.light = Light(self.level_array, self.original_array, self.lit_tiles,
                               self.knight.return_position())
            self.knight.previous_tile = self.light.previous_tile
            print('previous tile: ', self.light.previous_tile)
            self.level_array[kp_y][kp_x] = 'kl'
            self.knight.next_tile = 'l'
            self.is_lit = True
            if self.check_for_attack():
                self.reset_knight(kp_y, kp_x, "Beware the eyes...")

        # press SPACE to interactive with torch
        if key == pygame.K_SPACE:
            kp_y, kp_x = self.knight.return_position()  # kp_y is knight's row, kp_y is knight's column
            xlocation_torch, ylocation_torch, sate_torch = BigTorch().is_torch_lit(
                self.level_array)  # check and retrun the state of troch, also retrun torch's row and column
            flag_isnearby = BigTorch().is_near_torch(xlocation_torch, ylocation_torch, kp_x,
                                                     kp_y)  # check eligibility to interact with the torch
            flag_finaltorch = BigTorch().change_torch_state(sate_torch, xlocation_torch,
                                                            ylocation_torch,
                                                            self.level_array,
                                                            flag_isnearby)  # change torch's pictures
            if (flag_finaltorch == True):  # if lit torch, play a related cutscene
                BigTorch().play_lightcutscene()
            # missing: all tiles change into visible

    def check_for_attack(self):
        for i in range(6):
            if self.level_array[1][i] == "kl":
                self.Ranged_Enemy.ranged_attack(self.level_array, self.knight)
                return True

    # Move knight back to starting square when they hit a spider
    def reset_knight(self, kp_y, kp_x, message):
        '''self.screen.fill((0,0,0))'''
        '''self.screen.blit(caption,[self.wINDOW_WIDTH/2,self.wINDOW_HEIGHT/2])'''
        self.caption_rect = pygame.Rect((kp_x + 6) * TILESIZE, kp_y * TILESIZE, TILESIZE, TILESIZE)
        self.reset = True
        self.message = message

    # Read in level is its own function so that we can call it to read in different levels.
    def read_in_level(self, level_number):
        print(self.levels)
        filepath = os.path.join("levels", self.levels[level_number])
        with open(filepath, "r") as f:
            csv_reader = csv.reader(f, delimiter=';')
            self.level_array = list(csv_reader)
            self.level_array = [x for x in self.level_array if x != []]
            self.original_array = copy.deepcopy(self.level_array)
        self.knight = Knight(9, 0)
        self.create_monster_objects()

    # Create array of monster objects
    def create_monster_objects(self):
        self.ranged_enemies.clear()
        for y in range(TILES_VERTICAL):
            for x in range(TILES_HORIZONTAL):
                if self.level_array[y][x] == "hre":
                    self.ranged_enemies.append(Ranged_Enemy(y, x))

    # Draw new assets to screen
    def draw(self, surface, time_tick):
        surface.fill(self.BG_COLOR)
        self.tiles = Tiles(surface, self.level_array)
        self.tiles.draw(surface)
        # if self.is_lit:
        #     self.light.draw(self.surface)
        if self.is_scanned:
            self.scan_label = self.scanner.draw(surface)
            self.scan_label['timestamp'] = time_tick
            print(time_tick)
        if self.scan_label and time_tick - self.scan_label['timestamp'] < 3000:
            surface.blit(self.scan_label['text'], self.scan_label['rect'])
        if self.reset:
            font = pygame.font.SysFont("arial", 16)
            caption = font.render(self.message, True, WHITE)
            surface.blit(caption, self.caption_rect)
            pygame.display.flip()
            pygame.time.wait(1000)
            self.knight.reset_knight_position(self.level_array)
            self.reset = False
        font = pygame.font.SysFont('arial', 20)
        for scanned in self.scanned_tiles:
            text = font.render(str(scanned[1]), True, (255, 255, 255))
            surface.blit(text, scanned[0])
        pygame.display.update()

    def startup(self, game_info):
        self.read_in_level(0)
        self.scanned_tiles = []

    def update(self, surface, key, time_tick):
        if not self.reset:
            self.keydown_events(key)
        self.draw(surface, time_tick)
