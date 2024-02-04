import random
import pygame


class CarConfig:
    def __init__(self, img, rear, front):
        self.img = img
        self.rear = rear
        self.front = front
        self.prepared = False

    def prepare_images(self, desired_car_height):
        if self.prepared:
            raise Exception("Already prepared")
        image = pygame.image.load(f"media/{self.img}.png")
        self.scale = desired_car_height / image.get_height()
        desired_car_width = image.get_width() * self.scale
        self.car_image = pygame.transform.scale(image, (desired_car_width, desired_car_height))
        self.car_rect = self.car_image.get_rect()

        self.rear_wheel = pygame.image.load(f"media/{self.img}-wheel-rear.png")
        self.rear_wheel = pygame.transform.scale(
            self.rear_wheel,
            (self.rear_wheel.get_width() * self.scale, self.rear_wheel.get_height() * self.scale,)
        )

        self.front_wheel = pygame.image.load(f"media/{self.img}-wheel-front.png")
        self.front_wheel = pygame.transform.scale(
            self.front_wheel,
            (self.front_wheel.get_width() * self.scale, self.front_wheel.get_height() * self.scale,)
        )
        self.prepared = True



CAR2 = CarConfig('car2', pygame.Vector2(120, 0), pygame.Vector2(240, 0))
CAR3 = CarConfig('car3', pygame.Vector2(140, -10), pygame.Vector2(240, 0))
CAR13 = CarConfig('car13', pygame.Vector2(220, -10), pygame.Vector2(340, -10))
CAR10 = CarConfig('car10', pygame.Vector2(120, 0), pygame.Vector2(270, 0))


class Car:

    def __init__(self, car_config, pos, speed=1720):
        self.car_config = car_config
        self.rear_rotate = 0
        self.front_rotate = 0
        self.speed = speed
        self.turning = 0
        self.pos = pos
        self.delta = pygame.Vector2(random.randint(-10, 10), random.randint(-10, 10))
        # self.delta = pygame.Vector2(0,0)


    def draw(self, screen, dt):
        self.delta = self.delta.rotate(random.randint(3, 10))
        self.car_config.car_rect.center = self.pos - self.delta

        self.delta = self.delta.rotate(random.randint(3, 10))
        screen.blit(self.car_config.car_image, self.car_config.car_rect)


        self.rear_rotate -= self.speed * dt
        self.front_rotate -= self.speed * dt

        rotated_rear_wheel = pygame.transform.rotate(self.car_config.rear_wheel, self.rear_rotate)
        rear_rect = rotated_rear_wheel.get_rect()
        rear_rect.center = self.car_config.car_rect.bottomleft + self.car_config.rear + self.delta
        screen.blit(rotated_rear_wheel, rear_rect)

        rotated_front_wheel = pygame.transform.rotate(self.car_config.front_wheel, self.front_rotate)
        front_rect = rotated_front_wheel.get_rect()
        front_rect.center = self.car_config.car_rect.bottomleft + self.car_config.front + self.delta
        screen.blit(rotated_front_wheel, front_rect)
