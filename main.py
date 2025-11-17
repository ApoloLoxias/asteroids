# Importing libraries
import pygame
import sys
# Importing project modules
from constants import (
      SCREEN_HEIGHT, SCREEN_WIDTH,
      BACKGROUND_COLOUR,
      TICK_RATE,
      PLAYER_SPAWN_X, PLAYER_SPAWN_Y,
      )
from logger import (log_state,
                    log_event,
)
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

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
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(PLAYER_SPAWN_X, PLAYER_SPAWN_Y)
    asteroidfield = AsteroidField()
    Shot.containers = (shots, updatable, drawable)
    
    # Sets main gameloop
    while True:
        # Initial checks
        log_state() # for boot.dev tests
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Gamestate update and input processing
        updatable.update(dt)
        # Checks for colisions
        for asteroid in asteroids:
            for asteroid2 in asteroids:
                if asteroid is asteroid2:
                    continue
                if asteroid.position.distance_to(asteroid2.position) !=0 and asteroid.collides_with(asteroid2):
                    print("Asteroid collision")
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
        # Screen/display updating
        screen.fill(BACKGROUND_COLOUR) # sets black (lightly gray) display surface
        for drawable_element in drawable:
            drawable_element.draw(screen)
        pygame.display.flip() # updates screen at the end of gameloop
        #Timekeeping and FPS limiting
        dt = 1/1000 * clock.tick(TICK_RATE)

if __name__ == "__main__":
    main()
