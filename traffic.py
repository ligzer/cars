import random

import pygame
from road import Road
from car import Car, CAR10, CAR13, CAR2, CAR3, CAR4

CARS = [CAR2, CAR3, CAR10, CAR13, CAR4]


class Traffic:
    def __init__(self, players):
        self.players = players
        self.cars = []
        self.road = Road(players)

    def draw(self, screen, dt):

        self.cars = [car for car in self.cars if car.pos.x > -1000 and car.pos.x < 3000]
        if len(self.cars) < 5 and random.random() > 0.99:
            if random.random() > 0.5:
                car = Car(
                    random.choice(CARS),
                    pygame.Vector2(random.randint(-900, -600), random.randint(0, 1000)),
                    random.randint(800, 1800))
            else:
                car = Car(
                    random.choice(CARS),
                    pygame.Vector2(random.randint(2000, 2900), random.randint(0, 1000)),
                    random.randint(0, 700))
            self.cars.append(car)
        for car in self.cars:
            car.turning += random.randint(-100, 100) * dt
        self.road.cars = self.players + self.cars

        self.road.draw(screen, dt)
