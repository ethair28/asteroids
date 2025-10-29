from circleshape import CircleShape
import pygame
import random 
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, lifetime=30.0):
        super().__init__(x, y, radius)
        self.lifetime = lifetime
    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255, 255, 255), self.position, self.radius, width=2)

    def update(self, dt):
        if self.lifetime <= 0:
            self.kill()
        else:
            self.position += (self.velocity * dt)
            self.lifetime -= dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            random_angle = random.uniform(20, 50)
            asteroid_1_v = self.velocity.rotate(random_angle) * 1.2
            asteroid_2_v = self.velocity.rotate(-random_angle) * 1.2
            asteroid_1_r = self.radius - ASTEROID_MIN_RADIUS
            asteroid_2_r = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, asteroid_1_r)
            asteroid_2 = Asteroid(self.position.x, self.position.y, asteroid_2_r)
            asteroid_1.velocity = asteroid_1_v
            asteroid_2.velocity = asteroid_2_v



