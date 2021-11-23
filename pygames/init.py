import random, pygame, sys
from pygame.locals import *

# Declaración de constantes y variables
WHITE = (255, 255, 255)

# Función principal del juego
def main():
  # Se inicializa el juego
  pygame.init()
  pygame.display.set_caption("Título del juego")
  screen = pygame.display.set_mode((480,360))

  # Bucle principal
  while True:

    # 1.- Se dibuja la pantalla
    screen.fill(WHITE)

    # 2.- Se comprueban los eventos
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit(0)

    # 3.- Se actualiza la pantalla
    pygame.display.update()


main()