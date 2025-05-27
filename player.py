import pygame
from constants import *
from circleshape import CircleShape
from shooting import Shot
from sounds import play_sound
from engine import Engine_anim


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        self.player_health = PLAYER_HEALTH
        self.player_dmg_cooldown = 0

        #Ship Textures
        self.battlecruiser_ship = pygame.image.load("./images/ships/battlecruiser_ship.png")
        self.bomber_ship = pygame.image.load("./images/ships/bomber_ship.png")
        self.dreadnought_ship = pygame.image.load("./images/ships/dreadnought_ship.png")
        self.fighter_ship = pygame.image.load("./images/ships/fighter_ship.png")
        self.frigate_ship = pygame.image.load("./images/ships/frigate_ship.png")
        self.support_ship = pygame.image.load("./images/ships/support_ship.png")
        self.torpedo_ship = pygame.image.load("./images/ships/torpedo_ship.png")

        self.active_ship = "frigate"

        self.ships = {
            'battlecruiser': self.battlecruiser_ship,
            'bomber': self.bomber_ship,
            'dreadnought': self.dreadnought_ship,
            'fighter': self.fighter_ship,
            'frigate': self.frigate_ship,
            'support': self.support_ship,
            'torpedo': self.torpedo_ship
        }
        self.active_engine = Engine_anim(self.position[0], self.position[1], self.radius, self.active_ship)

    def draw(self, screen):
        if (int(self.player_dmg_cooldown * 10) % 2) == 0:
            
            active_ship = self.ships.get(self.active_ship)
            active_engine = self.active_engine.frames[self.active_engine.current_frame]
            width, height = active_ship.get_size()
            #rotated_image = pygame.transform.rotate(active_ship, -self.rotation -180)
            #rotated_rect = rotated_image.get_rect(center=(self.position[0], self.position[1]))

            player_rotated = self.rotate_image(active_ship, -self.rotation -180)
            player_rotated_rect = self.rotated_rect(player_rotated, (self.position[0], self.position[1]))
            engine_rotated = self.rotate_image(active_engine, -self.rotation -180)
            engine_rotated_rect = self.rotated_rect(engine_rotated, (self.position[0], self.position[1]))

            screen.blit(engine_rotated, engine_rotated_rect)
            screen.blit(player_rotated, player_rotated_rect)
            

            #Debug to show collision radius
            #player_color = (255, 255, 255)
            #pygame.draw.circle(screen, player_color, self.position, self.radius, 2)
    
    def rotate_image(self, image_to_rotate, rotation):
        return pygame.transform.rotate(image_to_rotate, rotation)

    def rotated_rect(self, rotated_image, image_center):
        return rotated_image.get_rect(center=image_center)

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
            
