import pygame
import random

pygame.init()
fps = 20
width = 400
height = 400
pygame.display.set_caption('Змейка')
screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
COLORS = [pygame.Color('white'), pygame.Color('red'), pygame.Color('green')]
pygame.display.set_caption('Snake Game')


class Snake:
    def __init__(self, snake_type):
        self.snake_head = [100, 100]
        self.snake_body = [[100, 100], [90, 100], [80, 100]]
        self.snake_type = snake_type
        self.move = 'right'
        self.direction = self.move

    def check_direction_change(self):
        if any((self.direction == "RIGHT" and not self.direction == "LEFT",
                self.direction == "LEFT" and not self.direction == "RIGHT",
                self.direction == "UP" and not self.direction == "DOWN",
                self.direction == "DOWN" and not self.direction == "UP")):
            self.move = self.direction

    def head_direction(self):
        if self.move == "RIGHT":
            self.snake_head[0] += 10
        elif self.move == "LEFT":
            self.snake_head[0] -= 10
        elif self.move == "UP":
            self.snake_head[1] -= 10
        elif self.move == "DOWN":
            self.snake_head[1] += 10

    def snake_mechanism(self, score, food_pos, width, height):
        self.snake_body.insert(0, list(self.snake_head))
        if (self.snake_head[0] == food_pos[0] and
                self.snake_head[1] == food_pos[1]):
            food_pos = [random.randrange(1, width / 10) * 10,
                        random.randrange(1, height / 10) * 10]
            score += 1
        else:
            self.snake_body.pop()
        return score, food_pos

    def spawn_snake(self, play_field, field_color):
        play_field.fill(field_color)
        for position in self.snake_body:
            pygame.draw.rect(play_field, COLORS[2], pygame.Rect(position[0], position[1], 10, 10))

    def collision_check(self, width, height):
        if any((
                self.snake_head[0] > width - 10
                or self.snake_head[0] < 0,
                self.snake_head[1] > height - 10
                or self.snake_head[1] < 0
        )):
            pygame.quit()
        for block in self.snake_body[1:]:
            if (block[0] == self.snake_head[0] and
                    block[1] == self.snake_head[1]):
                pygame.quit()


class Food():
    def __init__(self, food_type, width, height):
        self.food_type = food_type
        self.food_x = 10
        self.food_y = 10
        self.food_pos = [random.randint(10, width/10)*10,
                         random.randint(10, height/10)*10]

    def spawn_food(self, play_field):
        pygame.draw.rect(
            play_field, self.food_type, pygame.Rect(
                self.food_pos[0], self.food_pos[1],
                self.food_x, self.food_y))


def main():
    running = True
    pygame.display.set_caption('Змейка')
    pygame.init()
    score = 0
    snake = Snake(COLORS[2])
    food = Food(COLORS[1], width, height)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direction = "RIGHT"
                    snake.check_direction_change()
                    snake.head_direction()
                    score, food.food_pos = snake.snake_mechanism(score, food.food_pos, width, height)
                elif event.key == pygame.K_LEFT:
                    direction = "LEFT"
                    snake.check_direction_change()
                    snake.head_direction()
                    score, food.food_pos = snake.snake_mechanism(score, food.food_pos, width, height)
                elif event.key == pygame.K_UP:
                    direction = "UP"
                    snake.check_direction_change()
                    snake.head_direction()
                    score, food.food_pos = snake.snake_mechanism(score, food.food_pos, width, height)
                elif event.key == pygame.K_DOWN:
                    direction = "DOWN"
                    snake.check_direction_change()
                    snake.head_direction()
                    score, food.food_pos = snake.snake_mechanism(score, food.food_pos, width, height)
        screen.fill(COLORS[0])
        food.spawn_food(screen)
        snake.spawn_snake(screen, COLORS[0])
        snake.collision_check(width, height)
        clock.tick(fps)
        pygame.display.flip()


if __name__ == '__main__':
    main()
