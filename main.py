import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updateable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    Player.containers = (updateable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updateable_group.update(dt)
        for drawable in drawable_group:
            drawable.draw(screen)
        pygame.display.flip()
        #limit frame rate to 60 fps
        dt = clock.tick(60)/1000




if __name__ == "__main__":
    main()
