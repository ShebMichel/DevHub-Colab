# 04_space_scene.py
# A space scene — tweak the parameters to make it your own!

import pygame
import random

pygame.init()

# ---- PARAMETERS — change these! ----
WIDTH, HEIGHT   = 800, 600
NUM_STARS       = 200
PLANET_COLOR    = pygame.Color("cornflowerblue")
PLANET_RADIUS   = 90
PLANET_X        = 220
PLANET_Y        = 300
MOON_COLOR      = pygame.Color("lightgray")
MOON_RADIUS     = 30
RING_COLOR      = pygame.Color("tan")
# ------------------------------------

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Scene")

# Generate stars once
random.seed(42)
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT),
          random.randint(1, 3)) for _ in range(NUM_STARS)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color("midnightblue"))

    # Stars
    for sx, sy, sr in stars:
        pygame.draw.circle(screen, pygame.Color("white"), (sx, sy), sr)

    # Planet ring (drawn behind planet)
    pygame.draw.ellipse(screen, RING_COLOR,
                        (PLANET_X - 130, PLANET_Y - 20, 260, 40), 6)

    # Planet
    pygame.draw.circle(screen, PLANET_COLOR, (PLANET_X, PLANET_Y), PLANET_RADIUS)

    # Planet shading (slightly darker circle offset)
    pygame.draw.circle(screen, pygame.Color("steelblue"),
                       (PLANET_X + 20, PLANET_Y - 20), PLANET_RADIUS - 20)

    # Moon
    pygame.draw.circle(screen, MOON_COLOR,
                       (PLANET_X + PLANET_RADIUS + 60, PLANET_Y - 50), MOON_RADIUS)

    # Distant small planet
    pygame.draw.circle(screen, pygame.Color("coral"), (620, 120), 45)

    pygame.display.flip()

pygame.quit()
