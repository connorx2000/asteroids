import pygame
from pygame import mixer
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shooting import Shot
from explosion import Explosin_anim
from sounds import play_sound
from engine import Engine_anim

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pygame Asteroid Shooter!")
    clock = pygame.time.Clock()
    
    dt = 0
    score = PLAYER_SCORE
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    explosions = pygame.sprite.Group()

    #Groups
    Player.containers = (updatable, drawable)
    Engine_anim.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Explosin_anim.containers = (explosions, updatable, drawable)
    Shot.containers = (bullets, updatable, drawable)

    active_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    active_astroid_field = AsteroidField()

    #Textures
    heart_full = pygame.image.load("./images/heart_full.png")
    heart_empty = pygame.image.load("./images/heart_empty.png") 

    #Background
    background = pygame.image.load("./images/background.png")
    background_scaled = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    #Fonts
    font = pygame.font.Font(None, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        text_surface = font.render(f"Score: {score}" , True, "WHITE")
        screen.blit(text_surface, (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 50))
        
        dt = clock.tick(60) / 1000
        updatable.update(dt)

        #Draws Background
        screen.blit(background_scaled, (0, 0))

        #Draws Sprites
        for sprite in drawable:
            sprite.draw(screen)

        # Draws players hearts
        for i in range(PLAYER_HEALTH):
                x = 10 + i * 60
                if i < active_player.player_health:
                    screen.blit(heart_full, ( x, SCREEN_HEIGHT - 60))
                else:
                    screen.blit(heart_empty, ( x, SCREEN_HEIGHT - 60))

        # Astroid collision system
        for asteroid in asteroids:
            if asteroid.collision(active_player):
                if active_player.health(1):
                    print(f"You have {active_player.player_health} remaining lives!")
                    play_sound("damage", 0.5)
                    break
                elif active_player.player_health == 0:
                    raise SystemExit (f"Game over, you scored {score}!")
                else:
                    #print(f"Player is immune to dmg for {active_player.player_dmg_cooldown} seconds!") 
                    pass

        # Bullet collision system
        for bullet in bullets:
            for asteroid in asteroids:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.split()
                    score += 1
                    play_sound("explosion", 0.25)
                    explosions.add(Explosin_anim(asteroid.position[0], asteroid.position[1], asteroid.radius))
                    
                

        pygame.display.flip()

if __name__ == "__main__":
    main()