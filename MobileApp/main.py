import flet as ft

from OnePetrologyApp import OnePetrologyApp
from controls.AudioCtrl import AudioCtrl
import logging

logging.basicConfig(level=logging.INFO)


def main(page: ft.Page):
    page.title = "DDE OnePetrology"
    page.tooltip = "DDE OnePetrology by dingyi"

    def route_change(e):
        # if e.route == "/" or e.route == "database":
        #     mainview.database()
        # elif e.route == "/map":
        #     mainview.map()
        # elif e.route == "/papers":
        #     mainview.paper()
        # elif e.route == "/profile":
        #     mainview.profile()
        # # elif e.route == "/audiorecord":
        # #     mainview.audio_recorder()
        # else:
        #     print(e.route, " 没有处理的路由")

        # print(e)
        page.go(e.route)

    # model =  build_sys_model()
    # page.model = model
    mainview = OnePetrologyApp(page)

    page.add(mainview)
    # lm = LayoutManager(page, mainview)
    page.on_route_change = route_change

    # print(f"Initial route: {page.route}")
    logging.getLogger("flet_core").info("Initial route: %s", page.route)
    page.go(page.route)

    # 添加语音识别功能
    audio_rec = AudioCtrl(page)
    page.overlay.append(audio_rec)


logging.getLogger("flet_core").setLevel(logging.INFO)
ft.app(main, view=ft.AppView.WEB_BROWSER, port=8080)#)#,
