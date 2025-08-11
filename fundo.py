import pygame

class Fundo:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("fundo.jpeg")
        self.position = self.image.get_rect()
        self.position.y = self.screen_rect.bottom
        self.image = pygame.transform.scale(self.image, (self.screen_rect.right, self.position.bottom))
        self.screen_rect.bottom -= 2500
        self.y = float(self.screen_rect.bottom)
    def blitme(self):
        self.y += self.settings.fundo
        self.screen_rect.bottom = self.y
        self.screen.blit(self.image, self.screen_rect)