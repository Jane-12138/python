import pygame
import sys

def event_check():
    for event in pygame.event.get():
            #处理特殊事件,事件类型为退出事件
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    moveflag == True



def update_screen(screen,settings,ship):
        #设置屏幕背景色,传入rgb带括号
        screen.fill(settings.screen_color)

        #绘制飞船到屏幕上
        ship.blitship()
        
        #更新屏幕，显示元素新位置
        pygame.display.flip()