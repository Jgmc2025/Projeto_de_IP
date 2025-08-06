import pygame


class TiroInimigo(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        self.image = pygame.Surface((4, 15))
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()

        self.rect.center = (x, y)
        self.velocidade = 7

    def update(self):

        self.rect.y += self.velocidade

        if self.rect.top > 500: 
            self.kill()



class Inimigos(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super().__init__()

        self.image = pygame.image.load("NaveInimiga.jpeg")
        self.image = pygame.transform.scale(self.image, (50, 40))

        self.rect = self.image.get_rect()

        self.rect.topleft = (x, y)

        self.velocidade_x = 12
        self.velocidade_y = 8

    def atirar(self):

        return TiroInimigo(self.rect.centerx, self.rect.bottom)
    
    def update(self):

        self.rect.x += self.velocidade_x
        self.rect.y += self.velocidade_y

        if self.rect.x <= 15 or self.rect.x >= 735:

            self.velocidade_x *= -1

        if self.rect.y >= 500:

            self.kill()


        
