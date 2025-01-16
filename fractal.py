# fractal.py

import pygame
import numpy as np
import random
from utils import generate_random_sid

def mandelbrot(c, max_iter):
    """Calculate the Mandelbrot value for a given complex number."""
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def generate_random_color():
    """Generate a random color."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generate_fractal(screen, width, height):
    """Generate and draw a random fractal on the screen."""
    # Randomly choose a fractal type
    fractal_type = random.choice(['mandelbrot', 'julia'])
    
    if fractal_type == 'mandelbrot':
        # Define the area of the complex plane to visualize
        x_min, x_max = -2.0, 1.0
        y_min, y_max = -1.5, 1.5
        max_iter = 100
        
        # Generate a random color for the Mandelbrot fractal
        base_color = generate_random_color()
        
        for x in range(width):
            for y in range(height):
                # Map pixel position to complex number
                c = complex(x_min + (x / width) * (x_max - x_min),
                            y_min + (y / height) * (y_max - y_min))
                m = mandelbrot(c, max_iter)
                
                # Create a color based on the number of iterations
                if m < max_iter:
                    # Create a color gradient based on the iteration count
                    color = (
                        (base_color[0] + m * 2) % 256,
                        (base_color[1] + m * 5) % 256,
                        (base_color[2] + m * 3) % 256
                    )
                else:
                    color = (0, 0, 0)  # Black for points inside the set
                
                screen.set_at((x, y), color)

    elif fractal_type == 'julia':
        # Generate a random SID for the Julia set
        sid = generate_random_sid()
        max_iter = 100
        c = complex(random.uniform(-1, 1), random.uniform(-1, 1))
        
        # Generate a random color for the Julia fractal
        base_color = generate_random_color()
        
        for x in range(width):
            for y in range(height):
                z = complex(x / width * 4 - 2, y / height * 4 - 2)
                n = 0
                while abs(z) <= 2 and n < max_iter:
                    z = z*z + c
                    n += 1
                
                # Create a color based on the number of iterations
                if n < max_iter:
                    color = (
                        (base_color[0] + n * 2) % 256,
                        (base_color[1] + n * 5) % 256,
                        (base_color[2] + n * 3) % 256
                    )
                else:
                    color = (0, 0, 0)  # Black for points inside the set
                
                screen.set_at((x, y), color)