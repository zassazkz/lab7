import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((920, 700))
clock = pygame.time.Clock()

image = pygame.image.load('clock/clockclock.png')
image = pygame.transform.scale(image, (600, 600))

minute_img = pygame.image.load('clock/righthand.png')
minute_img = pygame.transform.scale(minute_img, (300, 200))
second_img = pygame.image.load('clock/lefthand.png')
second_img = pygame.transform.scale(second_img, (300, 200))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  

    current_time = datetime.datetime.now()
    hour = int(current_time.strftime("%I"))
    minute = int(current_time.strftime("%M"))
    second = int(current_time.strftime("%S"))

    hour_angle = (hour % 12 + minute / 60) * -30
    minute_angle = minute * -6 + 80
    second_angle = second * -6

    rotated_minute = pygame.transform.rotate(minute_img, minute_angle)
    rotated_second = pygame.transform.rotate(second_img, second_angle)

    screen.fill((255, 255, 255))
    screen.blit(image, (100, 100))
    screen.blit(rotated_second, (400 - int(rotated_second.get_width() / 2), 400 - int(rotated_second.get_height() / 2)))
    screen.blit(rotated_minute, (400 - int(rotated_minute.get_width() / 2), 400 - int(rotated_minute.get_height() / 2)))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()