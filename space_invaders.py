import pygame


class Alien:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
        self.size = 30

    def spawn(self, speed_up_coef):
        pygame.draw.rect(self.game.screen, (pygame.Color((155, 93, 229))), pygame.Rect(self.x, self.y, self.size, self.size))
        self.y += speed_up_coef

    def check_for_collision(self, game):
        for laser in game.rockets:
            if (laser.x < self.x + self.size and
                laser.x > self.x - self.size and
                laser.y < self.y + self.size and
                laser.y > self.y - self.size):
                game.rockets.remove(laser)
                game.aliens.remove(self)


class Hero:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y

    def spawn(self):
        pygame.draw.rect(self.game.screen, (pygame.Color((0, 187, 249))), pygame.Rect(self.x, self.y, 8, 5))


class Generator:
    def __init__(self, game):
        border_x = 30
        border_y = 50
        for x in range(border_x, game.width - border_x, border_y):
            for y in range(border_x, int(game.height / 2), border_y):
                game.aliens.append(Alien(game, x, y))


class Rocket:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game

    def spawn(self):
        pygame.draw.rect(self.game.screen, (pygame.Color((241, 91, 181))), pygame.Rect(self.x, self.y, 2, 4))
        self.y -= 2


class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.aliens = []
        self.rockets = []
        self.lost = False
        self.COLORS = [pygame.Color((16, 20, 25)), pygame.Color((0, 187, 249)),
              pygame.Color((155, 93, 229)), pygame.Color(241, 91, 181)]
        self.screen = pygame.display.set_mode((width, height))

    def write_text(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('Monaco', 50)
        textsurface = font.render(text, True, (self.COLORS[1]))
        self.screen.blit(textsurface, (320, 160))


def start():
    game = Game(800, 800)
    pygame.init()
    pygame.mixer.music.load('space_invaders.mp3')
    pygame.mixer.music.play()

    pygame.display.set_caption('Космические захватчики')
    clock = pygame.time.Clock()
    running = True

    hero = Hero(game, game.width / 2, game.height - 20)
    generator = Generator(game)
    rocket = None

    while running:
        if len(game.aliens) == 0:
            game.write_text("ПОБЕДА")

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            hero.x -= 2 if hero.x > 20 else 0
        elif pressed[pygame.K_RIGHT]:
            hero.x += 2 if hero.x < game.width - 20 else 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game.lost:
                game.rockets.append(Rocket(game, hero.x, hero.y))

        pygame.display.flip()
        clock.tick(60)
        game.screen.fill(game.COLORS[0])

        for inwader in game.aliens:
            inwader.spawn(0.4)
            inwader.check_for_collision(game)
            if (inwader.y > game.height):
                game.lost = True
                game.write_text("ПОРАЖЕНИЕ")

        for laser in game.rockets:
            laser.spawn()

        if not game.lost:
            hero.spawn()
    pygame.quit()


