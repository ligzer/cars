import pygame


class PlayerControl:
    def __init__(self, car, up, down, left, right):
        self.car = car
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    def control(self, dt, screen):
        keys = pygame.key.get_pressed()
        LIMIT = 600

        if keys[self.left]  and keys[self.right]:
            self.car.turning = 0
        elif keys[self.left] and self.car.pos.y >= -LIMIT:
            self.car.turning = -600
        elif keys[self.right] and self.car.pos.y <= screen.get_height() + LIMIT:
            self.car.turning = 600
        else:
            self.car.turning = 0

        if keys[self.up] and keys[self.down]:
            self.car.speed = 720
        elif keys[self.up] and self.car.pos.y <= screen.get_width() + LIMIT:
            self.car.speed = 1200
        elif keys[self.down] and self.car.pos.y >= - LIMIT:
            self.car.speed = 300
        else:
            self.car.speed = 720

