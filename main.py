import pygame
from constants import *

def main():
    # init pygame
    pygame.init()

    # set options
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # infinite loop runs game
    while True:
        # enable x button to quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # create window with black background
        color = [0,0,0]
        screen.fill(color)

        # update display
        pygame.display.flip()

if __name__ == "__main__":
    main()
