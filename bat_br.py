from config_2 import *
import pygame
class Bat:
     def __init__(self):
        self.x=(SCREEN_WIDTH-BAT_WIDTH)//2
        self.y=SCREEN_HEIGHT-BAT_OFFSET
        self.speed_x=0
     def update(self):
         self.x+=self.speed_x
         keys = pygame.key.get_pressed()
         if keys[pygame.K_a]:
             self.speed_x+=-1
         elif keys[pygame.K_d]:
             self.speed_x += 1
         else:
             self.speed_x=0
         if self.x<=0:
             self.x = 0
         if self.x >= SCREEN_WIDTH-BAT_WIDTH:
             self.x = SCREEN_WIDTH-BAT_WIDTH

        
