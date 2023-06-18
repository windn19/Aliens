import sys

import pygame

from settings import Settings
from frog import Frog


class Aliens:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
        pygame.display.set_caption('Aliens')
        self.frog = Frog(self)

    def run_game(self):
        while True:
            self._check_event()
            self._update_screen()

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.frog.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ai = Aliens()
    ai.run_game()