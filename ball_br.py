from config_2 import *
class Ball:
    def __init__(self):
        self.r = 20
        self.x = SCREEN_WIDTH//2
        self.y = SCREEN_HEIGHT // 2
        self.speed_x=7
        self.speed_y=6
        self.left_score = 0
    def update(self):
        # передвигаем мяч по экарну
        self.x+=self.speed_x
        self.y+=self.speed_y
        #выход за левый кран экрана
        if self.x <= self.r:
            # летел налево - полетел направо
            self.speed_x=-self.speed_x
        if self.x>= SCREEN_WIDTH - self.r:
            #летел направо - полетел налево
            self.speed_x=-self.speed_x
            #выход за верхний край
        if self.y<=self.r:
            #летел наверх-полетел вниз
            self.speed_y=-self.speed_y
            #выход за нижний край

