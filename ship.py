import pygame

class Ship:
    def __init__(self, ai_game):
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load("1000102277.png")
        self.image = pygame.transform.scale(self.image,(50,60))
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def draw(self):
        self.x += self.settings.d
        self.x -= self.settings.a
        self.y -= self.settings.w
        self.y += self.settings.s

        self.rect.y = self.y
        self.rect.x = self.x
        self.screen.blit(self.image, self.rect)

