import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shooting import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    dt = 0

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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        
        dt = clock.tick(60) / 1000
        updatable.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        for asteroid in asteroids:
            if asteroid.collision(active_player):
                distance = asteroid.position.distance_to(active_player.position)
                print(f"Player collision! Distance: {distance}")
                raise SystemExit ("Game over!")
            
        for bullet in bullets:
            for asteroid in asteroids:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.split()
                

        pygame.display.flip()

if __name__ == "__main__":
    main()