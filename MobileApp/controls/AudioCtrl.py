'''

   语音识别组件，调用百度语音识别API
   暂时用浮动button实现，用对话框显示结果


   --by dingyi
   20240509


'''

import flet as ft

from AudioASR import AudioASR
from Clock import Clock


class AudioCtrl(ft.AudioRecorder):

    def __init__(self,page):
        super().__init__(audio_encoder=ft.AudioEncoder.WAV,
        on_state_changed=self.handle_state_change,
        sample_rate=16000,
        channels_num=1)
        # 全局对象
        self.asr = AudioASR()
        self.page = page
        # 暂时使用浮动按钮实现
        self.page.floating_action_button = ft.FloatingActionButton(
            icon=ft.icons.KEYBOARD_VOICE, on_click=self.audio_recorder_result, bgcolor=ft.colors.LIME_300
        )

    def handle_state_change(self,e):
        print(f"State Changed: {e.data}")

    def audio_recorder_result(self,e):
        print("处理录音", e.control)
        if self.page.floating_action_button.icon == ft.icons.KEYBOARD_VOICE :
            # 启动录音功能
            self.page.floating_action_button.icon = ft.icons.STOP

            self.page.update()
            self.start_recording(self.asr.gen_file_path())
        else:
            # 停止录音
            self.page.floating_action_button.icon = ft.icons.KEYBOARD_VOICE
            self.page.splash = None
            self.page.update()
            output_path = self.stop_recording()
            print(f"StopRecording: {output_path}")
            if output_path is None:

                pass
            else:
                self.asr.audio_list.append(output_path) # 添加到列表中
                # 并调用百度api进行解析
                self.asr.do_asr(output_path)
                # 录音解析完成后弹出对话框
                # 显示识别结果对话框
                dlg = ft.AlertDialog(
                    title=ft.Text("Chat with OnePetrology"),
                    content=self.asr.display()
                    , on_dismiss=lambda e: print("对话框已关闭！")
                )
                self.page.dialog = dlg
                dlg.open = True
                self.page.update()

