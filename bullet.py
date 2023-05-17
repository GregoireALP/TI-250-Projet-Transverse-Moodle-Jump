import pygame
import constants
import random


class Bullet(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('assets/bullet.png')
        self.image = pygame.transform.scale(self.image, (50, 50))

        # positionnement aléatoire de la balle
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = random.randint(0, constants.SCREEN_HEIGHT - self.rect.height)

        # vélocité et gravité
        # vitesse initiale aléatoire et temps de départ
        self.v0 = [random.uniform(5, 10), random.uniform(-5, 5)]
        self.t0 = pygame.time.get_ticks() / 1000 # en secondes

        # accélération gravitationnelle
        self.g = 9.81 # m/s^2

    def update(self):
        # temps écoulé depuis le départ de la balle
        t = pygame.time.get_ticks() / 1000 - self.t0

        # mise à jour de la position verticale de la balle en fonction du temps
        y = self.rect.y + self.v0[1]*t + 1/2*self.g*t**2
        self.rect.y = round(y)

        # mise à jour de la position horizontale de la balle en fonction du temps
        x = self.rect.x + self.v0[0]*t
        self.rect.x = round(x)

        # si la balle sort de l'écran, on la supprime
        if self.rect.x < -self.rect.width:
            self.kill()