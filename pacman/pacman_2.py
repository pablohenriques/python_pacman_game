import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600), 0)

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)


class Pacman:

    def __init__(self):
        self.linha = 1
        self.coluna = 1
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = 800 // 30
        self.vel_x = 1
        self.vel_y = 1
        self.raio = int(self.tamanho / 2)

    def calcular_regras(self):
        self.coluna = self.coluna + self.vel_x
        self.linha = self.linha + self.vel_y
        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)

        if (self.centro_x + self.raio) > 800:
            self.vel_x = -1
        if (self.centro_x - self.raio) < 0:
            self.vel_x = 1

        if (self.centro_y + self.raio) > 600:
            self.vel_y = -1
        if (self.centro_y - self.raio) < 0:
            self.vel_y = 1

    def pintar(self, tela):
        # desenhar corpo do pacman
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)

        # desenho da boca do pacman
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)

        # desenho do olho pacman
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)

    def __str__(self):
        return f"{self.centro_x}"


if __name__ == "__main__":
    pacman = Pacman()

    while True:
        # calcular as regras
        pacman.calcular_regras()

        # pintar a tela
        screen.fill(PRETO)
        pacman.pintar(screen)
        pygame.display.update()
        pygame.time.delay(100)

        # capturar os eventos
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()