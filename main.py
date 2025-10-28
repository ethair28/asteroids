from constants import *
import pygame
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    max_fps = 60
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        updatable.update(dt)
        screen.fill((0, 0, 0))
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(max_fps) / 1000
    pygame.quit()
if __name__ == "__main__":
    main()
