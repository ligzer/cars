import pygame
from car import Car, CAR10, CAR13, CAR2, CAR3
from traffic import Traffic
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
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        traffic.draw(screen)

        keys = pygame.key.get_pressed()
        LIMIT = 0
        if keys[pygame.K_ESCAPE]:
            running = False
        if keys[pygame.K_LEFT]:
            if player1.pos.y>= -LIMIT:
                player1.pos.y -= 600 * dt
        if keys[pygame.K_RIGHT]:
            if player1.pos.y <= screen.get_height() + LIMIT:
                player1.pos.y += 600 * dt
        if keys[pygame.K_UP]:
            if player1.pos.x <= screen.get_width() + LIMIT:
                player1.pos.x += 300 * dt
        if keys[pygame.K_DOWN]:
            if player1.pos.x >= -LIMIT:
                player1.pos.x -= 300 * dt
        if keys[pygame.K_a]:
            if player2.pos.y>= -LIMIT:
                player2.pos.y -= 600 * dt
        if keys[pygame.K_d]:
            if player2.pos.y<= screen.get_height() + LIMIT:
                player2.pos.y += 600 * dt
        if keys[pygame.K_w]:
            if player2.pos.x <= screen.get_width() + LIMIT:
                player2.pos.x += 300 * dt
        if keys[pygame.K_s]:
            if player2.pos.x >= -LIMIT:
                player2.pos.x -= 300 * dt

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(30) / 1000

    pygame.quit()