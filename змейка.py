import pygame
import time

pygame.init()

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Определение размеров экрана
width = 800
height = 600

# Создание экрана
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Змейка")

# Основной цикл программы
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Очистка экрана
    screen.fill(BLACK)

    # Обновление экрана
    pygame.display.flip()

    # Ограничение частоты обновления экрана
    clock.tick(60)

# Завершение программы
pygame.quit()