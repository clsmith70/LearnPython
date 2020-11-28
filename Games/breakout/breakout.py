import pygame

pygame.init()
screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()
background_image = \
    pygame.image.load(r"/home/pi/Code/Games/breakout/images/space2.jpeg")

while True:
    screen.blit(background_image, (0, 0))
    pygame.display.update()
    clock.tick(60)