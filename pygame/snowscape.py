# snowscape.py
# create a serene snow falling scene

# GOAL:
#   * create 100s if objects
#   *

import random
import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "Snowscape"
NUM_SNOW = 150

class Snow:
    def __init__(self, radius=1):
        self.radius = radius

        self.x, self.y = (
            random.randrange(0, WIDTH),
            random.randrange(0, HEIGHT)
        )

        self.colour = WHITE

        self.vel_y = 3

    def draw(self, screen):
        """Draws the snow on the screen.

        Arguments:
            screen - pygame.surface to draw on

        Returns:
            None
        """
        pygame.draw.circle(
            screen,
            self.colour,
            (self.x, self.y),
            self.radius
        )

    def update(self):
        """Update location of snow"""
        self.y += self.vel_y

        if self.y > HEIGHT:
            self.x = random.randrange(0, WIDTH)
            self.y = random.randrange(-15, 0)


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # create snow objects
    snow_list = []
    # farther snow
    for i in range(NUM_SNOW):
        snow = Snow()
        snow_list.append(snow)
        # closer snow
    for i in range(NUM_SNOW):
        snow = Snow(random.choice([3, 4, 5]))
        snow.vel_y = random.choice([4, 5])
        snow_list.append(snow)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        for snow in snow_list:
            snow.update()

        # ----- DRAW
        screen.fill(BLACK)
        for snow in snow_list:
            snow.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()