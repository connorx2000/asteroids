import pygame
from animation import Animation
from constants import *

class Explosin_anim(Animation):
    def __init__(self, x, y, radius):
        spritesheet = pygame.image.load("./images/explosion_spritesheet.png")
        super().__init__(x, y, spritesheet, num_frames = 16)
        for group in Explosin_anim.containers:
            group.add(self)

        self.frame_delay = FRAME_DELAY
        self.row = 4
        self.col = 4
        self.current_frame = 0
        self.time_since_last_frame = 0
        self.radius = radius
        self.frames = self.extract_frames(self.row, self.col)
        self.scale_explosion(radius)
        
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))
        

    def update(self, dt):
        self.time_since_last_frame += dt
        if self.time_since_last_frame > self.frame_delay:
            self.time_since_last_frame = 0
            self.current_frame += 1
            if self.current_frame < len(self.frames):
                self.image = self.frames[self.current_frame]
            if self.current_frame >= len(self.frames):
                #print("Explosion deleted!")
                self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def scale_explosion(self, radius):
        desired_size = radius * 2
        scaled_frames = []
        for frame in self.frames:
            scaled = pygame.transform.scale(frame, (desired_size, desired_size))
            scaled_frames.append(scaled)
        self.frames = scaled_frames