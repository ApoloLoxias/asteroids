import pygame

# Screen configuration
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BACKGROUND_COLOUR = (34, 34, 34) #Black (slightly gray)

# Clock settings
TICK_RATE = 60 # In Hz

# Global sprite configuration
LINE_WIDTH = 2 # For the contouring; if ==0: fills up the sprites

# Player configuration
PLAYER_RADIUS = 20 # Radius of a cirlce used to generate the triangular shape
PLAYER_SPAWN_X = SCREEN_WIDTH / 2
PLAYER_SPAWN_Y = SCREEN_HEIGHT / 2
PLAYER_COLOUR = (240, 240, 240) # White (light gray)
PLAYER_TURN_SPEED = 300 # Rotational acceleration
PLAYER_SPEED = 200 # Translation acceleration
SHOT_RADIUS = 5
SHOT_COLOUR = (240, 40, 40) # Red
PLAYER_SHOT_SPEED = 500
PLAYER_SHOT_COOLDOWN = 0.3 # In seconds

# Asteroids configuration
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE_SECONDS = 0.8
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
ASTEROID_COLOUR = (240,240, 240) # White (light gray)

# Keybinds and controls
KEYBIND_ROTATE_LEFT = pygame.K_a
KEYBIND_ROTATE_RIGHT = pygame.K_d
KEYBIND_MOVE_FORWARD = pygame.K_w
KEYBIND_MOVE_BACKWARD = pygame.K_s