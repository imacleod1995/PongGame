import pygame
from pygame.sprite import Sprite

class Ball(Sprite):
    def __init__(self, screen, p1, p2):
        super().__init__()
        self.color = 44, 44, 44
        self.rect = pygame.Rect(780, 480, 20, 20)
        self.p1 = p1
        self.p2 = p2
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.screen = screen
        self.dx = -1
        self.dy = -1
        self.x_moving_down = False


    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y


    def check_boundaries(self):
        if self.rect.bottom == self.screen.get_rect().bottom:
            self.dy = -1
            self.x_moving_down = False
        elif self.rect.colliderect(self.p1.rect):
            self.dy = 1
            self.dx = 1
            self.x_moving_down = True
        elif self.rect.colliderect(self.p2.rect):
            self.dx = -1
            self.dy = 1
        elif self.rect.top == self.screen.get_rect().top:
            self.dy = 1
            self.x_moving_down = True
        elif self.rect.left > self.screen.get_rect().right:
            #p1 scores
            self.p1.score += 1
            self.x = 780
            self.y = 480
        elif self.rect.right < self.screen.get_rect().left:
            #p2 scores
            self.p2.score += 1
            self.x = 780
            self.y = 480

    def draw_ball(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
