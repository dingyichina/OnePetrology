'''

     实现一个类似微信掼蛋游戏的倒计时clock组件
     倒计时读秒，最多支持99秒

     --add  by dingyi
     20240512

'''
import math
import threading
import time

import flet as ft
class Clock(ft.Stack):

    def __init__(self,seconds=30,tipseconds=20,handler=None):
        super().__init__()
        self.seconds = seconds
        self.tipseconds = tipseconds  # 开始抖动的提醒时间
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.step =  0.125  # 为了保证协调，最好是1或者1的能被2或者4等分，数值越少，抖动的时候频率越高
        self.count = 0
        self.img = ft.Image(src="/clock.png", width=50, height=50, fit=ft.ImageFit.CONTAIN,rotate = ft.transform.Rotate(0, alignment=ft.alignment.center),animate_rotation = ft.animation.Animation(round(self.step*1000/3), ft.AnimationCurve.BOUNCE_OUT),)
        self.txt = ft.Text(value=f"{self.seconds}", top=7,left=12, size=20, weight=ft.FontWeight.BOLD)
        self.controls = [
            self.img,
            self.txt
         ]
        self.__event_handlers = []
        self.add_handler(handler)

        # self.start()
        # 设置动画

    # def start(self,seconds=30,tipseconds=20):
    #     # 启动 timer
    #     self.seconds = seconds
    #     self.tipseconds = tipseconds  # 开始抖动的提醒时间
    #     self.running = True
    #     self.th = threading.Thread(target=self.update_timer, args=(), daemon=True)
    #     self.th.start()

    def update_timer(self):
        while self.seconds and self.running:
            self.seconds -= self.step
            cur_second = math.ceil(self.seconds)
            self.txt.value = "{:02d}".format(cur_second)
            self.txt.update()
            if cur_second > 0:
                # self.timer = threading.Timer(1,self.onTimer)
                # self.timer.start()
                if cur_second == self.tipseconds:
                    self.img.rotate.angle = -math.pi /10  # 旋转角度
                    self.img.update()
                elif cur_second < self.tipseconds:
                    if self.count % 2 ==0:
                        self.img.rotate.angle -= math.pi /5
                    else:
                        self.img.rotate.angle += math.pi /5
                    self.img.update()
            else:
                self.seconds = 0
                self.running = False # 计时结束
                self.img.rotate.angle = 0
                self.img.update()
                # self.timer.cancel()
                # 回调所有的handler
                for h in self.__event_handlers:
                    h()
            self.count +=1  # 循环次数，用来确认左右摇摆
            time.sleep(self.step)

    def did_mount(self):
        self.running = True
        self.th = threading.Thread(target=self.update_timer, args=(), daemon=True)
        self.th.start()
    def will_unmount(self):
        self.running = False



    # 添加计时停止时的回调函数
    def add_handler(self,handler):
        if handler is not None:
            self.__event_handlers.append(handler)



# def main(page: ft.Page):
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     def callback():
#         print("time is out ")
#     def callback2():
#         print("时间到了哈")
#     page.spacing = 30
#     c = Clock(seconds=30,tipseconds=20,handler=callback)
#     c.add_handler(callback2)
#     page.add(
#        c
#     )
#
#
# ft.app(target=main)
