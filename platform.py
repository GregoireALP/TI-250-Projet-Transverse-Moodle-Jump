import pygame
from constants import *


class Platform(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/platform.png')
        self.image = pygame.transform.scale(self.image, (80, 20))
        self.rect = pygame.Rect(SCREEN_WIDTH / 2 - self.image.get_width()/2,
                                SCREEN_HEIGHT - 150,
                                self.image.get_width(),
                                self.image.get_height())

