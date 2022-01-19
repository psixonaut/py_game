import pygame


class Game:
    screen = None
    aliens = []
    rockets = []
    lost = False
    colors = [pygame.Color('black'), pygame.Color('white'), pygame.Color('green'), pygame.Color('red')]

    def __init__(self, width, height):
        pygame.init()
        self.width = height
        self.height = width
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        running = True

        hero = Hero(self, width / 2, height - 20)
        generator = Generator(self)
        rocket = None

        while running:
            if len(self.aliens) == 0:
                self.write_text("VICTORY")

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                hero.x -= 2 if hero.x > 20 else 0
            elif pressed[pygame.K_RIGHT]:
                hero.x += 2 if hero.x < width - 20 else 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                    self.rockets.append(Rocket(self, hero.x, hero.y))

            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill(Game.colors[0])

            for inwader in self.aliens:
                inwader.spawn(0.2)
                inwader.check_for_collision(self)
                if (inwader.y > height):
                    self.lost = True
                    self.write_text("DEFEAT")

            for laser in self.rockets:
                laser.spawn()

            if not self.lost:
                hero.spawn()

    def write_text(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('Monaco', 50)
        textsurface = font.render(text, True, (Game.colors[1]))
        self.screen.blit(textsurface, (110, 160))


class Alien:
    def __init__(self, game, x, y):
        self.x = x
        self.game = game
        self.y = y
        self.size = 30

    def spawn(self, speed_up_coef):
        pygame.draw.rect(self.game.screen, (Game.colors[2]), pygame.Rect(self.x, self.y, self.size, self.size))
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
        pygame.draw.rect(self.game.screen, (Game.colors[1]), pygame.Rect(self.x, self.y, 8, 5))


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
        pygame.draw.rect(self.game.screen, (Game.colors[3]), pygame.Rect(self.x, self.y, 2, 4))
        self.y -= 2


Game(800, 800)
