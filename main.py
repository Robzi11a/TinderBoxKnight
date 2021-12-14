import pygame
import ground as floor
from game import Game
from mainmenu import Menu
from level import Level
from randomdifficulty import RandomDifficulty


def main():
    pygame.init()
    pygame.display.set_caption("Tinder Box Knight")
    game = Game()

    state_dict = {floor.MAIN_MENU: Menu(),
                  floor.LEVEL: Level(),
                  floor.RANDOM_LEVEL: RandomDifficulty(),
                  floor.EASY_LEVEL: Level(-1),
                  floor.MEDIUM_LEVEL: Level(-2),
                  floor.HARD_LEVEL: Level(-3)
                  }

    game.setup_states(state_dict, floor.MAIN_MENU)

    game.run()


if __name__ == '__main__':
    main()
