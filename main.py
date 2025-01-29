# main.py

import pygame
from fractal import draw_fractal

# Инициализация Pygame
pygame.init()

# Настройка дисплея
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Уникальная генерация фракталов")

# Главный цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана
    screen.fill((0, 0, 0))

    # Генерация и рисование уникального фрактала
    draw_fractal(screen, WIDTH, HEIGHT)

    # Обновление дисплея
    pygame.display.flip()

# Выход из Pygame
pygame.quit()