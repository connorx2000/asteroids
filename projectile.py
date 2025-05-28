import pygame
from animation import Animation
from circleshape import CircleShape
from constants import *

class Projectile(CircleShape):
    def __init__(self, x, y, velocity, player_rotation):

        #Bullet Textures
        self.laser_projectile = pygame.image.load("./images/projectiles/laser_projectile.png")
        self.ray_projectile = pygame.image.load("./images/projectiles/ray_projectile.png")
        self.rocket_projectile = pygame.image.load("./images/projectiles/rocket_projectile.png")
        self.torpedo_projectile = pygame.image.load("./images/projectiles/torpedo_projectile.png")

        projectile = {
            'laser': self.laser_projectile,
            'ray': self.ray_projectile,
            'rocket': self.rocket_projectile,
            'torpedo': self.torpedo_projectile
        }

        self.active_projectile = "laser"
        self.rotation = player_rotation

        self.row = 1
        self.col = 1
        if self.active_projectile == "laser":
            self.col = 5
            projectile_frames = 5
        elif self.active_projectile == "ray" or self.active_projectile == "rocket":
            self.col = 4
            projectile_frames = 4
        else:
            self.col = 3
            projectile_frames = 3

        self.spritesheet = projectile.get(self.active_projectile)
        super().__init__(x, y, SHOT_RADIUS)

        self.velocity = velocity

        for group in Projectile.containers:
            group.add(self)

        self.frame_delay = FRAME_DELAY
        
        self.current_frame = 0
        self.time_since_last_frame = 0
        
        self.radius = SHOT_RADIUS
        self.num_frames = projectile_frames
        self.frames = self.extract_frames(self.row, self.col)
        
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=(x, y))     

        self.position = pygame.Vector2(x, y)
        self.last_update_time = pygame.time.get_ticks()
        

    def update(self, dt):
        self.time_since_last_frame += dt
        self.position += (self.velocity * dt)
        self.rect = self.image.get_rect(center=(self.position))
        if self.time_since_last_frame > self.frame_delay:
            self.time_since_last_frame = 0
            self.current_frame += 1
            if self.current_frame < len(self.frames):
                self.image = self.frames[self.current_frame]
            if self.current_frame >= len(self.frames):
                self.current_frame = 0
    
    def extract_frames(self, row, col):
        frames = []
        frame_width = int(self.spritesheet.get_width() / col)
        frame_height = int(self.spritesheet.get_height() / row)

        for i in range(self.num_frames):
            col_index = i % col
            row_index = i // col
            frame = self.spritesheet.subsurface(pygame.Rect(col_index * frame_width, row_index * frame_height, frame_width, frame_height))
            frames.append(frame)
        return frames
    
    
    def draw(self, surface):
        #surface.blit(self.image, self.rect)

        active_projectile = self.frames[self.current_frame]

        projectile_rotated = self.rotate_image(active_projectile, -self.rotation -180)
        projectile_rotated_rect = self.rotated_rect(active_projectile, (self.position[0], self.position[1]))
            
        surface.blit(projectile_rotated, projectile_rotated_rect)

        #Debug to show collision radius
        #asteroid_color = (255, 255, 255)
        #pygame.draw.circle(surface, asteroid_color, self.position, self.radius, 2)

    def rotate_image(self, image_to_rotate, rotation):
        return pygame.transform.rotate(image_to_rotate, rotation)

    def rotated_rect(self, rotated_image, image_center):
        return rotated_image.get_rect(center=image_center)

    def collision(self, other):
        distance = self.position.distance_to(other.position)
        if distance <= (self.radius + other.radius):
            return True
        else:
            return False