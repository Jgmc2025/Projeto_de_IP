import pygame, sys, random
from stars import Stars
from settings import Settings
from fundo import Fundo
from ship import Ship
from asteroids import AsteroideCadente, AsteroideFixo
class Jogo:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.stars_code = True
        self.i = 0
        self.screen = pygame.display.set_mode((750,500))
        self.clock = pygame.time.Clock()
        self.sprite_stars = pygame.sprite.Group()
        self.stars = Stars(self)
        self.fundo = Fundo(self)
        self.ship = Ship(self)
        self.sprite_asteroids = pygame.sprite.Group()
    def rodar(self):
        while True:
            self.imagem()
            self.update()
            self.checar_colisao()
            self.apply_stars()
            self.criar_asteroids
            self.limites()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self.movimento(event)
            self.clock.tick(60)
    def limites(self):
        if self.ship.rect.right >= self.ship.screen_rect.right:
             self.settings.d = 0
        if self.ship.rect.left <= self.ship.screen_rect.left:
             self.settings.a = 0
        if self.ship.rect.bottom >= self.ship.screen_rect.bottom:
             self.settings.s = 0
        if self.ship.rect.top <= self.ship.screen_rect.top:
             self.settings.w = 0
    def movimento(self,event):
        if event.key == pygame.K_s:
            self.ship.image = pygame.image.load("1000102277.png")
            self.ship.image = pygame.transform.scale(self.ship.image,(50,60))
            self.settings.right = 0
            self.settings.left = 0
            self.settings.s = 0.4
            self.settings.w = 0
            self.settings.d = 0
            self.settings.a = 0
        elif event.key == pygame.K_w:
            self.ship.image = pygame.image.load("1000102277.png")
            self.ship.image = pygame.transform.scale(self.ship.image,(50,60))
            self.settings.right = 0
            self.settings.left = 0
            self.settings.w = 0.4
            self.settings.s = 0
            self.settings.d = 0
            self.settings.a = 0
        elif event.key == pygame.K_d:
            self.ship.image = pygame.image.load("1000102277.png")
            self.ship.image = pygame.transform.scale(self.ship.image,(50,60))
            self.ship.image = pygame.transform.rotate(self.ship.image, -30)
            self.settings.right = 0.4
            self.settings.left = 0
            self.settings.d = 0.4
            self.settings.w = 0
            self.settings.s = 0
            self.settings.a = 0
        elif event.key == pygame.K_a:
            self.ship.image = pygame.image.load("1000102277.png")
            self.ship.image = pygame.transform.scale(self.ship.image,(50,60))
            self.ship.image = pygame.transform.rotate(self.ship.image, 30)
            self.settings.left = 0.4
            self.settings.right = 0
            self.settings.a = 0.4
            self.settings.w = 0
            self.settings.d = 0
            self.settings.s = 0
    def update(self):
        self.sprite_stars.update()
        self.sprite_asteroids.update()
        for star in self.sprite_stars.copy():
            if star.rect.bottom >= self.stars.screen_rect.bottom or star.rect.right >= self.stars.screen_rect.right \
                or star.rect.left <= self.stars.screen_rect.left or star.rect.top <= self.stars.screen_rect.top:
                self._remove_and_add(star)
    def _remove_and_add(self, star):
        self.sprite_stars.remove(star)
        one_star = Stars(self)
        self.sprite_stars.add(one_star)
    def apply_stars(self):
        if self.stars_code:
            self.i += 1
            one_star = Stars(self)
            self.sprite_stars.add(one_star)
            if self.i >= 1000:
                self.stars_code = False
    def imagem(self):
        self.fundo.blitme()
        for star in self.sprite_stars.sprites():
            star.draw_stars()
        self.sprite_asteroids.draw(self)
        self.ship.draw()
        pygame.display.flip()

    def criar_asteroids(self):
            if random.randint(0, 1) < 2:
                if random.randint(0, 1) > 0.3:
                    asteroide = AsteroideCadente()
                else:
                    asteroide = AsteroideFixo()
            self.sprite_asteroids.add(asteroide)

    def checar_colisao(self):
        if pygame.sprite.spritecollide(self.ship, self.sprite_asteroids, True):
            print("Você colidiu! Fim de jogo.")
            pygame.quit()

if __name__ == "__main__":
    ai = Jogo()
    ai.rodar()
