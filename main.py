import random
import sys
import pygame
import os
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QDialog
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
import pygame
from PyQt5.uic import loadUi
from copy import deepcopy
from random import choice

W, H = 20, 20
TILE = 20
GAME_RES = W * TILE, H * TILE
FPS = 60
colors = [(155, 93, 229), (241, 91, 181), (254, 228, 64), (0, 187, 249), (0, 245, 212)]


class Game_tetris():
    def __init__(self):
        pygame.init()
        self.game_init()

    def game_init(self):
        # Установка позиции окна Pygame относительно верхнего левого угла экрана
        position = (200, 200)
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (position)

        size = width, height = 200, 200

        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption('Тетрис')
        self.screen.fill((0, 0, 255))
        self.radius = 0
        self.change_radius = pygame.USEREVENT + 1
        self.clock = pygame.time.Clock()
        self.flag_circle_exists = False
        self.circle_size = []
        pygame.time.set_timer(self.change_radius, 10)
        self.color_constant = colors[random.randint(0, 4)]

    def general_game_cycle(self, window):
        pygame.init()
        # game_sc = pygame.Surface(GAME_RES)
        game_sc = pygame.display.set_mode(GAME_RES)
        clock = pygame.time.Clock()

        grid = [pygame.Rect(x * TILE, y * TILE, TILE, TILE) for x in range(W) for y in range(H)]

        figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
                       [(0, -1), (-1, -1), (-1, 0), (0, 0)],
                       [(-1, 0), (-1, 1), (0, 0), (0, -1)],
                       [(0, 0), (-1, 0), (0, 1), (-1, -1)],
                       [(0, 0), (0, -1), (0, 1), (-1, -1)],
                       [(0, 0), (0, -1), (0, 1), (1, -1)],
                       [(0, 0), (0, -1), (0, 1), (-1, 0)]]

        figures = [[pygame.Rect(x + W // 2, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]
        figure_rect = pygame.Rect(0, 0, TILE - 2, TILE - 2)
        field = [[0 for i in range(W)] for j in range(H)]

        anim_count, anim_speed, anim_limit = 0, 60, 2000
        figure = deepcopy(choice(figures))

        def check_borders():

            if figure[i].x < 0 or figure[i].x > W - 1:
                return False
            elif figure[i].y > H - 1 or field[figure[i].y][figure[i].x]:
                return False
            return True

        while True:
            dx, rotate = 0, False
            game_sc.fill(pygame.Color('black'))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        dx = -1
                    elif event.key == pygame.K_RIGHT:
                        dx = 1
                    elif event.key == pygame.K_DOWN:
                        anim_limit = 100
                    elif event.key == pygame.K_UP:
                        rotate = True
            # move x
            figure_old = deepcopy(figure)
            for i in range(4):
                figure[i].x += dx
                if not check_borders():
                    figure = deepcopy(figure_old)
                    break
            # move y
            anim_count += anim_speed
            if anim_count > anim_limit:
                anim_count = 0
                figure_old = deepcopy(figure)
                for i in range(4):
                    figure[i].y += 1
                    if not check_borders():
                        for j in range(4):
                            field[figure_old[j].y][figure_old[j].x] = pygame.Color(self.color_constant)
                        figure = deepcopy(choice(figures))
                        anim_limit = 2000
                        break
            # rotate
            center = figure[0]
            figure_old = deepcopy(figure)
            if rotate:
                for i in range(4):
                    x = figure[i].y - center.y
                    y = figure[i].x - center.x
                    figure[i].x = center.x - x
                    figure[i].y = center.y + y
                    if not check_borders():
                        figure = deepcopy(figure_old)
                        break
            # check lines
            line = H - 1
            for row in range(H - 1, -1, -1):
                count = 0
                for i in range(W):
                    if field[row][i]:
                        count += 1
                    field[line][i] = field[row][i]
                if count < W:
                    line -= 1
            # draw grid
            [pygame.draw.rect(game_sc, (40, 40, 40), i_rect, 1) for i_rect in grid]
            # draw figure
            for i in range(4):
                figure_rect.x = figure[i].x * TILE
                figure_rect.y = figure[i].y * TILE
                pygame.draw.rect(game_sc, pygame.Color(self.color_constant), figure_rect)
            # draw field
            for y, raw in enumerate(field):
                for x, col in enumerate(raw):
                    if col:
                        figure_rect.x, figure_rect.y = x * TILE, y * TILE
                        pygame.draw.rect(game_sc, col, figure_rect)
            pygame.display.flip()
            clock.tick(FPS)


fps = 20
width = 400
height = 400
pygame.display.set_caption('Змейка')
screen = pygame.display.set_mode([width, height])
clock = pygame.time.Clock()
COLORS = [pygame.Color('white'), pygame.Color('red'), pygame.Color('green')]
pygame.display.set_caption('nake Game')


class Game_snake():
    def __init__(self, snake_type):
        pygame.init()
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
        self.food_pos = [random.randint(10, width / 10) * 10,
                         random.randint(10, height / 10) * 10]

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
    snake = Game_snake(COLORS[2])
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



class Greet_Window(QDialog):
    def __init__(self):
        super(Greet_Window, self).__init__()
        self.initUI()

    def initUI(self):
        loadUi('main_menu.ui', self)
        #self.setGeometry(400, 400, 800, 600)
       # self.setWindowTitle('PyMiniGames')
        self.pushButton.clicked.connect(self.to_menu)
        self.show()


    def to_menu(self):
        # переход во второе окно
        menu = Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, menu)
        widg.setCurrentIndex(index)

class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        loadUi('menu_2.ui', self)
        #self.setGeometry(400, 400, 800, 600)
       # self.setWindowTitle('PyMiniGames')

        self.pushButton.clicked.connect(self.to_tet_game)
        self.pushButton_2.clicked.connect(self.to_snake_game)
        self.pushButton_3.clicked.connect(self.back)
        self.show()

    def back(self):
        back = Greet_Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, back)
        widg.setCurrentIndex(index)

    def to_tet_game(self):
        background = Background()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, background)
        widg.setCurrentIndex(index)

    def to_snake_game(self):
        background1 = Background1()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, background1)
        widg.setCurrentIndex(index)

class Background(QDialog):
    def __init__(self):
        super(Background, self).__init__()
        self.initUI()

    def initUI(self):
        loadUi('game_background.ui', self)
        self.pushButton.clicked.connect(self.openGame)
        self.pushButton_2.clicked.connect(self.to_stop)
        self.pushButton_3.clicked.connect(self.to_menu)
        self.show()

    def init_pygame(self):

        self.game = Game_tetris()
        self.timer = QTimer()
        self.timer.timeout.connect(self.pygame_loop)
        self.timer.start(10)

    def pygame_loop(self):
        if self.game.general_game_cycle(self):
            self.timer.stop()
            self.timer.disconnect()
            pygame.quit()

    def to_menu(self):
        menu = Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, menu)
        widg.setCurrentIndex(index)

    def to_stop(self):
        self.timer.stop()
        self.timer.disconnect()
        pygame.quit()

    def openGame(self):
        self.init_pygame()

class Background1(QDialog):
    def __init__(self):
        super(Background1, self).__init__()
        self.initUI()

    def initUI(self):
        loadUi('game_background.ui', self)
        self.pushButton.clicked.connect(self.openGame)
        self.pushButton_2.clicked.connect(self.to_stop)
        self.pushButton_3.clicked.connect(self.to_menu)
        self.show()

    def init_pygame(self):
        print('i')
        self.game = Game_snake()
        self.timer = QTimer()
        self.timer.timeout.connect(self.pygame_loop)
        self.timer.start(10)

    def pygame_loop(self):
        if self.game.main(self):
            self.timer.stop()
            self.timer.disconnect()
            pygame.quit()

    def to_menu(self):
        menu = Window()
        index = widg.currentIndex() + 1
        widg.insertWidget(index, menu)
        widg.setCurrentIndex(index)

    def to_stop(self):
        self.timer.stop()
        self.timer.disconnect()
        pygame.quit()
    def openGame(self):
        self.init_pygame()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    grt_wnd = Greet_Window()
    wnd = Window()
    # bcg = Background()
    # bcg1 = Background1()
    widg = QtWidgets.QStackedWidget()
    widg.addWidget(grt_wnd)
    widg.addWidget(wnd)
    # widg.addWidget(bcg)
    # widg.addWidget(bcg1)
    widg.setFixedWidth(1920)
    widg.setFixedHeight(1000)
    widg.show()
    result = app.exec_()
    sys.exit(result)
