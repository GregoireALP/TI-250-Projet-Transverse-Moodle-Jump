import pygame
import utils.window as w
import utils.constants as c

if __name__ == "__main__":
    pygame.init()

    """
    GAME LOOP
    """
    isRunning = True
    while isRunning:

        # Setting background image
        w.WINDOW.blit(w.backgroundPicture, (0, 0))

        # Check for all current events
        for e in pygame.event.get():

            # If QUIT event
            if e.type == pygame.QUIT:
                isRunning = False

        # Update console at the end of the loop
        pygame.display.update()

    pygame.quit()
