import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shooting import Shot

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

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (bullets, updatable, drawable)

    active_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    active_astroid_field = AsteroidField()

    font = pygame.font.Font(None, 50)
    #satext_surface = font.render(f"Score: {score}" , True, "WHITE")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        text_surface = font.render(f"Score: {score}" , True, "WHITE")
        screen.blit(text_surface, (SCREEN_WIDTH - 200, SCREEN_HEIGHT - 50))
        
        dt = clock.tick(60) / 1000
        updatable.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        for asteroid in asteroids:
            if asteroid.collision(active_player):
                if active_player.health(1):
                    print(f"You have {active_player.player_health} remaining lives!")
                    break
                elif active_player.player_health == 0:
                    raise SystemExit (f"Game over, you scored {score}!")
                else:
                    print(f"Player is immune to dmg for {active_player.player_dmg_cooldown} seconds!") 
            
        for bullet in bullets:
            for asteroid in asteroids:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.split()
                    score += 1
                

        pygame.display.flip()

if __name__ == "__main__":
    main()