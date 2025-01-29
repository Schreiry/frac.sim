# fractal.py

import pygame
import numpy as np
import random

def generate_random_color():
    """Generate a random color."""
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generate_unique_fractal(screen, width, height, step):
    """Generate and draw a unique fractal on the screen."""
    # Определяем случайные параметры для фрактала
    max_iter = random.randint(50, 200)
    x_min, x_max = random.uniform(-2.0, 2.0), random.uniform(-2.0, 2.0)
    y_min, y_max = random.uniform(-2.0, 2.0), random.uniform(-2.0, 2.0)

    # Генерируем случайный цвет
    base_color = generate_random_color()

    for x in range(0, width, step):
        for y in range(0, height, step):
            # Преобразуем пиксель в комплексное число
            c = complex(x_min + (x / width) * (x_max - x_min),
                        y_min + (y / height) * (y_max - y_min))
            z = 0
            n = 0
            while abs(z) <= 2 and n < max_iter:
                z = z*z + c
                n += 1
            
            # Создаем цвет на основе количества итераций
            if n < max_iter:
                color = (
                    (base_color[0] + n * 2) % 256,
                    (base_color[1] + n * 5) % 256,
                    (base_color[2] + n * 3) % 256
                )
            else:
                color = (0, 0, 0)  # Черный для точек внутри множества
            
            # Устанавливаем цвет пикселя
            screen.set_at((x, y), color)

def draw_fractal(screen, width, height):
    """Постепенно рисует фрактал на экране."""
    step = 1
    while step <= 10:  # Увеличиваем шаг для постепенного рисования
        generate_unique_fractal(screen, width, height, step)
        pygame.display.flip()
        pygame.time.delay(100)  # Задержка для визуализации
        step += 1