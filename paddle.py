import pygame

class Paddle:
    def __init__(self, screen):
        self.image = pygame.image.load("images/paddle.png")
        self.screen = screen
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.midleft = self.screen_rect.midleft
        self.score = 0


        self.rect.centerx += 50
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_up and self.rect.top != self.screen.get_rect().top:
            self.rect.centery -= 1

        if self.moving_down and self.rect.bottom != self.screen.get_rect().bottom:
            self.rect.centery += 1

