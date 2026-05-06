import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    # print(f"Starting Asteroids with pygame version: {pygame.version.ver}!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    user = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #Draw the screen
        screen.fill("black")
        user.draw(screen)
        
        # Delta functions
        dt += clock.tick(60)/1000
        user.update(dt)
        
        #Display everything
        pygame.display.flip()
        
        

if __name__ == "__main__":
    main()
