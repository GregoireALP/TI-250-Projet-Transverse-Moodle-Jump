import pygame

import constants
from constants import *

def draw_menu(self):

    # Création de la fenêtre de jeu
    pygame.display.set_caption("Menu Moodle Jump")
    background = pygame.image.load('assets/cloud_background.jpg')
    background = pygame.transform.scale(background, (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    # Affichage de l'arrière-plan
    self.screen.blit(background, (0, 0))

    # Création du texte du menu
    title = self.font.render("Moodle Jump", True, (255, 255, 255))
    play = self.font.render("Jouer", True, (255, 255, 255))
    map = self.font.render("Map", True, (255, 255, 255))
    quit = self.font.render("Quitter", True, (255, 255, 255))

    # Positionner les textes sur l'écran
    self.title_rect = title.get_rect(
        center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
    self.play_rect = play.get_rect(
        center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    self.map_rect = map.get_rect(
        center=(SCREEN_WIDTH / 2, 4 * SCREEN_HEIGHT / 6))
    self.quit_rect = quit.get_rect(
        center=(SCREEN_WIDTH / 2, 5 * SCREEN_HEIGHT / 6))

    # Dessiner les textes sur l'écran
    self.screen.blit(title, self.title_rect)
    self.screen.blit(play, self.play_rect)
    self.screen.blit(map, self.map_rect)
    self.screen.blit(quit, self.quit_rect)

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
