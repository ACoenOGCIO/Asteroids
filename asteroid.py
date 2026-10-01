from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random
import copy

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw (self, screen):
        # Draw the asteroid as a circle
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), self.radius, LINE_WIDTH)

    def update(self, dt):
        # Update the asteroid's position based on its velocity
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            asteroid1_velocity = copy.deepcopy(self.velocity)
            asteroid2_velocity = copy.deepcopy(self.velocity)
            asteroid1_velocity.rotate_ip(angle)
            asteroid2_velocity.rotate_ip(angle * -1)
            asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, asteroid_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, asteroid_radius)
            asteroid1.velocity = asteroid1_velocity * 1.2
            asteroid2.velocity = asteroid2_velocity * 1.2
            

