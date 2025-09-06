import pygame
import random
from constants import ASTEROID_MIN_RADIUS, ASTEROID_SPEEDUP_RATE
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_a = self.velocity.rotate(random_angle)
        asteroid_b = self.velocity.rotate(-random_angle)
        first_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        second_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        #print(f"{self.position[0]} , {self.position[1]}")
        first_asteroid.velocity = asteroid_a * ASTEROID_SPEEDUP_RATE
        second_asteroid.velocity = asteroid_b * ASTEROID_SPEEDUP_RATE
