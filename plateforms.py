import pygame

import constants
import platform
from constants import *


class Platforms:

    def __init__(self):
        self.platforms = pygame.sprite.Group()
        self.init_plateforms()

    def init_plateforms(self):
        # init plateform where player appears
        self.platforms.add(platform.Platform(constants.PLAYER_SPWAN[0], constants.PLAYER_SPWAN[1]))

        self.platforms.add(platform.Platform(100, 100))

    def update_plateforms(self):
        print("Nombre de plateformes: ", len(self.platforms))
        for pl in self.platforms:
            pl.rect.y += 1

            # Supprime les palateformes qui sont hors de l'ecran
            if pl.rect.y > constants.SCREEN_WIDTH:
                self.platforms.remove(pl)
