import sys
import pygame
from paddle import Paddle
from compPaddle import Computer

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1500, 1000))
    pygame.display.set_caption("Pong")
    bg_color = (235, 235, 235)
    #screen.fill(bg_color)
    p1 = Paddle(screen)
    p2 = Computer(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    p1.moving_up = True
                elif event.key == pygame.K_DOWN:
                    p1.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    p1.moving_up = False
                elif event.key == pygame.K_DOWN:
                    p1.moving_down = False
        p1.update()
        screen.fill(bg_color)
        p1.blitme()
        p2.blitme()

        pygame.display.flip()


run_game()