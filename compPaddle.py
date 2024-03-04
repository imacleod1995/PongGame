import pygame
import random


class Computer():
    def __init__(self, screen):
        self.image = pygame.image.load("images/paddle.png")
        self.screen = screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.midright = self.screen_rect.midright

        self.rect.centerx -= 50
        self.move_up = False
        self.move_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self, ball):
        pass


