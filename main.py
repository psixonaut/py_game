import pygame
import random

COLORS = [pygame.Color('black'), pygame.Color('white'), pygame.Color('blue')]

class Snake:
    pass

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
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Инициализация игры')
    board = Field(20, 20)
    board.set_view(5, 5, 25)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(COLORS[0])
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()
