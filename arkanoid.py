import pygame
import random


# Определение направления
def clash(move_x, move_y, circle, rect, center):
    if move_x > 0:
        dx = circle[0] + center - rect[0]
    else:
        dx = (rect[0] + rect[2]) - circle[0]
    if move_y > 0:
        dy = circle[1] + center - rect[1]
    else:
        dy = circle[1] - (rect[1] + rect[3])
    if abs(dx - dy) < 10:
        move_x = -move_x
        move_y = -move_y
    elif dx > dy:
        move_y = -move_y
    elif dy > dx:
        move_x = -move_x
    return move_x, move_y


# Игра
def start():
    # Основные настройки
    full_screen = width, height = 800, 600
    FPS = 60

    # Настройки платформы
    platform_width, platform_height = 300, 25
    platform_speed = 15
    x = width // 2 - platform_width // 2
    y = height - platform_height - 10
    x1 = platform_width
    y1 = platform_height
    platform_rect = pygame.Rect(x, y, x1, y1)

    # Настройки шарика
    radius_circle = 15
    ball_speed = 6
    center = int(15 * 2 ** 0.5)
    coord = (random.randrange(center, width - center))
    center_screen = height // 2
    circle = coord, center_screen
    ball = pygame.Rect(coord, center_screen, center, center)
    move_x, move_y = 1, -1

    # Цвета
    color = [(155, 93, 229), (241, 91, 181), (254, 228, 64), (0, 187, 249), (0, 245, 212)]

    # Списки
    block_list_1 = []
    block_list = []
    # Генерация прямоугольников
    for i in range(10):
        for j in range(5):
            block_list.append((10 + 79 * i, 20 + 50 * j, 69, 30))
            block_list_1.append(pygame.Rect(10 + 79 * i, 20 + 50 * j, 69, 30))

    color_list = []
    for i in range(50):
        color_list.append(random.choice(color))

    pygame.init()
    pygame.mixer.music.load('arcanoid.mp3')
    pygame.mixer.music.play()
    sc = pygame.display.set_mode(full_screen)
    clock = pygame.time.Clock()
    pygame.display.set_caption('Арканоид')
    sc.fill(pygame.Color(10, 10, 10))
    count_game = 0
    # Цикл игры
    running = True
    while running:
        ball = pygame.Rect(coord, center_screen, center, center)
        platform_rect = pygame.Rect(x, y, x1, y1)
        sc.fill(pygame.Color(10, 10, 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Направление полета
        if circle[0] <= radius_circle or circle[0] > width - radius_circle:
            move_x = -move_x
        if circle[1] <= radius_circle:
            move_y = -move_y

        # Перемешение платформы
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and x > 0:
            x -= platform_speed
        if key[pygame.K_RIGHT] and x < width - 300:
            x += platform_speed
        count = 0
        for i in block_list:
            pygame.draw.rect(sc, color_list[count], i)
            count += 1

        # Отрисовка
        pygame.draw.rect(sc, pygame.Color(0, 187, 249),
                         (x, y, x1, y1))
        pygame.draw.circle(sc, pygame.Color(254, 228, 64), circle, radius_circle, 0)

        coord += ball_speed * move_x
        center_screen += ball_speed * move_y
        circle = coord, center_screen
        if ball.colliderect(platform_rect) and move_y > 0:
            move_x, move_y = clash(move_x, move_y, ball, (x, y, x1, y1), center)

        # Столкновение
        index = ball.collidelist(block_list_1)
        if index != -1:
            hit_rect = block_list.pop(index)
            color_list.pop(index)
            block_list_1.pop(index)
            move_x, move_y = clash(move_x, move_y, circle, hit_rect, center)
            FPS += 1

        # Проверка на поражение
        if circle[1] + center > height and count_game == 0:
            sc.fill(pygame.Color(10, 10, 10))
            fon = pygame.font.Font(None, 100)
            over = fon.render('Поражение!', True, pygame.Color((47, 102, 144)))
            sc.blit(over, (200, 250))

        # Проверка на победу
        elif not len(block_list):
            sc.fill(pygame.Color(10, 10, 10))
            fon = pygame.font.Font(None, 100)
            vin = fon.render('Победа!', True, pygame.Color((47, 102, 144)))
            sc.blit(vin, (260, 250))
            count_game = 1
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

start()
