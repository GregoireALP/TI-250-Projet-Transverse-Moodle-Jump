# Import et initialise la bibliothèque pygame
import pygame
import sys
from constants import *
from platform import *
from user import *


class Game:

    def __init__(self):
        # Création de la fenêtre de jeu
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Moodle Jump")
        pygame.display.set_icon(pygame.image.load('assets/player2.png'))

        self.clock = pygame.time.Clock()

    def draw_sprite(self, sprite):
        self.screen.blit(sprite.image, sprite.rect)
        #pygame.draw.rect(self.screen, (255, 255, 255), sprite.rect, 2)

    def run(self):
        running = True

        # Attribution des sprites a une variable
        player = Player()
        platform = Platform()

        if player.rect.colliderect(platform.rect):
            player.rect.x = 10

        # Création de l'arrière-plan
        background = pygame.image.load('assets/dark_background.png')
        background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Boucle de jeu permettant à l'utilisateur de fermer la fenêtre
        while running:
            self.clock.tick(FPS)
            key = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
                    running = False

            player.handle_movement(key, platform)

            collide = player.rect.y >= (platform.rect.y - platform.rect.height)

            if collide:
                if player.rect.colliderect(platform.rect):
                    player.rect.bottom = platform.rect.top
                    player.jumping = False
                    player.velocity_y = 0
                else:
                    player.on_platform = False
            else:
                player.on_platform = False

            self.screen.blit(background, (0, 0))
            self.draw_sprite(player)
            self.draw_sprite(platform)

            pygame.display.flip()

        pygame.quit()
        sys.exit()
