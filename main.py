import core.game as game
import pygame

if __name__ == '__main__':

    # On initialise Pygame
    pygame.init()

    # On instancie la classe de jeu
    game = game.Game()

    # On lance le jeu en appelant sa méthode run()
    game.run()
