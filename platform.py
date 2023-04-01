import pygame
from constants import *


class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, isDisappear=False):
        pygame.sprite.Sprite.__init__(self)
        self.isDisappear = isDisappear


        # Skins the plateform
        if(not self.isDisappear):
            self.image = pygame.image.load('assets/platform.png')
            self.image = pygame.transform.scale(self.image, (80, 20))
        else:
            self.image = pygame.image.load('assets/platformDisappear.png')
            self.image = pygame.transform.scale(self.image, (80, 20))

        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

