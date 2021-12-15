import pygame
import os
import ground as c
from abc import abstractmethod


class State:
    def __init__(self):
        self.keep_looping = True
        self.next = None
        self.knight_info = {}

    @abstractmethod
    def startup(self, game_info):
        pass

    def cleanup(self):
        self.keep_looping = True
        return self.knight_info

    @abstractmethod
    def update(self, surface, keys, time_tick):
        pass


class Game:
    def __init__(self):
        self.surface = pygame.display.set_mode((c.WINDOW_WIDTH, c.WINDOW_HEIGHT))
        print("current windows size: ", c.WINDOW_WIDTH, "*", c.WINDOW_HEIGHT)
        self.keep_looping = True
        self.clock = pygame.time.Clock()
        self.key = pygame.key.get_pressed()
        self.state_dict = {}
        self.state_name = None
        self.state = None
        self.time_tick = 0.0

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]
        game_info = self.state.cleanup()
        self.state.startup(game_info)

    def update(self):
        if not self.state.keep_looping:
            self.next_state()
        self.state.update(self.surface, self.key, self.time_tick)
        self.key = ''

    def next_state(self):
        if self.state.next == c.QUIT:
            print('quit game')
            self.keep_looping = False
        else:
            self.state_name = self.state.next
            game_info = self.state.cleanup()
            self.state = self.state_dict[self.state_name]
            self.state.startup(game_info)

    def run(self):
        while self.keep_looping:
            self.clock.tick(30)
            self.time_tick = pygame.time.get_ticks()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.keep_looping = False
                    pygame.display.quit()
                    quit()
                elif event.type == pygame.KEYDOWN:
                    self.key = event.key
            self.update()
            pygame.display.update()

