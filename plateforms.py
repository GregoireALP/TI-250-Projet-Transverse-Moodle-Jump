import pygame

import constants
import platform
import random
from constants import *


def generate_platforms():
    # Initialisation des variables
    current_height = constants.PLAYER_SPWAN[1]

    platform_gap_y = 100
    platform_gap_x = 20

    positions = []

    for _ in range(constants.PLATEFORMS):
        current_height -= platform_gap_y

        # Generate random position for platforms
        position_x = random.randint(platform_gap_x, constants.SCREEN_WIDTH - platform_gap_x)

        # Check if platform is not too close from the previous one
        if len(positions) > 0:
            while abs(position_x - positions[-1][0]) < platform_gap_x:
                position_x = random.randint(0, constants.SCREEN_WIDTH - platform_gap_x)

        positions.append((position_x, current_height))

    return positions


class Platforms:

    def __init__(self):

        self.platforms = pygame.sprite.Group()
        self.init_plateforms()

        self.speed = 1

    def reset(self):

        self.platforms.empty()
        self.init_plateforms()

    def init_plateforms(self):

        # init plateform where player appears
        self.platforms.add(platform.Platform(constants.PLAYER_SPWAN[0], constants.PLAYER_SPWAN[1] + 20))

        # Generate plateforms
        for position in generate_platforms():
            self.platforms.add(platform.Platform(position[0], position[1], False, False))

    def update_plateforms(self):

        for pl in self.platforms:

            pl.rect.y += self.speed

            # Remove plateforms
            if pl.rect.y > constants.SCREEN_HEIGHT:
                self.platforms.remove(pl)

            # Regenate plateform
            if len(self.platforms) < constants.PLATEFORMS:
                for pos in generate_platforms():
                    if random.random() < 0.15:
                        self.platforms.add(platform.Platform(pos[0], pos[1] - constants.SCREEN_HEIGHT / 2, True, False))
                    elif random.random() < 0.3:
                        self.platforms.add(platform.Platform(pos[0], pos[1] - constants.SCREEN_HEIGHT / 2, False, True))
                    else:
                        self.platforms.add(platform.Platform(pos[0], pos[1] - constants.SCREEN_HEIGHT / 2, False, False))

            # Check if plateform is moving
            if pl.isMoving:
                if pl.rect.x > constants.SCREEN_WIDTH:
                    pl.velocity_x = -1
                elif pl.rect.x < 0:
                    pl.velocity_x = 1

                pl.rect.x += pl.velocity_x
