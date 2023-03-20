import pygame
from constants import *


class Platform(pygame.sprite.Sprite):

    def __init__(self, x ,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/platform.png')
        self.image = pygame.transform.scale(self.image, (100, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
