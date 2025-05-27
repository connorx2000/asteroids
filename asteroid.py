import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

        #Textures
        self.asteroid_texture = pygame.image.load("./images/asteroid.png")

    def draw(self, screen):
        desired_size = self.radius * 2
        scaled_asteroid = pygame.transform.scale(self.asteroid_texture, (desired_size, desired_size))
        screen.blit(scaled_asteroid, (self.position[0] - desired_size / 2, self.position[1] - desired_size / 2))

        #Debug to show collision radius
        #asteroid_color = (255, 255, 255)
        #pygame.draw.circle(screen, asteroid_color, self.position, self.radius * 0.5, 2)

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
            
    def collision(self, other):
        distance = self.position.distance_to(other.position)
        if distance <= (self.radius * 0.5 + other.radius):
            return True
        else:
            return False