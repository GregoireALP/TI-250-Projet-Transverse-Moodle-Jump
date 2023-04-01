import pygame

import constants
import platform
import random
from constants import *


def generate_platforms():
    # Initialisation des variables
    current_height = 0
    platform_gap = 20

    min_gap = 100
    max_gap = 400
    platform_positions = []

    # Génération des plateformes
    for i in range(25):
        # Calcul de la position de la nouvelle plateforme
        new_platform_pos = (random.randint(0, constants.SCREEN_WIDTH), current_height + platform_gap)

        # Vérification si la nouvelle plateforme ne dépasse pas la hauteur maximale
        if new_platform_pos[1] >= constants.SCREEN_HEIGHT * 10:
            break

        # Vérification si l'écart entre les plateformes est équilibré
        if platform_gap > max_gap:
            platform_gap = max_gap
        elif platform_gap < min_gap:
            platform_gap = min_gap

        # Ajout de la nouvelle plateforme à la liste
        platform_positions.append(new_platform_pos)

        # Mise à jour de la hauteur actuelle
        current_height = new_platform_pos[1]

        # Calcul de l'écart entre les plateformes pour la prochaine itération
        platform_gap += random.uniform(-0.5, 0.5)

    return platform_positions


class Platforms:

    def __init__(self):

        self.platforms = pygame.sprite.Group()
        self.init_plateforms()

    def init_plateforms(self):

        # init plateform where player appears
        self.platforms.add(platform.Platform(constants.PLAYER_SPWAN[0], constants.PLAYER_SPWAN[1]))

        # Generate plateforms
        for position in generate_platforms():

            self.platforms.add(platform.Platform(position[0], position[1], False, False))

    def update_plateforms(self):
        
        for pl in self.platforms:

            pl.rect.y += 0

            # Check if plateform is moving
            if pl.isMoving:
                if pl.rect.x > constants.SCREEN_WIDTH:
                    pl.velocity_x = -1
                elif pl.rect.x < 0:
                    pl.velocity_x = 1

                pl.rect.x += pl.velocity_x

