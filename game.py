# Import et initialise la bibliothèque pygame
import pygame
import sys

import chronometre
from constants import *
from plateforms import Platforms
from platform import *
from user import *


class Game:

    def __init__(self):
        # Création de la fenêtre de jeu
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Moodle Jump")
        pygame.display.set_icon(pygame.image.load('assets/player2.png'))

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("comicsansms", 48)

        self.state = "menu"

        self.quit_rect = None
        self.map_rect = None
        self.play_rect = None
        self.title_rect = None

        self.score_rect = None
        self.replat_rect = None

    def draw_menu(self):
        # Design
        pygame.display.set_caption("Menu Moodle Jump")
        background = pygame.image.load('assets/cloud_background.jpg')
        background = pygame.transform.scale(background, (400, 600))

        self.screen.blit(background, (0, 0))

        # Création du texte du menu
        title = self.font.render("Moodle Jump", True, (255, 255, 255))
        play = self.font.render("Jouer", True, (255, 255, 255))
        map = self.font.render("Map", True, (255, 255, 255))
        quit = self.font.render("Quitter", True, (255, 255, 255))

        # Positionner les textes sur l'écran
        self.title_rect = title.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
        self.play_rect = play.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.map_rect = map.get_rect(center=(SCREEN_WIDTH / 2, 4 * SCREEN_HEIGHT / 6))
        self.quit_rect = quit.get_rect(center=(SCREEN_WIDTH / 2, 5 * SCREEN_HEIGHT / 6))

        # Dessiner les textes sur l'écran
        self.screen.blit(title, self.title_rect)
        self.screen.blit(play, self.play_rect)
        self.screen.blit(map, self.map_rect)
        self.screen.blit(quit, self.quit_rect)

        pygame.display.flip()

    def draw_score(self, score):
        score = self.font.render(f"Score: {score}", True, (255, 255, 255))
        replay = self.font.render("Rejouer", True, (255, 255, 255))

        self.score_rect = score.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
        self.replat_rect = replay.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

        self.screen.blit(score, self.score_rect)
        self.screen.blit(replay, self.replat_rect)

        pygame.display.flip()

    def draw_sprite(self, sprite):
        self.screen.blit(sprite.image, sprite.rect)
        # pygame.draw.rect(self.screen, (255, 255, 255), sprite.rect, 2)

    def run(self):
        running = True

        self.draw_menu()

        # Attribution des sprites a une variable
        player = Player()
        platforms = Platforms()
        chrono = chronometre.Chronometre()

        # Création de l'arrière-plan
        background = pygame.image.load('assets/dark_background.png')
        background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Boucle de jeu permettant à l'utilisateur de fermer la fenêtre
        while running:
            self.clock.tick(FPS)
            key = pygame.key.get_pressed()
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or key[pygame.K_BACKSPACE]:
                    running = False

                if self.state == "playing":
                    if key[pygame.K_ESCAPE]:
                        self.state = "menu"

                if self.state == "menu":
                    if self.play_rect.collidepoint(mouse_pos):
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            self.state = "playing"
                    if self.quit_rect.collidepoint(mouse_pos):
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            running = False

            if self.state == "menu":
                self.draw_menu()

            if self.state == "end":
                self.draw_score(chrono.get_time() / 1000)

            elif self.state == "playing":
                # Appelle la fonction permettant de controller le joueur.
                player.handle_movement(key)

                self.screen.blit(background, (0, 0))
                self.draw_sprite(player)

                chrono.running()

                for platform in platforms.platforms:

                    # Gérer la collision entre le jouer et les plateformes
                    if player.rect.colliderect(platform.rect):
                        if player.velocity_y <= 0:  # Vérifie si le joueur tombe
                            player.rect.bottom = platform.rect.top
                            player.jumping = False
                            player.velocity_y = 0

                            # Errase plateform if isDisapear is True
                            if platform.isDisappear:
                                platforms.platforms.remove(platform)

                        # Saut automatique TODO enlever le # pour activer
                        player.jump()

                    self.draw_sprite(platform)
                    platforms.update_plateforms()

                # Regarde si le joueur est toujours sur l'ecram
                if player.rect.y > constants.SCREEN_HEIGHT:
                    self.state = "end"
                    chrono.stop()

                pygame.display.flip()

        pygame.quit()
        sys.exit()
