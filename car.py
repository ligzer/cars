import pygame


class Car:

    def __init__(self, img, desired_car_height, pos, rear, front):
        self.rear = rear
        self.front = front
        self.rear_rotate = 0
        self.front_rotate = 0
        self.image = pygame.image.load(f"media/{img}.png")
        self.scale = desired_car_height/self.image.get_height()
        desired_car_width = self.image.get_width() * self.scale
        self.image = pygame.transform.scale(self.image, (desired_car_width, desired_car_height))
        self.car_rect = self.image.get_rect()
        self.car_rect.center = pos


        self.rear_wheel = pygame.image.load(f"media/{img}-wheel-rear.png")
        self.rear_wheel = pygame.transform.scale(
            self.rear_wheel,
            (self.rear_wheel.get_width() * self.scale, self.rear_wheel.get_height() * self.scale,)
        )



        self.front_wheel = pygame.image.load(f"media/{img}-wheel-front.png")
        self.front_wheel = pygame.transform.scale(
            self.front_wheel,
            (self.front_wheel.get_width() * self.scale, self.front_wheel.get_height() * self.scale,)
        )


    def draw(self, screen):
        screen.blit(self.image, self.car_rect)
        self.rear_rotate -= 12
        self.front_rotate -= 11
        rotated_rear_wheel = pygame.transform.rotate(self.rear_wheel, self.rear_rotate)
        rear_rect = rotated_rear_wheel.get_rect()
        rear_rect.center = self.car_rect.bottomleft+self.rear
        screen.blit(rotated_rear_wheel, rear_rect)
        rotated_front_wheel = pygame.transform.rotate(self.front_wheel, self.rear_rotate)

        front_rect = rotated_front_wheel.get_rect()
        front_rect.center = self.car_rect.bottomleft+self.front
        screen.blit(rotated_front_wheel, front_rect)

