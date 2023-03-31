import pygame
from constants import *


class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/platform.png')
        self.image = pygame.transform.scale(self.image, (80, 20))
        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

