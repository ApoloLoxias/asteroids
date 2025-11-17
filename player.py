import pygame
from triangleshape import TriangleShape
from constants import (LINE_WIDTH,
                       PLAYER_RADIUS,
                       PLAYER_COLOUR,
                       PLAYER_TURN_SPEED,
                       GYRO_SPEED,
                       PLAYER_SPEED,
                       PLAYER_SHOT_SPEED,
                       PLAYER_SHOT_COOLDOWN,
                       KEYBIND_ROTATE_LEFT,
                       KEYBIND_ROTATE_RIGHT,
                       KEYBIND_MOVE_FORWARD,
                       KEYBIND_MOVE_BACKWARD,
                       SCREEN_HEIGHT,
                       SCREEN_WIDTH,)
from shot import Shot

class Player(TriangleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.shot_timer = 0
    
    # draws a triangular sprite on the screen, using the vertices from triangle(self)
    def draw(self, screen):
        pygame.draw.polygon(screen, PLAYER_COLOUR, self.triangle(), LINE_WIDTH)


    def thrust(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.velocity += rotated_with_speed_vector
    def gimbal(self, dt):
        self.angular_velocity += PLAYER_TURN_SPEED * dt
        return
    def stabilize(self, dt):
        if self.angular_velocity > 0:
            self.angular_velocity -= GYRO_SPEED * dt
        if self.angular_velocity < 0:
            self.angular_velocity += GYRO_SPEED * dt

    def rotate(self, dt):
        self.rotation += self.angular_velocity * dt
        return
    def move (self, dt):
        self.position += self.velocity * dt


    def shoot(self):
        if self.shot_timer > 0:
            return
        shot = Shot(self.position[0], self.position[1])
        shot.velocity =  pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        self.shot_timer = PLAYER_SHOT_COOLDOWN
    #
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_timer -= dt

        if keys[KEYBIND_ROTATE_LEFT]:
            self.gimbal(-dt)
        elif keys[KEYBIND_ROTATE_RIGHT]:
            self.gimbal(dt)
        else:
            self.stabilize(dt)
        if keys[KEYBIND_MOVE_FORWARD]:
            self.thrust(dt)
        if keys[KEYBIND_MOVE_BACKWARD]:
            self.thrust(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.move(dt)
        self.rotate(dt)

        if self.position[0] < 0:
            self.position[0] = SCREEN_WIDTH
        if self.position[0] > SCREEN_WIDTH:
            self.position[0] = 0
        if self. position[1] <0:
            self.position[1] = SCREEN_HEIGHT
        if self.position[1] > SCREEN_HEIGHT:
            self.position [1] = 0