import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main ():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    

    #Groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    player = Player(x, y)

    Asteroid.containers = (asteroids, updateable, drawable)

    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()

    Shot.containers = (drawable, updateable, shots)

    #game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        
        updateable.update(dt)
        for item in asteroids:
            if item.collision(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collision(item):
                    shot.kill()
                    split_results = item.split()
                    if split_results is not None:
                        new_vector_1, new_vector_2, new_radius = split_results
                        asteroid_field.spawn(new_radius, item.position, new_vector_1 * 1.2)
                        asteroid_field.spawn(new_radius, item.position, new_vector_2 * 1.2)
                    
        
        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()

        # Limit Frame Rate to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()