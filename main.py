from game import *
import pygame

if __name__ == '__main__':

    # Initialise pygame
    pygame.init()

    # Création de la fenêtre de jeu
    game = Game()

    # Boucle de jeu permettant à l'utilisateur de fermer la fenêtre
    game.run()
