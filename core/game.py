import pygame

import config.windowUtils as wUtils
import core.player as p


class Game:

    def __init__(self):

        # On définie une fenetre
        self.screen = pygame.display.set_mode((wUtils.WIDTH, wUtils.HEIGHT))

        # On met le fond d'écran
        self.backgroundPicture = pygame.image.load("./assets/background.png")
        self.backgroundPicture = pygame.transform.scale(self.backgroundPicture, (wUtils.WIDTH, wUtils.HEIGHT))

        pygame.display.set_caption("Moodle Jump")  # TITLE

        self.clock = pygame.time.Clock()

    def draw_sprite(self, sprite):
        self.screen.blit(sprite.image, sprite.rect)
        pygame.display.update()

    def run(self):

        isRunning = True
        player = p.Player()

        # Boucle de jeu permettant à l'utilisateur de fermer la fenêtre
        while isRunning:

            self.clock.tick(60)

            # On récupere la touche pressée
            key = pygame.key.get_pressed()

            # On parcours tous les events déclenchées
            for event in pygame.event.get():

                # Si le joueur ferme le jeu
                if event.type == pygame.QUIT or key[pygame.K_ESCAPE]:
                    isRunning = False

            if key[pygame.K_RIGHT] or key[pygame.K_d]:
                player.move_right()
            if key[pygame.K_LEFT] or key[pygame.K_q]:
                player.move_left()

            player.jump()

            # On dessine le joueur
            self.draw_sprite(player)

            # On dessine le fond d'écran
            # self.screen.blit(self.backgroundPicture, (0, 0))

            # On actualise la fenetre
            pygame.display.update()

        pygame.quit()
