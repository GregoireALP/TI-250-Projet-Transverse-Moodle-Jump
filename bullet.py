import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/bullet.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image = pygame.transform.rotate(self.image, 90)
        self.rect = self.image.get_rect()

        self.player = player
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y - 30

        self.velocity = 5

    def remove(self):
        self.player.bullets.remove(self)

    def move(self):
        self.rect.y -= self.velocity

        if self.rect.y < 0:
            self.remove()