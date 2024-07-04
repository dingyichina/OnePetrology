'''
    语音识别交互数据持有者
    负责缓存所有对话的历史记录

    --- by dingyi

'''
import os
from datetime import datetime
import  flet as ft
from aip import AipSpeech
'''  目前采用百度的语音引擎，效果一般'''
""" 你的 APPID AK SK """
APP_ID = '67832249'
API_KEY = 'Lq2LrRXGNevdUifgPxQdO0TS'
SECRET_KEY = '0WFSWlbOCyh97qxiwueSicW3hKrWvCbD'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

class AudioASR:

    def __init__(self):
        self.audio_list = []
        self.asr_text = []

    def gen_file_path(self):
        # 根据时间生成文件名
        now = datetime.now()
        # 格式化时间戳，生成文件名
        filename = now.strftime("%Y%m%d_%H%M%S") + ".wav"
        self.cur_file = filename
        return filename


    def fail_record(self):
        self.audio_list.append(None)
        self.asr_text.append("fail to record,please check")
    def do_asr(self, file_path):
        # 识别本地文件
        with open(file_path, 'rb') as fp:
             rtn = client.asr(fp.read(), 'wav', 16000)
             self.asr_text.append(rtn)

    def getresult(self,index):
        if index >= len(self.asr_text):
            return "failed ,please check"
        rtn = self.asr_text[index]
        if 'result' not in rtn:
            return "failed ,please check"
        return rtn['result'][0]

    def calcsize(self,index):
        file_size = os.path.getsize(self.audio_list[index])
        return min(file_size/4096, 160)  # 控制最大宽度

    def display(self):
        rtn= ft.ListView(expand=True, spacing=10)

        for i in range(len(self.audio_list)):
            r = ft.Row([
                # 具有图标的头像（即图标与反色背景）
               ft.CircleAvatar(
                    content=ft.Icon(ft.icons.RECORD_VOICE_OVER),

                ),
                ft.Column(
                    [
                        ft.Container(  bgcolor=ft.colors.CYAN_200, padding=5,height=20,width=self.calcsize(i), content=ft.ElevatedButton("..."),
                            ),
                        ft.Text(self.getresult(i),max_lines=10,width=160),
                    ],
                )

            ])
            rtn.controls.append(r)
            # 添加server端的反馈
            r = ft.Row([
               ft.Text("暂时我还无法处理您的要求，我正在努力学习中哦O(∩_∩)O", max_lines=10, width=160),
               ft.Lottie(src=f'https://raw.githubusercontent.com/xvrh/lottie-flutter/master/example/assets/Mobilo/C.json',
                         repeat=True,
                         reverse=False,
                         animate=True)
                 ])
            rtn.controls.append(r)
        return rtn