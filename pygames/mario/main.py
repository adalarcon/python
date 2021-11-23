import pygame
import player
from player import Hero
from pygame import mixer

pygame.init()

TITLE = "Sprite example"
GAME_OVER_TXT = "GAME OVER"
YOU_WIN_TXT = "YOU WIN !"

BACKGROUND_SOUND = "./pygames/mario/assets/sounds/mario.mp3"

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 580

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()
game_over = False
background = pygame.image.load('./pygames/mario/assets/img/bg.jpg')

player = Hero((10, 426))

# Sound
mixer.music.load(BACKGROUND_SOUND)
mixer.music.play(-1)


while game_over == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    userMovement = pygame.key.get_pressed()
    player.handle_event(userMovement)
    screen.blit(background, (0, 0))
    screen.blit(player.image, player.rect)

    pygame.display.update()
    clock.tick(15)

pygame.quit ()