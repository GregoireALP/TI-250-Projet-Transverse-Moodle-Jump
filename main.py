import pygame
import utils.window as w
import utils.constants as c

if __name__ == "__main__":
    pygame.init()

    # Import background image
    backgroundPicture = pygame.image.load("assets/background.png")
    backgroundPicture = pygame.transform.scale(backgroundPicture, (w.wUtils.window_params["width"], w.wUtils.window_params["height"]))

    """
    MAIN GAME LOOP
    """
    isRunning = True
    while isRunning:

        # Setting background image
        w.WINDOW.blit(backgroundPicture, (0, 0))

        # Check for all current events
        for e in pygame.event.get():

            # If QUIT event
            if e.type == pygame.QUIT:
                isRunning = False

        # Update console at the end of the loop
        pygame.display.update()

    pygame.quit()
