import pygame
import player

pygame.init()

# Definimos algunas variables que usaremos en nuestro código

ancho_ventana = 1024
alto_ventana = 748
screen = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Tutorial sprites Piensa 3D")
clock = pygame.time.Clock()
player = player.Kate((ancho_ventana/2, alto_ventana/2))
game_over = False
background = pygame.image.load('./pygames/hero_sprites/bg.jpg')


while game_over == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    player.handle_event(event)
    screen.blit(background, (0, 0))
    screen.blit(player.image, player.rect)

    pygame.display.flip()
    clock.tick(15)

pygame.quit ()