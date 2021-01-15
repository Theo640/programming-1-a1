# sprite_example.py
# Introduction to the Sprite class

# Goals:
#   * introduce the Sprite class
#   * subclass the Sprite class (inheritance)

import random
import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 800
HEIGHT = 600
TITLE = "Sprite Example"
NUM_JEWELS = 45


class Jewel(pygame.sprite.Sprite):
    def __init__(self):
        # call the superclass constructor
        super().__init__()

        # Image is a surface
        self.image = pygame.Surface((35,20))
        self.image.fill((100, 255, 100))

        # Rect is Rectangle (x, y, width, height)
        self.rect = self.image.get_rect()




def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # Sprite group and sprite creation
    all_sprites_group = pygame.sprite.Group()

    # Jewel creation
    for i in range(NUM_JEWELS):
        jewel = Jewel()
        jewel.rect.x = random.randrange(WIDTH - jewel.rect.width)
        jewel.rect.y = random.randrange(HEIGHT - jewel.rect.height)
        all_sprites_group.add(jewel)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC

        # ----- DRAW
        screen.fill(BLACK)
        all_sprites_group.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()