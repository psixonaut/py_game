import pygame
import random
import sqlite3

score = 0


class Game:
    def __init__(self):
        global score
        self.width = 800
        self.height = 800
        self.COLORS = [pygame.Color('red'), pygame.Color('green'), pygame.Color('black'), pygame.Color('white'),
                       pygame.Color('brown')]
        self.fps = pygame.time.Clock()
        self.over = False

    def start_game(self):
        pygame.init()

    def print_name(self):
        self.screen = pygame.display.set_mode((
            self.width, self.height))
        pygame.display.set_caption('Змейка')

    def update(self):
        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(20)

    def show_score(self, choice=1):
        score_font = pygame.font.SysFont('monaco', 24)
        score_surf = score_font.render(
            'Score: {0}'.format(score), True, self.COLORS[2])
        score_rect = score_surf.get_rect()
        if choice == 1:
            score_rect.midtop = (80, 10)
        else:
            score_rect.midtop = (360, 120)
        self.screen.blit(score_surf, score_rect)

    def game_over(self):
        self.screen.fill(self.COLORS[3])
        game_over_font = pygame.font.SysFont('monaco', 72)
        game_over_surf = game_over_font.render('Игра окончена', True, self.COLORS[0])
        game_over_rect = game_over_surf.get_rect()
        game_over_rect.midtop = (360, 15)
        self.screen.blit(game_over_surf, game_over_rect)
        self.show_score(0)
        pygame.display.flip()
        self.over = True



class Snake:
    def __init__(self, snake_color):
        self.snake_head = [100, 80]
        self.snake_body = [[100, 80], [90, 80], [80, 80]]
        self.snake_color = snake_color
        self.direction = "DOWN"
        self.new_directions = self.direction

    def check_direction_changes(self):
        if any((self.new_directions == "RIGHT" and not self.direction == "LEFT",
                self.new_directions == "LEFT" and not self.direction == "RIGHT",
                self.new_directions == "UP" and not self.direction == "DOWN",
                self.new_directions == "DOWN" and not self.direction == "UP")):
            self.direction = self.new_directions

    def change_position(self):
        if self.direction == "RIGHT":
            self.snake_head[0] += 10
        elif self.direction == "LEFT":
            self.snake_head[0] -= 10
        elif self.direction == "UP":
            self.snake_head[1] -= 10
        elif self.direction == "DOWN":
            self.snake_head[1] += 10

    def body_mechanism(self, score, food_pos, width, height):
        self.snake_body.insert(0, list(self.snake_head))
        if (self.snake_head[0] == food_pos[0] and
                self.snake_head[1] == food_pos[1]):
            food_pos = [random.randrange(30, width/10)*10 - 20,
                        random.randrange(30, height/10)*10 - 20]
            score += 1
        else:
            self.snake_body.pop()
        return score, food_pos

    def spawn_snake(self, screen, surface_color):
        screen.fill(surface_color)
        for pos in self.snake_body:
            pygame.draw.rect(
                screen, self.snake_color, pygame.Rect(
                    pos[0], pos[1], 10, 10))

    def collision_check(self, game_end, width, height):
        if any((
            self.snake_head[0] > width-10
            or self.snake_head[0] < 0,
            self.snake_head[1] > height-10
            or self.snake_head[1] < 0
                )):
            game_end()
        for square in self.snake_body[1:]:
            if (square[0] == self.snake_head[0] and square[1] == self.snake_head[1]):
                game_end()

class Food:
    def __init__(self, food_color, width, height):
        self.food_color = food_color
        self.food_x = 10
        self.food_y = 10
        self.food_pos = [random.randrange(30, width/10)*10 - 20,
                         random.randrange(30, height/10)*10 - 20]

    def spawn_food(self, screen):
        pygame.draw.rect(
            screen, self.food_color, pygame.Rect(
                self.food_pos[0], self.food_pos[1],
                self.food_x, self.food_y))


def start():
    global score
    score = 0
    game = Game()
    game.start_game()
    game.print_name()
    snake = Snake(game.COLORS[1])
    food = Food(game.COLORS[4], game.width, game.height)
    running = True
    while running:
        new_directions = snake.direction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    new_directions = "RIGHT"
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    new_directions = "LEFT"
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    new_directions = "UP"
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    new_directions = "DOWN"
        snake.new_directions = new_directions
        snake.check_direction_changes()
        snake.change_position()
        snake.collision_check(game.game_over, game.width, game.height)
        score, food.food_pos = snake.body_mechanism(score, food.food_pos, game.width, game.height)
        snake.spawn_snake(game.screen, game.COLORS[3])
        food.spawn_food(game.screen)
        snake.collision_check(game.game_over, game.width, game.height)
        game.show_score()
        if not game.over:
            game.update()
    pygame.quit()
