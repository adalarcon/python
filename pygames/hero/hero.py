import pygame, sys
from pygame.locals import *

# definimos nuestros colores para el juego
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (0, 0, 255)
YELLOW = (255, 0, 255)
RED = (255,  0, 0)

# funcion principal de nuestro juego
def main():
  SCREEN_WIDTH = 480
  SCREEN_HEIGHT = 360
  hero_pos_x = 240
  hero_pos_y = 180 

  
  # inicializamos el juego
  pygame.init()
  pygame.display.set_caption("Hola mundo de pygame")
  background = pygame.image.load('./pygames/hero/bg.jpg')
  hero = pygame.image.load('./pygames/hero/hero.png')
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
  while True:
    # 1. Actualizar la pantalla 
    screen.fill(RED)
    screen.blit(background, (0, 0))
    screen.blit(hero, (hero_pos_x, hero_pos_y))

    # 2. Capturamos los eventos 
    for event in pygame.event.get():
      if event.type == QUIT:
        print("evento QUIT")
        pygame.quit() # termina juego de pygame
        sys.exit(0) # termina el programa

      if event.type == MOUSEBUTTONDOWN:
        x, y = event.pos
        hero_pos_x = x - 15
        print("evento MOUSEBUTTONDOWN")
        
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          print("evento KEYDOWN")
          pygame.quit() # termina juego de pygame
          sys.exit(0) # termina el programa
        if event.key == K_UP:
          hero_pos_y = hero_pos_y - 10
          print("evento KEYDOWN KEY UP")
        if event.key == K_RIGHT:
          print("evento KEYDOWN K_RIGHT")
          hero_pos_x = hero_pos_x + 10
        if event.key == K_DOWN:
          hero_pos_y = hero_pos_y + 10
          print("evento KEYDOWN K_DOWN")
        if event.key == K_LEFT:
          hero_pos_x = hero_pos_x - 10
          print("evento KEYDOWN K_LEFT")

    # 3. Actualizamos pantalla
    pygame.display.update()

main()