import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    Player.containers = (updateable_group, drawable_group)
    Asteroid.containers = (asteroid_group, updateable_group, drawable_group)
    AsteroidField.containers = (updateable_group)
    Shot.containers = (updateable_group, drawable_group, shots_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updateable_group.update(dt)
        for asteroid in asteroid_group:
            if asteroid.colision(player):
                print("Game over!")
                sys.exit()
            for shot in shots_group:
                if asteroid.colision(shot):
                    asteroid.kill()
                    shot.kill()
        for drawable in drawable_group:
            drawable.draw(screen)
        pygame.display.flip()
        #limit frame rate to 60 fps
        dt = clock.tick(60)/1000




if __name__ == "__main__":
    main()
