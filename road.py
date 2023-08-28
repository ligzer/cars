import pygame


class Road:
    def __init__(self, cars):
        self.rect = pygame.Rect(0,0, 180, 10)
        self.speed = 36
        self.pos = pygame.Vector2(0,0)
        self.cars = cars

    def draw(self, screen):
        x = -300

        h = screen.get_height()
        w =screen.get_width()
        rect = pygame.Rect(0,0, 180, 10)
        self.pos.x -= self.speed
        self.pos.x %= 300
        while x <= w:
            y = 200
            while y <= h:
                rect.x = x
                rect.y = y
                rect.bottomleft += self.pos
                pygame.draw.rect(screen, "white", rect)
                y += 200
            x += 300

        for car in sorted(self.cars, key=lambda x: x.pos.y):
            car.draw(screen)
