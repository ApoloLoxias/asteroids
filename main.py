# Importing libraries
import pygame
# Importing project modules
from constants import (
      SCREEN_HEIGHT, SCREEN_WIDTH,
      BACKGROUND_COLOUR,
      TICK_RATE,
      PLAYER_SPAWN_X, PLAYER_SPAWN_Y,
      )
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    # Initial terminal message
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Preliminary initializations
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 # Stores time between current and previous frames
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(PLAYER_SPAWN_X, PLAYER_SPAWN_Y)
    asteroidfield = AsteroidField()
    
    # Sets main gameloop
    while True:
        # Initial checks
        log_state() # for boot.dev tests
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Gamestate update and input processing
        updatable.update(dt)
        # Screen/display updating
        screen.fill(BACKGROUND_COLOUR) # sets black (lightly gray) display surface
        for drawable_element in drawable:
            drawable_element.draw(screen)
        pygame.display.flip() # updates screen at the end of gameloop
        #Timekeeping and FPS limiting
        dt = 1/1000 * clock.tick(TICK_RATE)

if __name__ == "__main__":
    main()
