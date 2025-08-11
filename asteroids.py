import pygame as pg
import random

class Asteroide(pg.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = pg.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        pass

class AsteroideCadente(Asteroide):
    def __init__(self, largura_tela):
        super().__init__("asteroidecadente.jpeg")
    

        self.rect.x = random.randint(0, largura_tela - self.rect.width)
        self.rect.y = random.randint(-150, -100)

        self.speed_y = random.randint(4, 10)
        self.speed_x = random.randint(-3, 3)

    def update(self, altura_tela):
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        if self.rect.top > altura_tela:
            self.kill()

class AsteroideFixo(Asteroide):
    def __init__(self, largura_tela, altura_tela):
        super().__init__("asteroidefixo.jpeg")

        self.rect.x = random.randint(0, largura_tela - self.rect.width)
        self.rect.y = random.randint(0, altura_tela - self.rect.height)
    
    def update(self):
        pass

