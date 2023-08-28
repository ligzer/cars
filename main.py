import pygame
from car import Car, CAR10, CAR13, CAR2, CAR3
from road import Road
pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
clock = pygame.time.Clock()
running = True
dt = 0

pygame.mixer.music.load("media/soundtrack.mpga")
pygame.mixer.music.play(-1)
player_pos = pygame.Vector2(screen.get_width() / 6, screen.get_height() / 2)
car1_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 4)
car2_pos = pygame.Vector2(screen.get_width() / 2, 3*screen.get_height() / 4)
car3_pos = pygame.Vector2(4*screen.get_width() / 6, screen.get_height() / 2)
desired_car_height = 180

CAR13.prepare_images(desired_car_height)
CAR10.prepare_images(desired_car_height)
CAR2.prepare_images(desired_car_height)
CAR3.prepare_images(desired_car_height)

car10 = Car(CAR13, car2_pos)
car1 = Car(CAR10, car3_pos)
car2 = Car(CAR2, car1_pos)
car3 = Car(CAR3, player_pos)

road = Road()
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

        road.draw(screen)
        car10.draw(screen)
        car1.draw(screen)
        car2.draw(screen)
        car3.draw(screen)

        keys = pygame.key.get_pressed()
        LIMIT = 0
        if keys[pygame.K_ESCAPE]:
            running = False
        if keys[pygame.K_LEFT]:
            if car10.pos.y>= -LIMIT:
                car10.pos.y -= 600 * dt
        if keys[pygame.K_RIGHT]:
            if car10.pos.y <= screen.get_height() + LIMIT:
                car10.pos.y += 600 * dt
        if keys[pygame.K_UP]:
            if car10.pos.x <= screen.get_width() + LIMIT:
                car10.pos.x += 300 * dt
        if keys[pygame.K_DOWN]:
            if car10.pos.x >= -LIMIT:
                car10.pos.x -= 300 * dt
        if keys[pygame.K_a]:
            if car1.pos.y>= -LIMIT:
                car1.pos.y -= 600 * dt
        if keys[pygame.K_d]:
            if car1.pos.y<= screen.get_height() + LIMIT:
                car1.pos.y += 600 * dt
        if keys[pygame.K_w]:
            if car1.pos.x <= screen.get_width() + LIMIT:
                car1.pos.x += 300 * dt
        if keys[pygame.K_s]:
            if car1.pos.x >= -LIMIT:
                car1.pos.x -= 300 * dt

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(30) / 1000

    pygame.quit()