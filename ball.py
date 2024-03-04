import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    def __init__(self, screen, p1, p2):
        super().__init__()
        self.color = 44, 44, 44
        self.rect = pygame.Rect(780, 480, 20, 20)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.screen = screen
        self.dx = 0
        self.dy = 0

    def draw_ball(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
