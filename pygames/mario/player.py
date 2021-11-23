
import pygame

class Hero(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('./pygames/mario/assets/img/mario.png')
        self.sheet.set_clip(pygame.Rect(0, 152, 52, 76))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.x_veloxity = 10
        self.y_veloxity = 10
        self.jump = False
        self.direction = ""

        self.left_states = { 
            0: (0, 76, 52, 76), 
            1: (52, 76, 52, 76), 
            2: (156, 76, 52, 76) 
        }
        self.right_states = { 
            0: (0, 152, 52, 76), 
            1: (52, 152, 52, 76), 
            2: (156, 152, 52, 76) 
        }

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= self.x_veloxity
            if self.rect.x <= 0:
                self.rect.x = -10
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += self.x_veloxity

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])

        if self.jump and self.direction == 'right':
            self.clip(self.right_states)
        if self.jump and self.direction == 'left':
            self.clip(self.left_states)

        if self.jump:
            self.rect.y -= self.y_veloxity
            self.y_veloxity -= 1
            if self.y_veloxity < -10:
                self.jump = False
                self.y_veloxity = 10

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):

        if event[pygame.K_LEFT]:
            self.direction == 'left'
            self.update('left')
        if event[pygame.K_RIGHT]:
            self.direction == 'right'
            self.update('right')
        if event[pygame.K_UP]:
            self.jump = True
        if event[pygame.K_SPACE]:
            self.jump = True
            
        if self.jump:
            self.update('jump')

   