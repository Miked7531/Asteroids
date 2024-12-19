import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self,x,y,radius,velocity=None):
        super().__init__(x,y,radius)
        self.velocity = velocity

    def draw(self,screen):
        pygame.draw.circle(screen,(255,255,255),self.position,self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)
        new_velocity1 = self.velocity.rotate(random_angle) * 1.4
        new_velocity2 = self.velocity.rotate(-random_angle) * 1.4
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # creates new asteroid objects and sets their velocity when split
        asteroid1 = Asteroid(x=self.position.x, y=self.position.y, radius=new_radius, velocity=new_velocity1)
        asteroid2 = Asteroid(x=self.position.x, y=self.position.y, radius=new_radius, velocity=new_velocity2)
        
        for group in self.groups():
            group.add(asteroid1)
            group.add(asteroid2)