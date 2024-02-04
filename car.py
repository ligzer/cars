import random
from pygame import Vector2
import pygame


class CarConfig:
    def __init__(self, img: str, wheels: list[Vector2]):
        self.img = img
        self.wheel_vectors = wheels
        self.wheels = []
        self.scale = 1.
        self.car_rect = None
        self.car_image = None
        self.prepared = False

    def prepare_images(self, desired_car_height):
        if self.prepared:
            raise Exception("Already prepared")
        image = pygame.image.load(f"media/{self.img}.png")
        self.scale = desired_car_height / image.get_height()
        desired_car_width = image.get_width() * self.scale
        self.car_image = pygame.transform.scale(image, (desired_car_width, desired_car_height))
        self.car_rect = self.car_image.get_rect()

        self.wheels = []
        for i in range(len(self.wheel_vectors)):
            img = pygame.image.load(f"media/{self.img}-wheel-{i}.png")
            scaled_img = pygame.transform.scale(img, (img.get_width() * self.scale, img.get_height() * self.scale,))
            self.wheels.append(scaled_img)

        self.prepared = True


CAR2 = CarConfig('car2', [Vector2(240, 0), Vector2(120, 0),])
CAR3 = CarConfig('car3', [Vector2(240, 0), Vector2(140, -10),])
CAR4 = CarConfig('car4', [Vector2(378, -18), Vector2(230, -14), Vector2(95, -13),])
CAR13 = CarConfig('car13', [Vector2(340, -10), Vector2(220, -10),])
CAR10 = CarConfig('car10', [ Vector2(270, 0), Vector2(120, 0),])


class Car:

    def __init__(self, car_config, pos, speed=1720):
        self.car_config = car_config
        self.wheel_rotates = [0] * len(car_config.wheels)
        self.speed = speed
        self.turning = 0
        self.pos = pos
        self.delta = Vector2(random.randint(-10, 10), random.randint(-10, 10))

    def draw(self, screen, dt):
        self.delta = self.delta.rotate(random.randint(3, 10))
        self.car_config.car_rect.center = self.pos - self.delta

        self.delta = self.delta.rotate(random.randint(3, 10))
        screen.blit(self.car_config.car_image, self.car_config.car_rect)

        for i in range(len(self.wheel_rotates)):
            self.wheel_rotates[i] -= self.speed * dt
            rotated_wheel = pygame.transform.rotate(self.car_config.wheels[i], self.wheel_rotates[i])
            wheel_rect = rotated_wheel.get_rect()
            wheel_rect.center = self.car_config.car_rect.bottomleft + self.car_config.wheel_vectors[i] + self.delta
            screen.blit(rotated_wheel, wheel_rect)
