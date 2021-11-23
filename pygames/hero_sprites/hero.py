import pygame, sys
from pygame.locals import *

# definimos nuestros colores para el juego
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (0, 0, 255)
YELLOW = (255, 0, 255)
RED = (255,  0, 0)

SCREEN_WITH  = 1024
SCREEN_HEIGHT = 748

HERO_POS_X = SCREEN_WITH / 2
HERO_POS_Y = SCREEN_HEIGHT / 2 

def event_handle(event):

  global HERO_POS_X
  global HERO_POS_Y

  if event.type == MOUSEBUTTONDOWN:
    x, y = event.pos
    HERO_POS_X = x - 15
    print("evento MOUSEBUTTONDOWN")
  if event.type == KEYDOWN:
    if event.key == K_ESCAPE:
      print("evento KEYDOWN")
      pygame.quit() # termina juego de pygame
      sys.exit(0) # termina el programa
    if event.key == K_UP:
      HERO_POS_Y = HERO_POS_Y - 10
      print("evento KEYDOWN KEY UP")
    if event.key == K_RIGHT:
      print("evento KEYDOWN K_RIGHT")
      HERO_POS_X = HERO_POS_X + 10
    if event.key == K_DOWN:
      HERO_POS_Y = HERO_POS_Y + 10
      print("evento KEYDOWN K_DOWN")
    if event.key == K_LEFT:
      HERO_POS_X = HERO_POS_X - 10
      print("evento KEYDOWN K_LEFT")


# funcion principal de nuestro juego
def main():
  # inicializamos el juego
  pygame.init()
  pygame.display.set_caption("Hola mundo de pygame")
  screen = pygame.display.set_mode((SCREEN_WITH, SCREEN_HEIGHT))
  background = pygame.image.load('./pygames/hero_sprites/bg.jpg')
  

  hero = pygame.image.load('./pygames/hero_sprites/hero.png')
  hero.set_clip(pygame.Rect(0, 0, 52, 76))

  image = hero.subsurface(hero.get_clip())
  rect = image.get_rect()
  rect.topleft = (HERO_POS_X, HERO_POS_Y)
  clock = pygame.time.Clock()

  while True:
    # 1. Actualizar la pantalla 
    screen.fill(RED)
    screen.blit(background, (0, 0))
    screen.blit(image, rect)
    pygame.display.flip()
    clock.tick(20)

    # 2. Capturamos los eventos 
    for event in pygame.event.get():
      if event.type == QUIT:
        print("evento QUIT")
        pygame.quit() # termina juego de pygame
        sys.exit(0) # termina el programa

      event_handle(event)

    # 3. Actualizamos pantalla
    pygame.display.update()

main()