import pygame
from road import Road
from car import Car, CAR10, CAR13, CAR2, CAR3


class Traffic:
    def __init__(self, cars):
        car1 = Car(CAR10, pygame.Vector2(300, 200))
        car2 = Car(CAR13, pygame.Vector2(700, 600))
        self.road = Road(cars + [car1, car2])

    def draw(self, screen):
        self.road.draw(screen)
