import pygame
import random

COLORS = [pygame.Color('black'), pygame.Color('white'), pygame.Color('blue')]
x = 0
y = 0
size = width, height = 600, 600


class Snake:
    def __init__(self, screen, width, height):
        global x, y
        x = width // 2
        y = height // 2
        pygame.draw.rect(screen, COLORS[2], [x, y, 10, 10])

    def spawn_snake(self, screen, width, height):
        global x, y
        x = width // 2
        y = height // 2
        pygame.draw.rect(screen, COLORS[2], [x, y, 10, 10])

    def snake_move(self, screen, x1, y1):
        global x, y
        x = x1
        y = y1
        pygame.draw.rect(screen, COLORS[2], [x1, y1, 10, 10])


def move(movement, screen):
    global height, x, y, width
    if movement == 'up' and x != height:
        Snake.snake_move(screen, screen, x + 3, y)
    elif movement == 'down' and x > 0:
        Snake.snake_move(screen, screen, x - 3, y)
    elif movement == 'right' and y != width:
        Snake.snake_move(screen, screen, x, y + 3)
    elif movement == 'left' and y != 0:
        Snake.snake_move(screen, screen, x, y - 3)


def main():
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Змейка')
    snake = Snake(screen, width, height)
    snake.spawn_snake(screen, width, height)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move("up", screen)
                elif event.key == pygame.K_DOWN:
                    move("down", screen)
                elif event.key == pygame.K_LEFT:
                    move("left", screen)
                elif event.key == pygame.K_RIGHT:
                    move("right", screen)
        screen.fill(COLORS[0])
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
