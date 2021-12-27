import pygame
import random

clock = pygame.time.Clock()
fps = 30
COLORS = [pygame.Color('black'), pygame.Color('white'), pygame.Color('blue')]
size = width, height = 600, 600
x0 = 0
y0 = 0


class Snake:
    def __init__(self, screen, width, height):
        x = width // 2
        y = height // 2
        pygame.draw.rect(screen, COLORS[2], [x, y, 10, 10])

    def spawn_snake(self, screen, width, height):
        x = width // 2
        y = height // 2
        pygame.draw.rect(screen, COLORS[2], [x, y, 10, 10])
        return x, y

    def snake_move(self, screen, x1, y1):
        pygame.draw.rect(screen, COLORS[2], [x1, y1, 10, 10])


def move(movement, screen, x, y):
    global height, width
    if movement == 'up' and x != height:
        Snake.snake_move(screen, screen, x + 3, y)
    elif movement == 'down' and x > 0:
        Snake.snake_move(screen, x - 3, y)
    elif movement == 'right' and y != width:
        Snake.snake_move(screen, screen, x, y + 3)
    elif movement == 'left' and y > 0:
        Snake.snake_move(screen, screen, x, y - 3)


def main():
    global x0, y0
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Змейка')
    snake = Snake(screen, width, height)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move("up", screen, x0, y0)
                    x0 += 3
                elif event.key == pygame.K_DOWN:
                    move("down", screen, x0, y0)
                    x0 -= 3
                elif event.key == pygame.K_LEFT:
                    move("left", screen, x0, y0)
                    y0 += 3
                elif event.key == pygame.K_RIGHT:
                    move("right", screen, x0, y0)
                    y0 -= 3
        screen.fill(COLORS[0])
        x0, y0 = snake.spawn_snake(screen, width, height)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


if __name__ == '__main__':
    main()
