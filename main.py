import pygame
import sys
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Initializes Pygame
    pygame.init()

    # Creates groups for the player's gameplay loop
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Create a player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Creates an asteroid field object
    asteroidfield = AsteroidField()

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

        # Updates the player
        # player.update(dt)
        updatable.update(dt)

        # Updates the asteroids
        asteroids.update(dt)

        # Checks to see if the player collides with an asteroid
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # Checks to see if a player bullet collides with an asteroid
        for shot in shots:
            for asteroid in asteroids:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        # Re-renders the player
        for item in drawable:
            item.draw(screen)
        # player.draw(screen)

        # Refreshes the display
        pygame.display.flip()

        # Pauses the game for 1/60th of a second
        clock.tick(60)
        # Updates the dt variable in terms of seconds
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
