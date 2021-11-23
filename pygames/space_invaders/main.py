import math
import random
import sys

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

TITLE = "Space Invader"
GAME_OVER_TXT = "GAME OVER"
YOU_WIN_TXT = "YOU WIN !"

BACKGROUND_SOUND = "./pygames/space_invaders/assets/sounds/background.mp3"
LASER_SOUND = "./pygames/space_invaders/assets/sounds/laser.wav"
EXPLOSION_SOUND = "./pygames/space_invaders/assets/sounds/explosion.wav"
WIN_SOUND = './pygames/space_invaders/assets/sounds/win.wav'
GAME_OVER_SOUND = './pygames/space_invaders/assets/sounds/game over.wav'

BACKGROUND_IMG = './pygames/space_invaders/assets/img/background.png'
ICON_IMG = './pygames/space_invaders/assets/img/hero.png'
HERO_IMG = './pygames/space_invaders/assets/img/hero.png'
ENEMY_IMG = './pygames/space_invaders/assets/img/enemy.png'
ENEMY_IMG1 = './pygames/space_invaders/assets/img/enemy1.png'
ENEMY_IMG2 = './pygames/space_invaders/assets/img/enemy2.png'
BULLET_IMG = './pygames/space_invaders/assets/img/bullet.png'

BULLET_READY_STATE = 0
BULLET_FIRE_STATE = 1

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600

ENEMY_VELOCITY = 4;
PLAYER_VELOCITY = 5

# create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background
background = pygame.image.load(BACKGROUND_IMG)
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Sound
mixer.music.load(BACKGROUND_SOUND)
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption(TITLE)
icon = pygame.image.load(ICON_IMG)
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load(HERO_IMG)
player_x = (SCREEN_WIDTH / 2) - (64/2)
player_y = SCREEN_HEIGHT - 120
player_x_change = 0

# Enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_velocity = []
enemy_y_velocity = []
num_of_enemies = 10

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load(random.choice([ENEMY_IMG, ENEMY_IMG1, ENEMY_IMG2])  ))
    enemy_x.append(random.randint(0, SCREEN_WIDTH - 64))
    enemy_y.append(random.randint(0, SCREEN_HEIGHT // 2))
    enemy_x_velocity.append(random.randint(4, 8))
    enemy_y_velocity.append(40)

# Bullet
bullet_img = pygame.image.load(BULLET_IMG)
bullet_x = 0
bullet_y = SCREEN_HEIGHT - 120
bullet_x_change = 10
bullet_y_change = 10
bullet_state = BULLET_READY_STATE

# Score
score_value = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)
score_x = 10
score_y = 10

# Message
message_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score():
    score_text = score_font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score_text, (score_x, score_y))

def show_message_text(text):
    message_text = message_font.render(text, True, (255, 255, 255))
    text_rect = message_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(message_text, text_rect)

def show_player(player_img, x, y):
    screen.blit(player_img, (x, y))

def show_enemy(enemy_img, x, y ):
    screen.blit(enemy_img, (x, y))

def show_bullet(x, y):
    global bullet_state
    bullet_state = BULLET_FIRE_STATE
    screen.blit(bullet_img, (x + 16, y + 10))

def isCollision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt(math.pow(enemy_x - bullet_x, 2) + (math.pow(enemy_y - bullet_y, 2)))
    if distance < 27:
        return True
    else:
        return False

def main():
        
    global player_x
    global player_x_change
    global player_y_change
    global bullet_x
    global bullet_y
    global bullet_state
    global num_of_enemies

    # Game Loop
    running = True
    finished = False
    while running:

        # RGB = Red, Green, Blue
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        # Detect events 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit() # termina juego de pygame
                sys.exit(0) # termina el programa

            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -PLAYER_VELOCITY
                if event.key == pygame.K_RIGHT:
                    player_x_change = PLAYER_VELOCITY
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    player_x_change = 0

                # Fire bullet
                if event.key == pygame.K_SPACE:
                    if bullet_state is BULLET_READY_STATE:
                        mixer.Sound(LASER_SOUND).play()
                        # Get the current x cordinate of the spaceship
                        bullet_x = player_x
                        show_bullet(bullet_x, bullet_y)

        # Player Movement
        player_x += player_x_change
        if player_x <= 0:
            player_x = 0
        elif player_x >= SCREEN_WIDTH - 64:
            player_x = SCREEN_WIDTH - 64

        # Detect if you win
        if num_of_enemies <= 0:
            mixer.music.stop()
            if not finished:
                mixer.Sound(WIN_SOUND).play(0)
            show_message_text(YOU_WIN_TXT)
            finished = True
            
        # Enemy Movement
        for i in range(num_of_enemies):

            # Game Over
            if enemy_y[i] > SCREEN_HEIGHT - 160 and not finished:
                for j in range(num_of_enemies):
                    enemy_y[j] = SCREEN_HEIGHT * 2
                show_message_text(GAME_OVER_TXT)
                mixer.music.stop()
                if not finished:
                    mixer.Sound(GAME_OVER_SOUND).play(0)
                finished = True
                break

            # Enemy Movement
            enemy_x[i] += enemy_x_velocity[i]

            #detect limits
            if enemy_x[i] <= 0 or enemy_x[i] >= SCREEN_WIDTH - 64:
                enemy_x_velocity[i] = enemy_x_velocity[i] * -1
                enemy_y[i] += enemy_y_velocity[i]

            # Detect collision
            collision = isCollision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
            if collision:
                mixer.Sound(EXPLOSION_SOUND).play()
                bullet_y = SCREEN_HEIGHT - 120
                bullet_state = BULLET_READY_STATE
                global score_value
                score_value += 1
                enemy_x.pop(i)
                enemy_y.pop(i)
                enemy_img.pop(i)
                num_of_enemies -= 1
                break
                

            show_enemy(enemy_img[i], enemy_x[i], enemy_y[i])

        # Bullet Movement
        if bullet_state is BULLET_FIRE_STATE:
            show_bullet(bullet_x, bullet_y)
            bullet_y -= bullet_y_change

        if bullet_y <= 0:
            bullet_y = SCREEN_HEIGHT - 120
            bullet_state = BULLET_READY_STATE

        show_player(player_img, player_x, player_y)
        show_score()
        pygame.display.update()

main()