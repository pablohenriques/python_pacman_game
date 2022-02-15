import pygame

pygame.init()

AMARELO = (255, 255, 0)
tela = pygame.display.set_mode((640, 480), 0)

while True:
    # calcular regras
    # pintar a tela
    pygame.draw.circle(tela, AMARELO, (320, 240), 50, 0)
    pygame.display.update()

    # Analisar eventos
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()