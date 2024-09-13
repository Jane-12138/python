#12-1 蓝色天空 ：创建一个背景为蓝色的Pygame窗口。
'''12-2 游戏角色 ：找一幅你喜欢的游戏角色位图图像或将一幅图像转换为位图。创建一个类，将该角色绘制到屏幕中央，
并将该图像的背景色设置为屏幕背景色，或将屏幕背景色设置为该图像的背景色。

12-3 火箭 ：编写一个游戏，开始时屏幕中央有一个火箭，而玩家可使用四个方向键上下左右移动火箭。请务必确保火箭不会移到屏幕外面。
12-4 按键 ：创建一个程序，显示一个空屏幕。在事件循环中，每当检测到pygame.KEYDOWN 事件时都打印属性event.key 。运行这个程序，并按各种键，看看
Pygame如何响应

'''
import pygame
import sys
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #初始化游戏设置
    pygame.init()
    settings=Settings()
    #设置游戏屏幕大小,注意是传入带括号的数组
    screen=pygame.display.set_mode((settings.screen_width,settings.screen_hight))
    #设置游戏窗口名
    pygame.display.set_caption('外星人飞船')

    #创建飞船实例
    ship=Ship(screen)

    #开始游戏主循环
    while True:
        #监听键盘鼠标事件
        gf.event_check()
        
        #更新屏幕
        gf.update_screen(screen,settings,ship)
        

run_game()