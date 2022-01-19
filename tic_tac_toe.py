import pygame
import random

pygame.init()

COL = [(155, 93, 229), (241, 91, 181), (0, 187, 249)]
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic tac toe')
scr = pygame.display.set_mode((600, 600))
scr.fill((0, 0, 0))
matric = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
flag = True
game_over = False
kolvo_hodov = 0

#рисовка поля
def field(scr):
    helper = 200
    pygame.draw.rect(scr, COL[0], (0, 0, 600, 600), 50)
    for i in range(2):
        pygame.draw.line(scr, COL[0], (helper, 0), (helper, 600), 25)
        pygame.draw.line(scr, COL[0], (0, helper), (600, helper), 25)
        helper += 200

#рисовка фигур
def figures(scr, items):
    for i in range(3):
        for j in range(3):
            if items[i][j] == 10:
                pygame.draw.circle(scr, (241, 91, 181), (j * 190 + 107, i * 190 + 107), 70, 20)
            elif items[i][j] == 1:
                pygame.draw.line(scr, (0, 187, 249), (j * 190 + 40, i * 190 + 40), (j * 190 + 175, i * 190 + 175), 25)
                pygame.draw.line(scr, (0, 187, 249), (j * 190 + 175, i * 190 + 40), (j * 190 + 40, i * 190 + 175), 25)

#проверка победы
def check(matric):
    global kolvo_hodov
    global game_over
    for i in range(3):
        # горизонтальная проверка
        if matric[0][i] + matric[1][i] + matric[2][i] == 30 or matric[0][i] + matric[1][i] + matric[2][i] == 3:
            if matric[0][i] + matric[1][i] + matric[2][i] == 30:
                end('o')
            elif matric[0][i] + matric[1][i] + matric[2][i] == 3:
                end('x')
            elif kolvo_hodov >= 8:
                end('xo')
            game_over = True
        # вертикальная проверка
        elif matric[i][0] + matric[i][1] + matric[i][2] == 30 or matric[i][0] + matric[i][1] + matric[i][2] == 3:
            if matric[i][0] + matric[i][1] + matric[i][2] == 30:
                end('o')
            elif matric[i][0] + matric[i][1] + matric[i][2] == 3:
                end('x')
            elif kolvo_hodov >= 8:
                end('xo')
            game_over = True
    #проверка наискосок
    if matric[0][0] + matric[1][1] + matric[2][2] == 30 or matric[0][0] + matric[1][1] + matric[2][2] == 3:
        if matric[0][0] + matric[1][1] + matric[2][2] == 30:
            end('o')
        elif matric[0][0] + matric[1][1] + matric[2][2] == 3:
            end('x')
        elif kolvo_hodov >= 8:
            end('xo')
        game_over = True
    elif matric[0][2] + matric[1][1] + matric[2][0] == 30 or matric[0][2] + matric[1][1] + matric[2][0] == 3:
        if matric[0][2] + matric[1][1] + matric[2][0] == 30:
            end('o')
        elif matric[0][2] + matric[1][1] + matric[2][0] == 3:
            end('x')
    elif sum(matric[0][:]) + sum(matric[1][:]) + sum(matric[2][:]) == 44:
        end('xo')
        game_over = True

#победный экран
def end(winner):
    global scr
    global game_over
    scr.fill('black')
    if winner == 'x':
        fon = pygame.font.Font(None, 100)
        res = fon.render('Победил', True, COL[0])
        scr.blit(res, (140, 100))
        pygame.draw.line(scr, (155, 93, 229), (200, 200), (400, 400), 25)
        pygame.draw.line(scr, (155, 93, 229), (400, 200), (200, 400), 25)
    elif winner == 'o':
        fon = pygame.font.Font(None, 100)
        res = fon.render('Победил', True, COL[0])
        scr.blit(res, (140, 100))
        pygame.draw.circle(scr, (155, 93, 229), (300, 300), 100, 20)
    elif winner == 'xo':
        fon = pygame.font.Font(None, 100)
        res = fon.render('Ничья', True, COL[0])
        scr.blit(res, (140, 100))
#основной цикл
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            coords = pygame.mouse.get_pos()
            if matric[coords[1] // 200][coords[0] // 200] == 0:
                matric[coords[1] // 200][coords[0] // 200] = 1
                kolvo_hodov += 1
                i, j = random.randint(0, 2), random.randint(0, 2)
                while matric[i][j] != 0:
                    i, j = random.randint(0, 2), random.randint(0, 2)
                matric[i][j] = 10
                kolvo_hodov += 1
            check(matric)
    if game_over is False:
        field(scr)
        figures(scr, matric)
    window.blit(scr, (0, 0))
    pygame.display.update()
pygame.quit()

