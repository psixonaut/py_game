import pygame
import random

full_screen = width, height = 800, 600
FPS = 60
platform_width, platform_height = 300, 25
platform_speed = 15
x = width // 2 - platform_width // 2
y = height - platform_height - 10
x1 = platform_width
y1 = platform_height
platform_rect = pygame.Rect(x, y, x1, y1)

radius_circle = 15
ball_speed = 6
center = int(15 * 2 ** 0.5)
coord = (random.randrange(center, width - center))
center_screen = height // 2
circle = coord, center_screen
ball = pygame.Rect(coord, center_screen, center, center)
dx, dy = 1, -1

color = [(155, 93, 229), (241, 91, 181), (254, 228, 64), (0, 187, 249), (0, 245, 212)]

block_list_1 = []
block_list = []
for i in range(10):
    for j in range(5):
        block_list.append((10 + 79 * i, 5 + 50 * j, 69, 30))
        block_list_1.append(pygame.Rect(10 + 79 * i, 5 + 50 * j, 69, 30))

color_list = []
for i in range(50):
    color_list.append(random.choice(color))


def clash(dx, dy, circle, rect):
    if dx > 0:
        delta_x = circle[0] + center - rect[0]
    else:
        delta_x = (rect[0] + rect[2]) - circle[0]
    if dy > 0:
        delta_y = circle[1] + center - rect[1]
    else:
        delta_y = circle[1] - (rect[1] + rect[3])

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

pygame.init()
sc = pygame.display.set_mode(full_screen)
clock = pygame.time.Clock()
pygame.display.set_caption('Arkanoid')
sc.fill(pygame.Color(10, 10, 10))

running = True
while running:
    ball = pygame.Rect(coord, center_screen, center, center)
    platform_rect = pygame.Rect(x, y, x1, y1)
    sc.fill(pygame.Color(10, 10, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if circle[0] <= radius_circle or circle[0] > width - radius_circle:
        dx = -dx
    if circle[1] <= radius_circle:
        dy = -dy

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and x > 0:
        x -= platform_speed
    if key[pygame.K_RIGHT] and x < width - 300:
        x += platform_speed
    count = 0
    for i in block_list:
        pygame.draw.rect(sc, color_list[count], i)
        count += 1

    pygame.draw.rect(sc, pygame.Color(0, 187, 249),
                     (x, y, x1, y1))
    pygame.draw.circle(sc, pygame.Color(254, 228, 64), circle, radius_circle, 0)

    coord += ball_speed * dx
    center_screen += ball_speed * dy
    circle = coord, center_screen
    if ball.colliderect(platform_rect) and dy > 0:
        dx, dy = clash(dx, dy, ball, (x, y, x1, y1))

    hit_index = ball.collidelist(block_list_1)
    if hit_index != -1:
        hit_rect = block_list.pop(hit_index)
        color_list.pop(hit_index)
        block_list_1.pop(hit_index)
        dx, dy = clash(dx, dy, circle, hit_rect)
        FPS += 1
    if circle[1] + center > height:
        sc.fill(pygame.Color(10, 10, 10))
        fon = pygame.font.Font(None, 100)
        over = fon.render('GAME OVER!', True, pygame.Color('red'))
        sc.blit(over, (180, 250))
    elif not len(block_list):
        sc.fill(pygame.Color(10, 10, 10))
        fon = pygame.font.Font(None, 100)
        vin = fon.render('VICTORY!', True, pygame.Color('BLUE'))
        sc.blit(vin, (240, 250))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
