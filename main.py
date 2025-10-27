import pygame

from constants import(SCREEN_WIDTH, SCREEN_HEIGHT)

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:                                 # sets infinite loop which keeps game opened
        for event in pygame.event.get():        # makes window close button work
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (34,34,34))
        pygame.display.flip()                    # updates screen

if __name__ == "__main__":
    main()