import pygame
from random import choice
from copy import deepcopy
import sqlite3


# Функция проверки поля
def border_check(figure, matrix, i, w, h):
    if (figure[i])[0] < 0 or (figure[i])[0] > w - 1:
        return False
    elif (figure[i])[1] > h - 1 or matrix[(figure[i])[1]][(figure[i])[0]]:
        return False
    return True


# Получение рекорда
def get_records():
    with open('name_for_profile') as s:
        login = s.readline()
    if login == '0':
        return 0
    else:
        bd = sqlite3.connect("our_users_1.sqlite")
        cur = bd.cursor()
        tet_res = cur.execute(f"""SELECT tetris_score FROM users_info WHERE name = '{login}'""").fetchone()
        bd.close()
        return tet_res[0]


# Запись рекорда
def set_records(record, score):
    this_record = max(int(record), score)
    with open('name_for_profile') as s:
        login = s.readline()
    if login != '0':
        bd = sqlite3.connect("our_users_1.sqlite")
        cur = bd.cursor()
        cur.execute(f"""UPDATE users_info SET tetris_score = {this_record} WHERE name = '{login}'""")
        bd.commit()


# Выбор цвета
def choice_color(color, color_list):
    color_count = color
    color = choice(color_list)
    while color == color_count:
        color = choice(color_list)
    return color


def start():
    # Размеры
    w = 10
    h = 20
    cell_size = 30
    FPS = 60
    full_screen = 600, 640
    size = width, height = w * cell_size, h * cell_size

    pygame.init()
    pygame.mixer.music.load('tetris.mp3')
    pygame.mixer.music.play()
    sc = pygame.display.set_mode(full_screen)
    screen = pygame.Surface(size)
    pygame.display.set_caption('Тетрис')
    sc.fill(pygame.Color(10, 10, 10))

    clock = pygame.time.Clock()
    # Надписи
    fon_glav = pygame.font.Font(None, 100)
    fon = pygame.font.Font(None, 45)

    name_tetris = fon_glav.render('TETRIS', True, pygame.Color((84, 153, 210)))
    name_score = fon.render('score:', True, pygame.Color((47, 102, 144)))
    name_record = fon.render('record:', True, pygame.Color((47, 102, 144)))
    # Очки
    score = 0
    count_lines = 0
    scores = {0: 0, 1: 100, 2: 300, 3: 700, 4: 1500}

    count_speed = 0
    speed = 60
    limit = 2000
    # Списки
    list_1 = []
    figures = []
    # Матрица поля
    matrix = [[0 for i in range(w)] for j in range(h)]
    # Позиция фигур при появлении
    figures_position = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
                        [(0, -1), (-1, -1), (-1, 0), (0, 0)],
                        [(-1, 0), (-1, 1), (0, 0), (0, -1)],
                        [(0, 0), (-1, 0), (0, 1), (-1, -1)],
                        [(0, 0), (0, -1), (0, 1), (-1, -1)],
                        [(0, 0), (0, -1), (0, 1), (1, -1)],
                        [(0, 0), (0, -1), (0, 1), (-1, 0)]]
    # Цвета
    color_list = [(155, 93, 229), (241, 91, 181), (254, 228, 64), (0, 187, 249), (0, 245, 212)]
    color = choice(color_list)
    # Генерация позиции фигур
    for i_1 in figures_position:
        for x, y in i_1:
            list_1.append([x + w // 2, y + 1, 1, 1])
        figures.append(list_1)
        list_1 = []
    # Сохранение фигур
    figure = deepcopy(choice(figures))
    figure_next = deepcopy(choice(figures))

    color = choice_color(color, color_list)
    next_color = choice_color(color, color_list)
    # Цикл игры
    running = True
    while running:
        sc.fill(pygame.Color(10, 10, 10))
        record = get_records()
        move = 0
        position = False
        sc.blit(screen, (20, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move = -1
                elif event.key == pygame.K_RIGHT:
                    move = 1
                elif event.key == pygame.K_DOWN:
                    limit = 100
                elif event.key == pygame.K_UP:
                    position = True

    # Перемещение по горизонтали
        old = deepcopy(figure)
        for i in range(4):
            (figure[i])[0] += move
            if not border_check(figure, matrix, i, w, h):
                figure = deepcopy(old)
                break

    # Перемещение по вертикали
        count_speed += speed
        if count_speed > limit:
            count_speed = 0
            old = deepcopy(figure)
            for i in range(4):
                (figure[i])[1] += 1
                if not border_check(figure, matrix, i, w, h):
                    for i in range(4):
                        matrix[(old[i])[1]][(old[i])[0]] = color
                    figure = figure_next
                    color = next_color
                    figure_next = deepcopy(choice(figures))
                    next_color = choice_color(color, color_list)
                    limit = 2000
                    break

    # Вращение фигур
        rotation = figure[0]
        old = deepcopy(figure)
        if position:
            for i in range(4):
                x = (figure[i])[1] - rotation[1]
                y = (figure[i])[0] - rotation[0]
                (figure[i])[0] = rotation[0] - x
                (figure[i])[1] = rotation[1] + y
                if not border_check(figure, matrix, i, w, h):
                    figure = deepcopy(old)
                    break

    # Проверка на собранную линию
        matrix_line = h - 1
        count_lines = 0
        for j_1 in range(h - 1, -1, -1):
            count = 0
            for i in range(w):
                if matrix[j_1][i]:
                    count += 1
                matrix[matrix_line][i] = matrix[j_1][i]
            if count < w:
                matrix_line -= 1
            else:
                speed += 3
                count_lines += 1

        score += scores[count_lines]
    # Отрисовка поля
        screen.fill(pygame.Color('black'))
        for y in range(h):
            for x in range(w):
                pygame.draw.rect(screen, pygame.Color(40, 40, 40),
                                 (x * cell_size, y * cell_size,
                                  cell_size, cell_size), 2)

    # Отрисовка фигур
        for i in range(4):
            pygame.draw.rect(screen, pygame.Color(color),
                             ((figure[i])[0] * cell_size, (figure[i])[1] * cell_size,
                              cell_size - 2, cell_size - 2))

    # Отрисовка изменений
        x = -1
        y = -1
        for i in matrix:
            x = -1
            y += 1
            for j in i:
                x += 1
                if j:
                    pygame.draw.rect(screen, j, (x * cell_size, y * cell_size,
                                                 cell_size - 2, cell_size - 2))
    # Отрисовка следующий фигуры
        for i in range(4):
            pygame.draw.rect(sc, pygame.Color(next_color),
                             ((figure_next[i])[0] * cell_size + 310, (figure_next[i])[1] * cell_size + 185,
                              cell_size - 2, cell_size - 2))
    # Отрисовка надписей
        sc.blit(name_tetris, (330, 20))
        sc.blit(name_score, (330, 100))
        sc.blit(fon.render(str(score), True, pygame.Color((163, 206, 241))), (440, 100))
        sc.blit(name_record, (330, 400))
        sc.blit(fon.render(str(record), True, pygame.Color((163, 206, 241))), (450, 400))

    # Поражение и перезапуск
        for i in range(w):
            if matrix[0][i]:
                set_records(record, score)
                matrix = [[0 for i in range(w)] for i in range(h)]
                count_speed = 0
                speed = 60
                limit = 2000
                score = 0
                for y in range(h):
                    for x in range(w):
                        pygame.draw.rect(screen, pygame.Color(40, 40, 40),
                                         (x * cell_size, y * cell_size,
                                          cell_size, cell_size))
                        sc.blit(screen, (20, 20))
                        pygame.display.flip()
                        clock.tick(200)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
