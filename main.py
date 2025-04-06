import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    # init pygame
    pygame.init()

    # set options
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # fps rate limiter
    clock = pygame.time.Clock()
    dt = 0

    # player groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    # asteroid groups
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    # shot groups
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)


    # init player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # infinite loop runs game
    while True:
        # enable x button to quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # player updates
        updatable.update(dt)
        
        # fill screen with RGB value
        color = [0,0,0]
        screen.fill(color)

        # asteroid collision
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                sys.exit()

            # shot collision
            for shot in shots:
                if asteroid.collide(shot):
                    shot.kill()
                    asteroid.kill()

        # player draws
        for item in drawable:
            item.draw(screen)

        # update display
        pygame.display.flip()
        
        # ticks
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
