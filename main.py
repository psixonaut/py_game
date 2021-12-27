import pygame
import random

COLORS = [pygame.Color('black'), pygame.Color('white'), pygame.Color('blue')]


class Snake:
    def __init__(self, screen, width, height):
        x = width // 2
        y = height // 2
        pygame.draw.rect(screen, COLORS[2], [x, y, 10, 10])

    def spawn_snake(self, screen, width, height):
        x = width // 2
        y = height // 2
        pygame.draw.rect(screen, COLORS[2], [x, y, 10, 10])


def main():
    pygame.init()
    size = width, height = 600, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Змейка')
    snake = Snake(screen, width, height)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(COLORS[0])
        snake.spawn_snake(screen, width, height)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
