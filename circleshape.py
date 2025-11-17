import pygame
from triangleshape import TriangleShape

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides_with(self, other):
        if isinstance(other, CircleShape):
            if self.position.distance_to(other.position) < self.radius + other.radius:
                return True
            return False
        if isinstance(other, TriangleShape):
            A = other.triangle()[0]
            B = other.triangle()[1]
            C = other.triangle()[2]
            if self.distance_to_triangle(A, B, C) < self.radius:
                return True
            return False
        
    def distance_to_triangle(self, A: pygame.Vector2, B: pygame.Vector2, C: pygame.Vector2):
        if self.centre_within(A, B, C):
            return 0
        return min(self.distance_to_segment(A, B), self.distance_to_segment(A, C),self.distance_to_segment(B, C));
    
    def centre_within(self, A: pygame.Vector2, B: pygame.Vector2, C: pygame.Vector2):
        AB = B - A
        BC = C - B
        CA = A - C
        AO = self.position - A
        BO = self.position - B
        CO = self.position - C
        return AB.cross(AO) * BC.cross(BO) >= 0 and BC.cross(BO) * CA.cross(CO) >= 0

    def distance_to_segment(self, A: pygame.Vector2, B: pygame.Vector2):
        AB = B - A
        AO = self.position-A
        d = AO.dot(AB) / (AB.length() ** 2)
        if d<0:
            return self.distance_to_dot(A)
        if d>1:
            return self.distance_to_dot(B)
        return self.distance_to_line(A,B)

    def distance_to_dot(self, A: pygame.Vector2):
        OA = A - self.position
        return OA.length()

    def distance_to_line(self, A: pygame.Vector2, B: pygame.Vector2):
        P = self.project(A, B)
        OP = P - self.position
        return OP.length()

    def project(self, A: pygame.Vector2, B: pygame.Vector2):
        AB = B - A
        AO = self.position - A
        ab = AB.normalize()
        return AO.dot(ab)*ab + A