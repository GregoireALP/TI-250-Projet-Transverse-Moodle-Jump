from game import *
import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/player2.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH / 2 - self.rect.width / 2
        self.rect.y = SCREEN_HEIGHT - self.rect.height

        self.velocity_y = 0
        self.speed = 4
        self.jumpForce = 18
        self.jumping = False

        self.on_platform = False

    def handle_movement(self, key, platform):
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            self.move_right()
        if key[pygame.K_LEFT] or key[pygame.K_q]:
            self.move_left()
        if key[pygame.K_UP] or key[pygame.K_SPACE]:
            self.jump()

        self.update(platform)

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

    def update(self, platform):
        if self.jumping:
            self.rect.y -= self.velocity_y
            self.velocity_y -= GRAVITY
            if self.rect.y >= SCREEN_HEIGHT - self.rect.height:
                self.rect.y = SCREEN_HEIGHT - self.rect.height
                self.jumping = False
        else:
            if self.rect.colliderect(platform.rect):
                self.rect.bottom = platform.rect.top
                self.jumping = False
                self.velocity_y = 0
                self.on_platform = True
            else:
                self.on_platform = False

            self.rect.x %= SCREEN_WIDTH
