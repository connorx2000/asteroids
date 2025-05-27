import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = velocity
        
    def draw(self, screen):
        
        
        #check ship
        #get image
        #play animation when shot

        #Original bullet
        asteroid_color = (255, 255, 255)
        pygame.draw.circle(screen, asteroid_color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)