import pygame
from car import Car, CAR10, CAR13, CAR2, CAR3
from traffic import Traffic
from control import PlayerControl

pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0

pygame.mixer.music.load("media/soundtrack.mpga")
pygame.mixer.music.play(-1)
player1_pos = pygame.Vector2(screen.get_width() / 6, screen.get_height() / 2)
player2_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 4)
desired_car_height = 180

CAR10.prepare_images(desired_car_height)
CAR13.prepare_images(desired_car_height)
CAR2.prepare_images(desired_car_height)
CAR3.prepare_images(desired_car_height)

player1 = Car(CAR2, player1_pos)
player2 = Car(CAR3, player2_pos)

traffic = Traffic([player1, player2])
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    control1 = PlayerControl(player1, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
    control2 = PlayerControl(player2, pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        traffic.draw(screen, dt)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
        pygame.display.flip()
        dt = clock.tick(30) / 1000

        control1.control(dt, screen)
        control2.control(dt, screen)

    pygame.quit()