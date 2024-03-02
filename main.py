import sys
import pygame
from paddle import Paddle

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1500, 1000))
    pygame.display.set_caption("Pong")
    bg_color = (235, 235, 235)
    screen.fill(bg_color)
    p1 = Paddle(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        p1.blitme()
        pygame.display.flip()


run_game()