import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Rotating Planet")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

class Planet:
    def __init__(self, center_x, center_y, radius, color, angle):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.color = color
        self.angle = angle  # Initial angle
        self.x = self.center_x + self.radius * math.cos(self.angle)
        self.y = self.center_y + self.radius * math.sin(self.angle)
        
    def update(self):
        self.angle += 0.01  # Increment the angle for rotation
        self.x = self.center_x + self.radius * math.cos(self.angle)
        self.y = self.center_y + self.radius * math.sin(self.angle)
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Create a planet instance
center_x = screen_width // 2
center_y = screen_height // 2
planet = Planet(center_x, center_y, 50, green, 0)  # Initial angle is 0

# Set up game loop variables
clock = pygame.time.Clock()
is_running = True

# Main game loop
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
    # Update game logic
    planet.update()
    
    # Clear the screen
    screen.fill(black)
    
    # Draw game objects
    planet.draw(screen)
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
sys.exit()
