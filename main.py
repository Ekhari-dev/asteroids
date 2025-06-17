import pygame
from constants import *
from player import *

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

    Player.containers = (updateable, drawable)
    player = Player(x, y)

    #game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        
        updateable.update(dt)
        
        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()

        # Limit Frame Rate to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()