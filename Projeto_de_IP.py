import pygame, sys
from stars import Stars
from settings import Settings
from fundo import Fundo
from ship import Ship
from Inimigos import Inimigos
from Inimigos import TiroInimigo
from coletaveis import Placa
from coletaveis import Combustivel
from game_over import Over
from dados import Dados
from asteroides import Asteroide
from restart import Restart
from final import Final

class Jogo:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.stars_code = True
        self.inimigos_code = True
        self.i = 0
        self.key = True
        self.primeiro_galao = True
        self.explosao = True
        self.primeira_placa = True
        self.won_game = False
        self.sair = True
        self.contador = 0
        self.diminui = 0
        self.quantas = 0
        self.quanto = 10
        self.fase = 1
        self.j = 0
        self.asta_code = True 
        self.lista = []
        self.screen = pygame.display.set_mode((750,500))
        self.clock = pygame.time.Clock()
        self.sprite_stars = pygame.sprite.Group()
        self.fundo = Fundo(self)
        self.ship = Ship(self)
        self.over = Over(self)
        self.dados = Dados(self)
        self.restart = Restart(self)
        self.inimigos = pygame.sprite.Group()
        self.tiros = pygame.sprite.Group()
        self.galao = pygame.sprite.Group()
        self.placa = pygame.sprite.Group()
        self.asteroides = pygame.sprite.Group()
    def rodar(self):
        while True:
            if self.sair:
                self.imagem()
            if self.key:
                if self.fase == 2:
                    self.aplicar_asteroides()
                else:
                    self.apply_inimigos()
                self.update()
                self.remove()
                self.atualizar()
                self.placa_e_combustivel()
                self.apply_stars()
                self.limites()
            if self.sair:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if self.key:
                            self.movimento(event)
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not self.key:
                        if self.restart.rect.collidepoint(event.pos):
                            carregar = pygame.mixer.Sound("Pasta_Menu/alto.mp3")
                            carregar.play()
                            Jogo().rodar()
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
            self.ship.image = pygame.image.load("imagens/1000102277.png").convert_alpha()
            self.ship.image = pygame.transform.scale(self.ship.image,(50,60))
            self.ship.mask = pygame.mask.from_surface(self.ship.image)
            self.settings.right = 0
            self.settings.left = 0
            self.settings.s = 3.5# ALTERACAO AQUI
            self.settings.w = 0
            self.settings.d = 0
            self.settings.a = 0
        elif event.key == pygame.K_w:
            self.ship.image = pygame.image.load("imagens/1000102277.png").convert_alpha()
            self.ship.image = pygame.transform.scale(self.ship.image,(50,60))
            self.ship.mask = pygame.mask.from_surface(self.ship.image)
            self.settings.right = 0
            self.settings.left = 0
            self.settings.w = 2
            self.settings.s = 0
            self.settings.d = 0
            self.settings.a = 0
        elif event.key == pygame.K_d:
            self.ship.image = pygame.image.load("imagens/1000102277.png").convert_alpha()
            self.ship.image = pygame.transform.scale(self.ship.image,(50,60))
            self.ship.image = pygame.transform.rotate(self.ship.image, -30)
            self.ship.mask = pygame.mask.from_surface(self.ship.image)
            self.settings.right = 2
            self.settings.left = 0
            self.settings.d = 2
            self.settings.w = 0
            self.settings.s = 0
            self.settings.a = 0
        elif event.key == pygame.K_a:
            self.ship.image = pygame.image.load("imagens/1000102277.png").convert_alpha()
            self.ship.image = pygame.transform.scale(self.ship.image,(50,60))
            self.ship.image = pygame.transform.rotate(self.ship.image, 30)
            self.ship.mask = pygame.mask.from_surface(self.ship.image)
            self.settings.left = 2
            self.settings.right = 0
            self.settings.a = 2
            self.settings.w = 0
            self.settings.d = 0
            self.settings.s = 0
    def update(self):
        self.sprite_stars.update()
        for star in self.sprite_stars.copy():
            if star.rect.bottom >= self.ship.screen_rect.bottom or star.rect.right >= self.ship.screen_rect.right \
                or star.rect.left <= self.ship.screen_rect.left:
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
    def _remove_and_add_asteroide(self, asteroide):
        self.asteroides.remove(asteroide)
        asta = Asteroide(self)
        self.asteroides.add(asta)
    def aplicar_asteroides(self):
        if self.asta_code:
            self.j += 1
            if self.j % 200 == 0:
                asta = Asteroide(self)
                self.asteroides.add(asta)
                if self.j >= (6 * 200):
                    self.j = 0
                    self.asta_code = False
        for asteroide in self.asteroides.copy():
            asteroide.atualizar()
            if asteroide.rect.bottom >= self.ship.screen_rect.bottom + 200:
                self._remove_and_add_asteroide(asteroide)
            if asteroide.rect.colliderect(self.ship.rect):
                self.asteroides.remove(asteroide)
                self.settings.w = 0
                self.settings.a = 0
                self.settings.s = 0
                self.settings.d = 0
                self.settings.fundo = 0
                self.key = False
                self.over.tocar_musica()
    def placa_e_combustivel(self):
        self.diminui += 1
        if self.quanto > 10:
            self.quanto = 10
        if self.diminui % 200 == 0:
            self.diminui = 0
            self.quanto -= 1
            if self.quanto > 10:
                self.quanto = 10
            self.settings.texto = f"Placas: {self.quantas}/{self.settings.quant_placas} | Combustível: {self.quanto}/10 | Fase: {self.fase}/3"
        if self.quanto == 0:
            self.settings.w = 0
            self.settings.a = 0
            self.settings.s = 0
            self.settings.d = 0
            self.settings.fundo = 0
            self.key = False
            self.over.tocar_musica()
        if self.quantas == self.settings.quant_placas:
            self.primeira_placa = True
            self.primeiro_galao = True
            self.inimigos.empty()
            self.tiros.empty()
            self.galao.empty()
            self.placa.empty()
            self.sprite_stars.empty()
            self.stars_code = True
            self.ship.__init__(ai_game=Ship(self))
            self.fase += 1
            if self.fase == 2:
                self.settings.quant_placas = 15
                self.settings.imagem = "imagens/fase2.png"
                self.fundo = Fundo(self)
            elif self.fase == 3:
                self.settings.quant_inimigos = 7
                self.settings.quant_placas = 15
                self.settings.vel_tiro = 6
                self.settings.vel_lados = 1.5
                self.settings.imagem = "imagens/fase3.jpg"
                self.fundo = Fundo(self)
            else:
                self.settings.w = 0
                self.settings.a = 0
                self.settings.s = 0
                self.settings.d = 0
                self.settings.fundo = 0
                self.won_game = True
                self.key = False
                self.over.tocar_musica()
            self.quantas = 0
            self.quanto = 10
        if self.primeira_placa:
            placa = Placa(self)
            self.placa.add(placa)
            self.primeira_placa = False
        if self.primeiro_galao:
            galao = Combustivel(self)
            self.galao.add(galao)
            self.primeiro_galao = False
        self.placa.update()
        self.galao.update()
        for placa in self.placa.copy():
            if placa.rect.colliderect(self.ship.rect):
                self.quantas += 1
                if self.quanto > 10:
                    self.quanto = 10
                self.settings.texto = f"Placas: {self.quantas}/{self.settings.quant_placas} | Combustível: {self.quanto}/10 | Fase: {self.fase}/3"
                som = pygame.mixer.Sound("imagens/pop.mp3")
                som.set_volume(0.3)
                som.play()
                self.placa.remove(placa)
                self.primeira_placa = True
            if placa.y >= self.ship.screen_rect.bottom + 100:
                self.placa.remove(placa)
                self.primeira_placa = True
        for galao in self.galao.copy():
            if galao.rect.colliderect(self.ship.rect):
                self.diminui = 0
                self.quanto += 1
                if self.quanto > 10:
                    self.quanto = 10
                self.settings.texto = f"Placas: {self.quantas}/{self.settings.quant_placas} | Combustível: {self.quanto}/10 | Fase: {self.fase}/3"
                som = pygame.mixer.Sound("imagens/plim.mp3")
                som.set_volume(0.3)
                som.play()
                self.galao.remove(galao)
                self.primeiro_galao = True
            if galao.y >= self.ship.screen_rect.bottom + 100:
                self.galao.remove(galao)
                self.primeiro_galao = True
    def apply_inimigos(self):
        if self.inimigos_code:
            self.contador += 1
            if self.contador % 200 == 0:
                inimigo = Inimigos(self)
                self.lista.append(inimigo)
                self.inimigos.add(inimigo)
                self.atirar(inimigo)
            elif self.contador >= (self.settings.quant_inimigos * 200):
                self.contador = 0
                self.inimigos_code = False
    def atualizar(self):
        i = 0
        for tiro in self.tiros.copy():
            tiro.atualizar()
            if tiro.rect.colliderect(self.ship.rect):
                self.tiros.remove(tiro)
                self.settings.w = 0
                self.settings.a = 0
                self.settings.s = 0
                self.settings.d = 0
                self.settings.fundo = 0
                self.key = False
                self.over.tocar_musica()
            if tiro.y >= self.ship.screen_rect.bottom + 200:
                if self.inimigos.copy():
                    inimigo = self.lista[i]
                    tiro.x,tiro.y = inimigo.x + 25,inimigo.y + 25
                    if inimigo.y >= self.ship.y or inimigo.y >= self.ship.screen_rect.bottom - 170:
                        self.tiros.remove(tiro)
                        self.lista.pop(i)
                    else:
                        som = pygame.mixer.Sound("imagens/tiro.mp3")
                        som.set_volume(0.2)
                        som.play()
                else:
                    self.tiros.empty()
                    self.lista = []
            i += 1
    def atirar(self,inimigo):
        som = pygame.mixer.Sound("imagens/tiro.mp3")
        som.set_volume(0.2)
        som.play()
        tiro = TiroInimigo(self)
        tiro.x,tiro.y = inimigo.x + 25,inimigo.y + 25
        self.tiros.add(tiro)
    def remove(self):
        self.inimigos.update()
        if not self.inimigos.copy():
            self.inimigos_code = True
        if self.ship.screen_rect.top <= self.fundo.screen_rect.top:
            self.settings.w = 0
            self.settings.a = 0
            self.settings.s = 0
            self.settings.d = 0
            self.settings.fundo = 0
            self.key = False
            self.over.tocar_musica()
        for inimigo in self.inimigos.copy():
            if inimigo.y >= self.ship.screen_rect.bottom - 170:
                inimigo.y += 4
            if inimigo.rect.colliderect(self.ship.rect):
                self.inimigos.remove(inimigo)
                self.settings.w = 0
                self.settings.a = 0
                self.settings.s = 0
                self.settings.d = 0
                self.settings.fundo = 0
                self.key = False
                self.over.tocar_musica()
            if inimigo.rect.bottom >= self.ship.screen_rect.bottom + 100:
                self.inimigos.remove(inimigo)
            if inimigo.x >= self.fundo.screen_rect.right:
                inimigo.direita = False
                inimigo.esquerda = True
            if inimigo.x <= self.fundo.screen_rect.left:
                inimigo.direita = True
                inimigo.esquerda = False
    def imagem(self):
        self.fundo.blitme()
        for star in self.sprite_stars.sprites():
            star.draw_stars()
        for galao in self.galao.sprites():
            galao.desenhar()
        for placa in self.placa.sprites():
            placa.desenhar()
        if self.fase != 2:
            for tiro in self.tiros.sprites():
                tiro.desenhe()
            for inimigo in self.inimigos.sprites():
                inimigo.desenhar()
        else:
            for asteroide in self.asteroides.sprites():
                asteroide.desenhar()
        if not self.won_game:
            self.ship.draw()
        if not self.key and not self.won_game:
            self.restart.desenhar()
            if self.explosao:
                som = pygame.mixer.Sound("imagens/explosao.mp3")
                som.set_volume(0.5)
                som.play()
                self.explosao = False
            imagem = pygame.image.load("imagens/explosao.png")
            self.ship.image = pygame.transform.scale(imagem,(100,120))
            self.over.desenhar()
        elif self.won_game:
            self.sair = False
            Final().ativar()
        else:
            self.dados.desenhar()
        pygame.display.flip()

