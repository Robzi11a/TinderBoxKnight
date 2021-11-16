import sys
import pygame
from settings import Settings

class TinderBoxKnight:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Tinder Box Knight")


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)    

    def _check_keydown_events(self, event):
        """Respond to keypresses."""  
        if event.key == pygame.K_q:
            sys.exit() 

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_colour)
             # Make the most recently drawn screen visible.

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    tbk = TinderBoxKnight()
    tbk.run_game()