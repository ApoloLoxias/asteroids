import pygame
from constants import *

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
        self.O = self.position

    def draw(self, screen):
        pygame.draw.circle(screen, ASTEROID_COLOUR, self.position, self.radius, LINE_WIDTH)


    def update(self, dt):
        # must override
        pass

    def collides_with(self, other):
        if self.position.distance_to(other.position) < self.radius + other.radius:
            return True
        return False
    
class Segment(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.A = pygame.Vector2(x1, y1)
        self.B = pygame.Vector2(x2, y2)

    def draw(self, screen):
        pygame.draw.line(screen, (240,40,40), self.A, self.B)

class Dot(pygame.sprite.Sprite):
    def __init__(self, x, y, colour=ASTEROID_COLOUR):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.colour = colour
    
    def project(self, A: "Dot", B: "Dot"):
        AB = B.position-A.position
        AO = self.position-A.position
        ab = AB.normalize()
        return AO.dot(ab)*ab + A.position
    
    def distance_to_line(self, A: "Dot", B: "Dot"):
        P = self.project(A, B)
        OP = P - self.position
        return OP.length()

    def distance_to_dot(self, A: "Dot"):
        OA = A.position - self.position
        return OA.length()
    
    def distance_to_segment(self, A: "Dot", B: "Dot"):
        AB = B.position-A.position
        AO = self.position-A.position
        d = AO.dot(AB) / (AB.length() ** 2)
        if d<0:
            return self.distance_to_dot(A)
        if d>1:
            return self.distance_to_dot(B)
        return self.distance_to_line(A,B)

    def centre_within(self, A: "Dot", B: "Dot", C: "Dot"):
        AB = B.position - A.position
        BC = C.position - B.position
        CA = A.position - C.position
        AO = self.position - A.position
        BO = self.position - B.position
        CO = self.position - C.position
        return AB.cross(AO) * BC.cross(BO) >= 0 and BC.cross(BO) * CA.cross(CO) >= 0

    def distance_to_triangle(self, A: "Dot", B: "Dot", C: "Dot"):
        if self.centre_within(A, B, C):
            return 0
        return min(self.distance_to_segment(A, B), self.distance_to_segment(A, C),self.distance_to_segment(B, C))

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.position, 1, LINE_WIDTH)