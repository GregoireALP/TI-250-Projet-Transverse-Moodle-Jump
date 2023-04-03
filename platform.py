import pygame
from constants import *


class Platform(pygame.sprite.Sprite):

    def __init__(self, x, y, isDisappear=False, isMoving=False):

        pygame.sprite.Sprite.__init__(self)

        self.isDisappear = isDisappear
        self.isMoving = isMoving
        self.velocity_x = 1

        # Skins the plateform
        if(self.isDisappear):
            self.image = pygame.image.load('assets/platformDisappear.png')
            self.image = pygame.transform.scale(self.image, (80, 20))

        elif self.isMoving:
            self.image = pygame.image.load('assets/platformMoving.png')
            self.image = pygame.transform.scale(self.image, (80, 20))
            
        else:
            self.image = pygame.image.load('assets/platform.png')
            self.image = pygame.transform.scale(self.image, (80, 20))

        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

