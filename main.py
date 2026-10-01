import pygame
from pygame import display
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
import sys


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}") 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (drawable, updatable, shots)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    pygame.init()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    while True:
        log_state()
        updatable.update(dt)

        for event in pygame.event.get():
            for asteroid in asteroids:
                if asteroid.collides_with(player) == True:
                    log_event("player_hit")
                    print("Game over!")
                    sys.exit()
                for shot in shots:
                    if asteroid.collides_with(shot) == True:
                        log_event("asteroid_shot")
                        asteroid.split()
                        shot.kill()

            if event.type == pygame.QUIT:
                return
        screen.fill("black ")
        for sprite in drawable:
            sprite.draw(screen)
        display.flip()
        dt = clock.tick(60) / 1000.0
    
    

if __name__ == "__main__":
    main()
