import pygame

import constants


class Chronometre:

    def __init__(self):
        self.time = 0
        self.run = True
        self.clock = pygame.time.Clock()

    def running(self):
            self.time += self.clock.tick(constants.FPS)

    def stop(self):
        self.run = False

    def get_time(self):
        return self.time
