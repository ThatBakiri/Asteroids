import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initializes Pygame
    pygame.init()
    
    # Creates a clock and initializes delta time variable
    clock = pygame.time.Clock()
    dt = 0

    # Sets the screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        # Updates the game state
        log_state()
        
        # Allows the player to quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Makes the background of the game black
        screen.fill("black")

        # Refreshes the display
        pygame.display.flip()

        # Pauses the game for 1/60th of a second
        clock.tick(60)
        # Updates the dt variable in terms of seconds
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
