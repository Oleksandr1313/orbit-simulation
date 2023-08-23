import pygame
import sys
import math

pygame.init()

# Display dimensions
WIDTH, HEIGHT = 500, 500

# Colors
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)

# Display
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Orbit Simulation")

# FPS
clock = pygame.time.Clock()

# Simulation continues
is_running = True

# CLASSES
class Planet:
    def __init__(self, x, y, color, angle, radius, major_radius, minor_radius, angular_increase):
        self.x = x
        self.y = y
        self.color = color
        self.angle = angle
        self.radius = radius
        self.major_radius = major_radius
        self.minor_radius = minor_radius
        self.angular_increase = angular_increase

    def motion(self):
        self.angle += self.angular_increase
        self.x = WIDTH // 2 + self.major_radius * math.cos(self.angle)
        self.y = HEIGHT // 2 + self.minor_radius * math.sin(self.angle)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

earth = Planet(WIDTH // 2, HEIGHT // 2, blue, 0, 12, 125, 125, 0.008) 
mars = Planet(WIDTH // 2, HEIGHT // 2, red, 0, 8, 200, 200, 0.005) 
sun = Planet(WIDTH // 2, HEIGHT // 2, yellow, 0, 30, 0, 0, 0) 

# GAME LOOP
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    display.fill(black)

    #sun
    sun.draw(display)

    #mars
    mars.motion()
    mars.draw(display)

    #earth
    earth.motion()
    earth.draw(display)

    pygame.display.flip()

    clock.tick(120)

pygame.quit()
sys.exit()
