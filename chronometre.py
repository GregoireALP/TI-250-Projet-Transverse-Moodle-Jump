import pygame

import constants

# Création de la classe Chronometre
class Chronometre:

    # Initialisation de la classe
    def __init__(self):
        self.time = 0
        self.run = True

        # Création du chronomètre
        self.clock = pygame.time.Clock()

    # Fonction permettant de lancer le chronomètre
    def running(self):
            self.time += self.clock.tick(constants.FPS)

    # Fonction permettant d'arrêter le chronomètre
    def stop(self):
        self.run = False

    # Fonction permettant de remettre le chronomètre à 0
    def reset(self):
        self.time = 0
        self.run = True

    # Fonction permettant de récupérer le temps
    def get_time(self):
        return self.time
