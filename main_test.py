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
from circle_triangle import *

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


    CircleShape.containers = (drawable,)
    Segment.containers = (drawable,)
    Dot.containers = (drawable,)
    

    circle = CircleShape(500, 500, 50)
    #segment = Segment(400, 400, 300, 450)
   # Dx = float
    #Dy = float
    A = Dot(300,300, (255, 0,0))
    B = Dot(434, 555, (0, 255, 0))
    #pygame.math.Vector2.dot(D.position, circle.position) == 0 
    print(A.position - B.position)
    alpha = (A.position[0]-B.position[0]) / (A.position[1]-B.position[1])
    #Dx = alpha Dy
    Dy = (circle.position[0] * alpha + circle.position[1])/(1+alpha*alpha)
    Dx = alpha * Dy
    D = Dot(Dx + A.position[0], Dy+A.position[1], (0, 0, 255))
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
