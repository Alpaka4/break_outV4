import pygame
from config_2 import *
from brick import Brick
class BrickRow:
    def __init__(self):
        self.row=[]
        y=80
        colors=[RED,RED,ORANGE,ORANGE,GREEN,GREEN,YELLOW,YELLOW]
        for i in range(8):
            color=colors[i]
            for i in range(20):
                x=i*BRICK_WIDTH
                brick=Brick(x,y,color,)
                self.row.append(brick)
            y+=BRICK_HEIGHT + 1
    def update(self):
        pass
