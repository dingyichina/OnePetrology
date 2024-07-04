import threading

import flet as ft

from DBView import DBThumbnail
from Model import DatabaseModel
from service import cms

'''
    database 的主控页面
    
'''



class DatabaseControl(ft.Column):
    def __init__(self,page: ft.Page):
        super().__init__(expand=True)
        print("DatabaseControl init ")
        self.page = page
        self.expand = True  #
        self.controls = []
        self.grid = ft.GridView(
            expand=1,
            runs_count=5,
            max_extent=500,
            child_aspect_ratio=0.6,
            spacing=5,
            run_spacing=5,
        )
        self.has_loaded_major_db = False
        self.has_loaded_subject_db = False
        self.running = True
        self.th = threading.Thread(target=self.back_job, args=(), daemon=True)
        self.th.start()
        self.display()
    def did_mount(self):
        print("DatabaseControl mount ")

    def will_unmount(self):
        self.running = False

        print("DatabaseControl unmount ")
    def back_job(self):
        if not self.running:
            return
        # 后台线程获取服务端数据
        if  not self.has_loaded_major_db:
            self.major_db = DBThumbnail(DatabaseModel("Igneous rock major database", "Wang tao,Tong ying,Guo lei,ding yi,etc.", "The main database of igneous rocks is based on a knowledge system, with samples as the core, covering various information such as chronology, geochemistry, isotopes, major and trace elements, etc. The data is continuously updated and widely includes relevant data from publicly published journals ",
                                  "/images/worldmap.gif", "geowind@126.com").get_info())
            self.has_loaded_major_db = True

        if not self.has_loaded_subject_db:
            self.get_subject_db()
            self.has_loaded_subject_db = True
        self.display()
        if self.page is not None : # 在当前显示页面中，则刷新，否则不刷新
            self.update()
        print("loading success.")

    def get_major_db(self):
        if self.has_loaded_major_db:
            return self.major_db.display
        else:
            return  ft.Column(
                    [ft.Text(),ft.ProgressRing(), ft.Text("loading from server...")],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,expand=True
                )
    def get_subject_db(self):
        list = cms.get_subject_list()
        for l in list:
            model = DatabaseModel("Igneous rock map of the world", "Dingyi", "This is a map of the world",
                                  "/images/worldmap.gif", "geowind@126.com").from_json(l)
            # print(model)
            model.get_info()
            self.grid.controls.append(DBThumbnail(model).display)
        # self.update()
        return self.grid

    def get_subject_db_view(self):
        if self.has_loaded_subject_db:
            return self.grid
        else:
            return ft.Column(
                [ft.Text(), ft.ProgressRing(), ft.Text("loading from server...")],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True
            )
    def display(self):
        self.controls = [
            # 暂时用tab来显示主库和专题库
            ft.Tabs(
                selected_index=1,
                animation_duration=300,
                tabs=[
                    ft.Tab(
                        icon=ft.icons.HOME,
                        text="Major database",
                        content=ft.SafeArea(
                            content=self.get_major_db()
                        ),
                    ),

                    ft.Tab(
                        text="Thematic databases",
                        icon=ft.icons.FORMAT_LIST_NUMBERED,
                        content=self.get_subject_db_view(),
                        # ft.WebView(  # 浏览器，
                        #     "https://petrology.deep-time.org/app/suject.html",
                        #     expand=True,
                        #     on_page_started=lambda _: print("Page started"),
                        #     on_page_ended=lambda _: print("Page ended"),
                        #     on_web_resource_error=lambda e: print("Page error:", e.data),
                        # ),
                    ),
                    ft.Tab(
                        text="My database",
                        icon=ft.icons.MY_LIBRARY_BOOKS,
                        content=ft.Text("自己的专题库，功能建设中，使用前需要现在profile进行配置"),
                    ),
                    ft.Tab(
                        icon=ft.icons.QUESTION_ANSWER,
                        text="Faq",
                        # tab_content=ft.Icon(ft.icons.SEARCH),
                        content=ft.Text("Faq coming soon ..."),
                    ),
                ],
                expand=1,
            )

        ]

        return self
