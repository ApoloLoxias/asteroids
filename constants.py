import pygame

# Screen configuration
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BACKGROUND_COLOUR = (34, 34, 34) #Black (slightly gray)

# Clock settings
TICK_RATE = 60 # In Hz

#Player configuration
PLAYER_RADIUS = 20 # Of the circular hitbox
LINE_WIDTH = 2 # For the contouring; if ==0: fills up the triangular sprite
PLAYER_SPAWN_X = SCREEN_WIDTH / 2
PLAYER_SPAWN_Y = SCREEN_HEIGHT / 2
PLAYER_COLOUR = (240, 240, 240) # White (light gray)
PLAYER_TURN_SPEED = 300

# Keybinds and controls
KEYBIND_ROTATE_LEFT = pygame.K_a
KEYBIND_ROTATE_RIGHT = pygame.K_d