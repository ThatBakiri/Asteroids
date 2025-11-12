import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    running = True

    while running:
        # Allows the player to quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Updates the game state
        log_state()

        # Makes the background of the game black
        screen.fill("black")

        # Refreshes the display
        pygame.display.flip()

    pygame.quit()
if __name__ == "__main__":
    main()
