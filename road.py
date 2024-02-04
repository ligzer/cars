import random

import pygame


class Road:
    def __init__(self, cars):
        self.rect = pygame.Rect(0, 0, 180, 10)
        self.speed = 720
        self.pos = pygame.Vector2(0, 0)
        self.cars = cars
        self.lamppost_pos = None
        self.lamppost = pygame.transform.scale(pygame.image.load(f"media/lamppost.png"),(250, 400))

    def draw(self, screen, dt):
        x = -300

        h = screen.get_height()
        w =screen.get_width()
        rect = pygame.Rect(0,0, 180, 10)
        self.pos.x -= self.speed * dt
        self.pos.x %= 300
        splitline = pygame.Rect(0, 0, 2000, 10)
        splitline.topleft = pygame.Vector2(0, 20)
        pygame.draw.rect(screen, "yellow", splitline)
        splitline.topleft = pygame.Vector2(0, 40)
        pygame.draw.rect(screen, "yellow", splitline)
        while x <= w:
            y = 240
            while y <= h:
                rect.x = x
                rect.y = y
                rect.bottomleft += self.pos
                pygame.draw.rect(screen, "white", rect)
                y += 200
            x += 300

        for car in sorted(self.cars, key=lambda car: car.pos.y):
            car.pos.x += (car.speed - self.speed)*dt
            car.pos.y += car.turning * dt
            car.draw(screen, dt)

        if self.lamppost_pos is None:
            if random.random() > 0.99:
                self.lamppost_pos = pygame.Vector2(3000,  screen.get_height() )
        else:
            self.lamppost_pos.x -= self.speed * dt
            rect = self.lamppost.get_rect()
            rect.midbottom = self.lamppost_pos
            screen.blit(self.lamppost, rect)
            if self.lamppost_pos.x < -300:
                self.lamppost_pos = None



