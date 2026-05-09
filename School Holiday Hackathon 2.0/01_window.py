# 01_window.py
# Open a pygame window and change its background color!

import pygame

pygame.init()

# Window settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame Window")

# Change this color! Use a readable name like "skyblue" or "black"
BACKGROUND = pygame.Color("midnightblue")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND)
    pygame.display.flip()

pygame.quit()
