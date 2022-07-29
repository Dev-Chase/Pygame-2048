# Run this file to play game
from random import randint, seed
import sys

if __name__ == '__main__':
    from settings import *
    from world import World
    # Pygame Setup
    pygame.init()
    SCREEN_SIZE = (W, H)
    screen = pygame.display.set_mode(SCREEN_SIZE)
    screenshake = 0
    offs = (0, 0)
    display = pygame.Surface(SCREEN_SIZE)
    clock = pygame.time.Clock()
    game_name = 'Sample Name'
    pygame.display.set_caption(game_name)
    world = World(display)
    Run = True
else: Run = False

seed(randint(0, 9999999999999999999999999999999))
while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False
            pygame.quit()
            sys.exit()
    
    display.fill(colours['white'])
    
    world.update()
    
    screen.blit(pygame.transform.scale(display, SCREEN_SIZE), offs)
    
    pygame.display.update()
    clock.tick(180)