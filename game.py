# Import et initialise la bibliothèque pygame
import pygame
import sys
import constants
import bullet
import drawers
from constants import *
from plateforms import Platforms
from platform import *
from user import *


class Game:

    def __init__(self):
        # Création de la fenêtre de jeu
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Moodle Jump")
        pygame.display.set_icon(pygame.image.load('assets/player.png'))

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("timenewroman", 48)

        self.state = "menu"

        self.quit_rect = None
        self.rules_rect = None
        self.play_rect = None
        self.title_rect = None
        self.credit_rect = None

        self.score_rect = None
        self.replat_rect = None

    def run(self):
        running = True

        drawers.draw_menu(self)

        # Attribution des sprites a une variable
        player = Player()
        platforms = Platforms()
        bullets = pygame.sprite.Group()
        bullet_timer = pygame.time.get_ticks()
        Timer = pygame.time.Clock()

        # Création de l'arrière-plan
        background = pygame.image.load('assets/dark_background.png')
        background = pygame.transform.scale(
            background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Boucle de jeu permettant à l'utilisateur de fermer la fenêtre
        while running:

            self.clock.tick(FPS)
            current_time = pygame.time.get_ticks()

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
                    if self.rules_rect.collidepoint(mouse_pos):
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            self.state = "rules"
                    if self.credit_rect.collidepoint(mouse_pos):
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            self.state = "credit"

                if self.state == "rules":
                    if key[pygame.K_ESCAPE]:
                        self.state = "menu"

                if self.state == "credit":
                    if key[pygame.K_ESCAPE]:
                        self.state = "menu"

                if self.state == "end":
                    if self.replat_rect.collidepoint(mouse_pos):
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            self.state = "playing"
                            platforms.reset()
                            player.reset()
                            player.score = 0

                    if self.quit_rect.collidepoint(mouse_pos):
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            running = False

            if self.state == "menu":
                drawers.draw_menu(self)

            if self.state == "rules":
                drawers.draw_rules(self)

            if self.state == "credit":
                drawers.draw_credit(self)

            if self.state == "end":
                drawers.draw_score(self, player.score)
                bullets.empty()

            elif self.state == "playing":
                drawers.score_in_game(self, player.score)

                # Apparition des bullet
                if current_time - bullet_timer > 6000:
                    nb = bullet.Bullet()
                    bullets.add(nb)
                    bullet_timer = current_time

                timeForScore = current_time / 1000
                if(60 - timeForScore) <= 0:
                    self.state = "end"

                # Appelle la fonction permettant de controller le joueur.
                player.handle_movement(key)

                self.screen.blit(background, (0, 0))
                drawers.draw_sprite(self, player)

                for platform in platforms.platforms:

                    # Gérer la collision entre le jouer et les plateformes
                    if player.rect.colliderect(platform.rect):
                        if player.velocity_y <= 0:  # Vérifie si le joueur tombe
                            player.rect.bottom = platform.rect.top
                            player.jumping = False
                            player.velocity_y = 0

                            if platform.isDisappear:
                                platforms.platforms.remove(platform)

                            player.jump()
                    
                    drawers.draw_sprite(self, platform)

                # Gérer la collision entre le joueur et les bullets et le jeu s'arrête
                for b in bullets:
                    if player.rect.colliderect(b.rect):
                        self.state = "end"

                platforms.update_plateforms()
                bullets.update()
                bullets.draw(self.screen)

                # Si le joueur est dans le 1/3 de l'écran, on fait descendre les plateformes plus vite
                if player.rect.y < (constants.SCREEN_HEIGHT * 0.2):
                    platforms.speed = 10
                elif player.rect.y < (constants.SCREEN_HEIGHT * 0.6):
                    platforms.speed = 4
                else:
                    platforms.speed = 0

                # Regarde si le joueur est toujours sur l'écran
                if player.rect.y > constants.SCREEN_HEIGHT:
                    self.state = "end"

                pygame.display.flip()

        pygame.quit()
        sys.exit()
