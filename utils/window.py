import pygame
import config.windowUtils as wUtils

WINDOW = pygame.display.set_mode((wUtils.window_params["width"], wUtils.window_params["height"]))

# Title at the top of the screen
pygame.display.set_caption("Moodle Jump")