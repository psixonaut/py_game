import pygame
import random

COLORS = [pygame.Color('black'), pygame.Color('white'), pygame.Color('blue')]


class Snake:
    def __init__(self, screen, width, height, tile_size):
        x = round(width / 2) * int(tile_size) - int(tile_size)
        y = round(height / 2) * int(tile_size) - int(tile_size)
        pygame.draw.rect(screen, COLORS[2], [x, y, int(tile_size), int(tile_size)])

    def spawn_snake(self, screen, width, height, tile_size):
        x = round(width / 2) * int(tile_size) - int(tile_size)
        y = round(height / 2) * int(tile_size) - int(tile_size)
        pygame.draw.rect(screen, COLORS[2], [x, y, int(tile_size), int(tile_size)])


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, COLORS[1],
                                 (x * self.cell_size + self.left, y * self.cell_size + self.top,
                                 self.cell_size, self.cell_size), 1)


def main():
    pygame.init()
    size = width, height = 600, 600
    width_tiles = 3
    height_tiles = 3
    cell_size = 50
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Инициализация игры')
    board = Field(width_tiles, height_tiles)
    board.set_view(0, 0, cell_size)
    snake = Snake(screen, width_tiles, height_tiles, cell_size)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(COLORS[0])
        board.render(screen)
        snake.spawn_snake(screen, width_tiles, height_tiles, cell_size)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
