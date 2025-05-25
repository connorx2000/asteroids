import pygame
from constants import *

def main():
    pygame.init
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_on = 0
    background = '#000000'
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while game_on == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, background)
        pygame.display.flip()

if __name__ == "__main__":
    main()