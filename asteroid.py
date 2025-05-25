import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        asteroid_color = (255, 255, 255)
        pygame.draw.circle(screen, asteroid_color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <=  ASTEROID_MIN_RADIUS:
            return
        else:
            old_radius = self.radius
            random_angle = random.uniform(20, 50)
            new_radius = old_radius - ASTEROID_MIN_RADIUS

            pos_rotate = self.velocity.rotate(random_angle)
            Asteroid(self.position[0], self.position[1], new_radius, pos_rotate * 1.2)
            
            neg_rotate = self.velocity.rotate(-random_angle)
            Asteroid(self.position[0], self.position[1], new_radius, neg_rotate * 1.2)
            
            
            