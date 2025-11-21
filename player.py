import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1)
        if keys[pygame.K_d]:
            self.rotate(1)
        if keys[pygame.K_w]:
            self.move(1)
        if keys[pygame.K_s]:
            self.move(-1)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()
            self.timer = PLAYER_SHOOT_COOLDOWN_SECONDS

        # Checks to see if the player's shot is on cooldown
        if self.timer > 0:
            self.timer -= dt
    
    def move(self, dt):
        vector = pygame.Vector2(0, 1)
        rotated_vector = vector.rotate(self.rotation)
        rotated_vector_w_speed = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_vector_w_speed

    def shoot(self):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        position = self.position.copy()

        return Shot(position.x, position.y, direction)
