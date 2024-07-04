import flet as ft
'''
    论文主视图，
    显示在线资源，岩浆岩资源库资源，本地资源
    
    add by dingyii
    
    2024-05-10

'''


class PaperControl(ft.Column):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.controls =[]
        self.display()
        pass

    def display(self):
        self.controls = [
            # 暂时用tab来显示主库和专题库
            ft.Tabs(
                selected_index=1,
                animation_duration=300,
                tabs=[
                    ft.Tab(
                        icon=ft.icons.AIR,
                        text="Online Papers",
                        content=ft.Container(
                            content=ft.WebView(
                                url="https://www.sciencedirect.com/",
                                expand=True,
                                on_page_started=lambda _: print("Page started"),
                                on_page_ended=lambda _: print("Page ended"),
                                on_web_resource_error=lambda e: print("Page error:", e.data),
                            )
                        ),
                    ),

                    ft.Tab(
                        text="OnePetrology",
                        icon=ft.icons.GRID_3X3,
                        content=ft.Container(
                            content=ft.WebView(
                                url="https://petrology.deep-time.org/dspace/collections/c04dce5a-2f71-4ef9-a872-b55f290511d2",
                                expand=True,
                                on_page_started=lambda _: print("Page started"),
                                on_page_ended=lambda _: print("Page ended"),
                                on_web_resource_error=lambda e: print("Page error:", e.data),
                            )
                        ),
                    ),
                    ft.Tab(
                        icon=ft.icons.LOCAL_BAR,
                        text="Local",
                        # tab_content=ft.Icon(ft.icons.SEARCH),
                        content=ft.Text("local files  coming soon ..."),
                    ),
                ],
                expand=1,
            )

        ]

        return self

