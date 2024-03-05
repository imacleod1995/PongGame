import sys
import pygame
from paddle import Paddle
from compPaddle import Computer
from ball import Ball

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1600, 1000))
    pygame.display.set_caption("Pong")
    bg_color = (235, 235, 235)
    txt_color = (0, 0, 0)
    blue = (0,0,128)
    font = pygame.font.SysFont('Comic Sans MS', size=16)
    p1_score = pygame.font.SysFont("Times New Roman", size=16)
    p2_score = pygame.font.SysFont("Times New Roman", size=16)
    text = font.render("Pong", True, (0, 0, 0))
    p1 = Paddle(screen)
    p2 = Computer(screen)
    #p1_text = font.render("Player 1 Score: {}".format(p1.score), True, (0, 0, 0))
    #p2_text = font.render("Player 2 Score: {}".format(p2.score), True, (0, 0, 0))
    ball = Ball(screen, p1, p2)
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
        p2.update(ball)
        ball.check_boundaries()
        ball.update()
        screen.fill(bg_color)
        p1_text = font.render("Player 1 Score: {}".format(p1.score), True, (0, 0, 0))
        p2_text = font.render("Player 2 Score: {}".format(p2.score), True, (0, 0, 0))
        screen.blit(p1_text, (150,10))
        screen.blit(p2_text, (1300, 10))
        p1.blitme()
        p2.blitme()
        ball.draw_ball()

        pygame.display.flip()


run_game()