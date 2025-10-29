from circleshape import CircleShape
from constants import *
import pygame   

class Shot(CircleShape):
    def __init__(self, x, y, lifetime=30.0):
        super().__init__(x, y, SHOT_RADIUS)
        self.lifetime = lifetime

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        if self.lifetime <= 0:
            self.kill()
        else:
            self.position += (self.velocity * dt)
            self.lifetime -= dt 