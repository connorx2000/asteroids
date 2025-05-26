import pygame
from constants import *
from circleshape import CircleShape
from shooting import Shot
from sounds import play_sound


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.player_health = PLAYER_HEALTH
        self.player_dmg_cooldown = 0

    def draw(self, screen):
        if (int(self.player_dmg_cooldown * 10) % 2) == 0:
            player_color = (255, 255, 255)
            pygame.draw.polygon(screen, player_color, self.triangle(), 2)
        else:
            pass
        

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
        self.shot_timer -= dt
        self.player_dmg_cooldown -= dt
        if self.player_dmg_cooldown < 0:
            self.player_dmg_cooldown = 0

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.shot_timer < 0:
            self.shoot(self)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt#

    def shoot(self, dt):
        forward = (pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED)
        Shot(self.position[0], self.position[1], forward)
        play_sound("shooting", 0.5)
        self.shot_timer = PLAYER_SHOOT_COOLDOWN

    def health(self, dmg):
        if self.player_dmg_cooldown > 0:
            return False
        elif self.player_dmg_cooldown == 0:
            self.player_health -= dmg
            self.player_dmg_cooldown = PLAYER_DMG_COOLDOWN
            return True
            
