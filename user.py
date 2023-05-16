import constants
import bullet
from game import *
import pygame


# Création de la classe Player
class Player(pygame.sprite.Sprite):

    # Initialisation de la classe
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('assets/player.png')
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = constants.PLAYER_SPWAN[0]
        self.rect.y = constants.PLAYER_SPWAN[1]

        self.velocity_y = 0
        self.speed = 3
        self.jumpForce = 13
        self.jumping = False

        self.score = 0

        self.on_platform = False

    def handle_movement(self, key):

        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.move_right()
        if key[pygame.K_LEFT] or key[pygame.K_q]:
            self.move_left()
        if key[pygame.K_SPACE]:
            self.shoot()

        self.update()

    def move_right(self):

        self.rect.x += self.speed

        if self.rect.x > SCREEN_WIDTH - (self.rect.width/2):
            self.rect.x = 0 - (self.rect.width/2)

    def move_left(self):

        self.rect.x -= self.speed

        if self.rect.x < 0 - (self.rect.width/2):
            self.rect.x = SCREEN_WIDTH - self.rect.width / 2

    def jump(self):

        if self.jumping:
            return

        self.jumping = True
        self.velocity_y = self.jumpForce

    def reset(self):
        self.rect.x = constants.PLAYER_SPWAN[0]
        self.rect.y = constants.PLAYER_SPWAN[1]

    def shoot(self):
        b = bullet.Bullet(self.rect.x, self.rect.y)

    def update(self):

        if self.velocity_y > 0:
            self.score += 1

        if self.jumping:
            self.rect.y -= self.velocity_y
            self.velocity_y -= GRAVITY
