import pygame
from random import randint
from pygame.sprite import Sprite

class Stars(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.color = (200,200,200)
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("big_star.png")
        self.image = pygame.transform.scale(self.image, (1,1))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, self.screen_rect.right)
        self.rect.y = randint(0, self.screen_rect.bottom)
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.settings.right
        self.x += self.settings.left
        self.y += self.settings.up

        self.rect.y = self.y
        self.rect.x = self.x

    def draw_stars(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

