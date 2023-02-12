import pygame
import sys
from config_2 import *
from bat_br import Bat
from ball_br import Ball
from brick import Brick
from brick_row import BrickRow

def point_in_rect(px,py,rect_x,rect_y,rect_w,rect_h):
    inx=rect_x<=px<=rect_x+rect_w
    iny=rect_y<=py<=rect_y+rect_h
    return inx and iny
def ball_hit_bricks(ball_br,brick_row):
    mid_leftx=ball_br.x-ball_br.r
    mid_lefty=ball_br.y
    mid_rightx=ball_br.x+ball_br.r
    mid_righty=ball_br.y
    mid_topx=ball_br.x
    mid_topy=ball_br.y-ball_br.r
    mid_bottomx=ball_br.x
    mid_bottomy=ball_br.y+ball_br.r
    for brick in brick_row.row:
        if point_in_rect(mid_topx,mid_topy,brick.x,brick.y,BRICK_WIDTH,BRICK_HEIGHT):
            brick_row.row.remove(brick)
            ball_br.speed_y=-ball_br.speed_y
            if brick.color==RED:
                ball_br.left_score+=7
            elif brick.color==ORANGE:
                ball_br.left_score+=5
            elif brick.color==GREEN:
                ball_br.left_score+=3
            elif brick.color==YELLOW:
                ball_br.left_score+=1  
            break
        if point_in_rect(mid_leftx,mid_lefty,brick.x,brick.y,BRICK_WIDTH,BRICK_HEIGHT):
            brick_row.row.remove(brick)
            ball_br.speed_y=-ball_br.speed_y
            if brick.color==RED:
                ball_br.left_score+=7
            elif brick.color==ORANGE:
                ball_br.left_score+=5
            elif brick.color==GREEN:
                ball_br.left_score+=3
            elif brick.color==YELLOW:
                ball_br.left_score+=1
            break    
        if point_in_rect(mid_bottomx,mid_bottomy,brick.x,brick.y,BRICK_WIDTH,BRICK_HEIGHT):
            brick_row.row.remove(brick)
            ball_br.speed_y=-ball_br.speed_y
            if brick.color==RED:
                ball_br.left_score+=7
            elif brick.color==ORANGE:
                ball_br.left_score+=5
            elif brick.color==GREEN:
                ball_br.left_score+=3
            elif brick.color==YELLOW:
                ball_br.left_score+=1
            break  
        if point_in_rect(mid_rightx,mid_righty,brick.x,brick.y,BRICK_WIDTH,BRICK_HEIGHT):
            brick_row.row.remove(brick)
            ball_br.speed_y=-ball_br.speed_y
            if brick.color==RED:
                ball_br.left_score+=7
            elif brick.color==ORANGE:
                ball_br.left_score+=5
            elif brick.color==GREEN:
                ball_br.left_score+=3
            elif brick.color==YELLOW:
                ball_br.left_score+=1
            break

            
game_state=0
bat_br=Bat()
ball_br=Ball()
brick_row=BrickRow()
clock = pygame.time.Clock()
sc = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.font.init()
f2 = pygame.font.SysFont('algerian', 48)
f3 = pygame.font.SysFont('algerian', 210)
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if ball_br.y>=SCREEN_HEIGHT - ball_br.r*2:
        game_over=f3.render(("GAME OVER"), True,(WHITE))
        sc.blit(game_over, (400 ,500))
        pygame.display.update()
    else:
        bat_br.update()
        ball_br.update()

        mid_leftx=ball_br.x-ball_br.r
        mid_lefty=ball_br.y

        mid_rightx=ball_br.x+ball_br.r
        mid_righty=ball_br.y

        mid_topx=ball_br.x
        mid_topy=ball_br.y-ball_br.r

        mid_bottomx=ball_br.x
        mid_bottomy=ball_br.y+ball_br.r
                #верхняя граница ракетки №1
        if point_in_rect(mid_bottomx,mid_bottomy,bat_br.x,bat_br.y,BAT_WIDTH,BAT_HEIGHT):
            ball_br.speed_y=-ball_br.speed_y
        for i in range(len(brick_row.row)):
            if point_in_rect(mid_topx,mid_topy,brick_row.row[i].x,brick_row.row[i].y,BAT_WIDTH,BAT_HEIGHT):
                ball_br.speed_y=-ball_br.speed_y
                #проверка столкновений мяча с кирпичами
        ball_hit_bricks(ball_br,brick_row)


        score_left_text = f2.render(str(ball_br.left_score), True,(YELLOW))
        sc.fill(BLACK)
        pygame.draw.rect(sc, WHITE,(bat_br.x,bat_br.y,BAT_WIDTH,BAT_HEIGHT))
        pygame.draw.circle(sc, ORANGE,(ball_br.x, ball_br.y), ball_br.r)
        for i in range(8):
            for brick in brick_row.row:
                pygame.draw.rect(sc, BLACK,(brick.x,brick.y,BRICK_WIDTH,BRICK_HEIGHT),1)
                pygame.draw.rect(sc, brick.color,(brick.x+1,brick.y+1,BRICK_WIDTH-1,BRICK_HEIGHT-1))

        sc.blit(score_left_text, (SCREEN_WIDTH//2 -100, 10))
        clock.tick(FPS)
        pygame.display.update()
