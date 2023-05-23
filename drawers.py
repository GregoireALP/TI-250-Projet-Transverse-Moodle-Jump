import pygame

import constants
from constants import *


def draw_menu(self):

    # Création de la fenêtre de jeu
    pygame.display.set_caption("Menu Moodle Jump")
    background = pygame.image.load('assets/menu.png')
    background = pygame.transform.scale(background, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))


    # Affichage de l'arrière-plan
    self.screen.blit(background, (0, 0))

    # Création du texte du menu
    title = self.font.render("Moodle Jump", True, (0, 0, 0))
    play = self.font.render("Jouer", True, (255, 255, 255))
    rules = self.font.render("Règle", True, (255, 255, 255))
    quit = self.font.render("Quitter", True, (255, 255, 255))
    credit = self.font.render("C", True, (255, 255, 255))

    # Positionner les textes sur l'écran
    self.title_rect = title.get_rect(
        center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
    self.play_rect = play.get_rect(
        center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    self.rules_rect = rules.get_rect(
        center=(SCREEN_WIDTH / 2, 4 * SCREEN_HEIGHT / 6))
    self.quit_rect = quit.get_rect(
        center=(SCREEN_WIDTH / 2, 5 * SCREEN_HEIGHT / 6))
    # Créer un rectangle pour cliquer sur le crédit
    self.credit_rect = credit.get_rect(
        center=(SCREEN_WIDTH - 33, SCREEN_HEIGHT - 20)
    )

    pygame.display.flip()


def draw_score(self, score):

    score = self.font.render("Score: " + str(score), True, (255, 255, 255))
    replay = self.font.render("Rejouer", True, (255, 255, 255))

    self.score_rect = score.get_rect(
        center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
    self.replat_rect = replay.get_rect(
        center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    self.screen.blit(score, self.score_rect)
    self.screen.blit(replay, self.replat_rect)

    pygame.display.flip()


def draw_sprite(self, sprite):

    # Dessiner le sprite sur l'écran
    self.screen.blit(sprite.image, sprite.rect)
    # pygame.draw.rect(self.screen, (255, 255, 255), sprite.rect, 2)


def draw_rules(self):

    # Création de la fenêtre de jeu
    pygame.display.set_caption("Règles Moodle Jump")
    background = pygame.image.load('assets/regles.png')

    # Affichage de l'arrière-plan
    self.screen.blit(background, (0, 0))

    # Update de la page
    pygame.display.flip()


def draw_credit(self):

    # Création de la fenêtre de jeu
    pygame.display.set_caption("Credit Moodle Jump")
    background = pygame.image.load('assets/credit.png')

    # Affichage de l'arrière-plan
    self.screen.blit(background, (0, 0))

    # Update de la page
    pygame.display.flip()
