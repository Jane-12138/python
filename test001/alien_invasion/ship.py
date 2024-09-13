import pygame
#ship模块，设置和管理飞船元素

class Ship():
    #初始化飞船并设置飞船初始位置，需要传入屏幕对象
    def __init__(self,screen) -> None:
        self.screen=screen

        #加载飞船图像
        self.ship_image=pygame.image.load('test001/alien_invasion/images/capture.bmp')

        #获取飞船图像的矩形属性和屏幕的矩形属性
        self.ship_rect=self.ship_image.get_rect()
        self.screen_rect=self.screen.get_rect()

         #设置飞船矩形的位置为，屏幕的x中央、屏幕的底部
        self.ship_rect.centerx=self.screen_rect.centerx
        self.ship_rect.bottom=self.screen_rect.bottom

    #将飞船图像绘制到屏幕上，blit（绘制图像，指定绘制位置）：将指定图像绘制到指定位置
    def blitship(self):
        self.screen.blit(self.ship_image,self.ship_rect)


