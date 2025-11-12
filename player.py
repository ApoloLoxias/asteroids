import pygame
from circleshape import CircleShape
from constants import (LINE_WIDTH,
                       PLAYER_RADIUS,
                       PLAYER_COLOUR,)

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
    
    # Calculates vertices of a triangle to be displayed, based on the circular hitbox
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    # draws a triangular sprite on the screen, using the vertices from triangle(self)
    def draw(self, screen):
        pygame.draw.polygon(screen, PLAYER_COLOUR, self.triangle(), LINE_WIDTH)

    