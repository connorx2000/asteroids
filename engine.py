import pygame
from animation import Animation
from constants import *

class Engine_anim(Animation):
    def __init__(self, x, y, radius, active_ship):

        #Ship Textures
        self.battlecruiser_engine = pygame.image.load("./images/engines/battlecruiser_engine.png")
        self.bomber_engine = pygame.image.load("./images/engines/bomber_engine.png")
        self.dreadnought_engine = pygame.image.load("./images/engines/dreadnought_engine.png")
        self.fighter_engine = pygame.image.load("./images/engines/fighter_engine.png")
        self.frigate_engine = pygame.image.load("./images/engines/frigate_engine.png")
        self.support_engine = pygame.image.load("./images/engines/support_engine.png")
        self.torpedo_engine = pygame.image.load("./images/engines/torpedo_engine.png")

        engines = {
            'battlecruiser': self.battlecruiser_engine,
            'bomber': self.bomber_engine,
            'dreadnought': self.dreadnought_engine,
            'fighter': self.fighter_engine,
            'frigate': self.frigate_engine,
            'support': self.support_engine,
            'torpedo': self.torpedo_engine
        }

        spritesheet = engines.get(active_ship)
        super().__init__(x, y, spritesheet, num_frames = 8)
        for group in Engine_anim.containers:
            group.add(self)

        self.frame_delay = FRAME_DELAY
        self.row = 1
        self.col = 8
        self.current_frame = 0
        self.time_since_last_frame = 0
        self.radius = radius
        self.frames = self.extract_frames(self.row, self.col)
        
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
                self.current_frame = 0

    def draw(self, surface):
        pass