import pygame
import random as rand
from logger import *
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt):
        self.position += self.velocity*dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            degree = rand.uniform(20, 50)
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            
            as1 = Asteroid(self.position.x, self.position.y, new_rad)
            as2 = Asteroid(self.position.x, self.position.y, new_rad)
            as1.velocity = self.velocity.rotate(degree)*1.2
            as2.velocity = self.velocity.rotate(-degree)*1.2
            
            