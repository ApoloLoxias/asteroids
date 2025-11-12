# Importing libraries
import pygame
# Importing project modules
from constants import (
      SCREEN_HEIGHT, SCREEN_WIDTH,
      BACKGROUND_COLOUR,
      )
from logger import log_state

def main():
    # Initial terminal message
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    # Preliminary initializations
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Sets main gameloop
    while True:
        log_state() # for boot.dev tests

        screen.fill(BACKGROUND_COLOUR) # sets black (lightly gray) display surface

        pygame.display.flip() # updates screen at the end of gameloop

if __name__ == "__main__":
    main()
