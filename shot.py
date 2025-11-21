import pygame
from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED, LINE_WIDTH, SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, radius = SHOT_RADIUS)
        
        self.velocity = direction * PLAYER_SHOOT_SPEED

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
