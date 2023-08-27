import pygame
from car import Car
from road import Road
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 6, screen.get_height() / 2)
car1_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 4)
car2_pos = pygame.Vector2(screen.get_width() / 2, 3*screen.get_height() / 4)
car3_pos = pygame.Vector2(4*screen.get_width() / 6, screen.get_height() / 2)
desired_car_height = 180
car10 = Car('car10', desired_car_height, player_pos, pygame.Vector2(120, 0), pygame.Vector2(270, 0))
car1 = Car('car10', desired_car_height, car1_pos, pygame.Vector2(120, 0), pygame.Vector2(270, 0))
car2 = Car('car13', desired_car_height, car2_pos, pygame.Vector2(220, -10), pygame.Vector2(340, -10))
car3 = Car('car13', desired_car_height, car3_pos, pygame.Vector2(220, -10), pygame.Vector2(340, -10))

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
        screen.fill("grey")

        road.draw(screen)
        car10.draw(screen)
        car1.draw(screen)
        car2.draw(screen)
        car3.draw(screen)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car10.car_rect.y -= 600 * dt
        if keys[pygame.K_RIGHT]:
            car10.car_rect.y += 600 * dt
        if keys[pygame.K_UP]:
            car10.car_rect.x += 300 * dt
        if keys[pygame.K_DOWN]:
            car10.car_rect.x -= 300 * dt
        if keys[pygame.K_a]:
            car3.car_rect.y -= 600 * dt
        if keys[pygame.K_d]:
            car3.car_rect.y += 600 * dt
        if keys[pygame.K_w]:
            car3.car_rect.x += 300 * dt
        if keys[pygame.K_s]:
            car3.car_rect.x -= 300 * dt

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    pygame.quit()