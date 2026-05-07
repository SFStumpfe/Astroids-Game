import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import *
from asteroid import *
from asteroidfield import *
from score import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    score = Score()
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Score.containers = (drawable,)
    Shot.containers = (shots, updatable, drawable)    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    user = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    AsteroidField()
    while True:
        log_state()
        dt = clock.tick(60)/1000
        updatable.update(dt)
        for i in asteroids:
            if i.collides_self(user):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for k in shots:
                if k.collides_self(i):
                    log_event("asteroid_shot")
                    i.split()
                    k.kill()
                    score.add_point()                   
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            
        #Draw the screen
        screen.fill("black")
        for container in drawable:
            container.draw(screen)
            font = pygame.font.Font(None, 36)
            text = font.render(f"Score: {score.score}", True, "white")
            text2 = font.render(f"High Score: {score.high_score}", True, "white")
            screen.blit(text, (10, 10))   
            screen.blit(text2, (10, 40))
            
        
        #Display everything
        pygame.display.flip()
        
        

if __name__ == "__main__":
    main()
