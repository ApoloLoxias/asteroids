import pygame

from constants import(SCREEN_WIDTH, SCREEN_HEIGHT)

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()   #creates a clock objetc
    dt = 0                                      # will hold time since last tick in miliseconds

    while True:                                 # sets infinite loop which keeps game opened
        for event in pygame.event.get():        # makes window close button work
            if event.type == pygame.QUIT:
                return
        screen.fill((34,34,34))
        pygame.display.flip()                   # updates screen
        dt = clock.tick(60)/1000    #caps framerate at 60 fps and returns time since last tick in milisecodns, then converts it to seconds and stores it in dt variable

if __name__ == "__main__":
    main()