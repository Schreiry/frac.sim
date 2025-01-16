# main.py

import pygame
import random
from fractal import generate_fractal
from utils import SID_COUNT

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Real-Time Fractal Simulation")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Generate and draw a random fractal
    generate_fractal(screen, WIDTH, HEIGHT)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()