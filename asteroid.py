import pygame
import random

from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_COLOUR, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.mass = radius ** 3
    
    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOUR, self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        split_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(split_angle)
        velocity2 = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid1.velocity = 1.2 * velocity1
        asteroid2.velocity = 1.2 * velocity2

    def bounce(self, other: "Asteroid"):
        m1 = self.mass
        m2 = other.mass
        v1 = self.velocity
        v2 = other.velocity
        O1 = self.position
        O2 = other.position
        dv = v1-v2
        dO = O1-O2
        self.velocity =  v1 + ((2*m1)/(m1+m2))*((dv.dot(dO))/((O1.distance_to(O2))**2))*dO.normalize()