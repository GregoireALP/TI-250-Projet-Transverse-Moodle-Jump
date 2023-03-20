import config.windowUtils as wUtils
import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # On définit l'apparance du joueur
        self.image = pygame.image.load('./assets/player.png').convert()
        self.image = pygame.transform.scale(self.image, (70, 70))

        self.rect = self.image.get_rect()

        # On définit sa position
        self.rect.x = wUtils.WIDTH / 2 - self.rect.width / 2
        self.rect.y = wUtils.HEIGHT - (wUtils.HEIGHT / 4)

        # On définit sa vitesse de déplacement, de saut, la
        self.speed = 1
        self.jump_speed = -10

        self.v0 = 100  # vitesse initiale en pixels/seconde
        self.a = -9.8  # accélération en pixels/seconde^2
        self.t = 0  # temps en secondes
        self.dt = 0.01

    def move_right(self):
        self.rect.x += self.speed
        if self.rect.x > wUtils.WIDTH:
            self.rect.x = 0

    def move_left(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = wUtils.WIDTH

    def jump(self):
        pass
