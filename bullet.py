import pygame
from constants import *


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y):

        pygame.sprite.Sprite.__init__(self)

        self.masse = 1

        self.image = pygame.image.load('assets/bullet.png')
        self.image = pygame.transform.scale(self.image, (20, 20))

        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

