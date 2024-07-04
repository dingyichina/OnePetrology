import flet as ft


class MapItem:
    def __init__(self, name, cn_name, icon, url):
        self.name = name
        self.cn_name = cn_name
        self.url = url
        self.icon = icon
        self.is_selected = False


class MapControl(ft.Column):
    def __init__(self):
        super().__init__()
        self.expand = True  #

        self.map_list = [
            MapItem(name="Igneous rock map of the world",
                    cn_name="全球岩浆岩图，2D",
                    icon=ft.icons.MAP,
                    url="https://petrology.deep-time.org/app/worldmap.html"),
            MapItem(name="3D Earth and Igneous rock map of the world",
                    cn_name="全球岩浆岩图，3D",
                    icon=ft.icons.MAP,
                    url="https://petrology.deep-time.org/app/3dmap.html"),
            MapItem(name="Igneous rock map of asia",
                    cn_name="亚洲岩浆岩图",
                    icon=ft.icons.MAP,
                    url="https://petrology.deep-time.org/app/asia.html"),
            MapItem(name="Recently published igneous maps ",
                    cn_name="最近出版的岩浆岩系列图件",
                    icon=ft.icons.MAP,
                    url="https://petrology.deep-time.org/app/publishmaps.html"),
        ]
        self.cur_map_index = 0
        # 此时就构建好右侧滑动抽屉
        self.end_drawer = ft.NavigationDrawer(
            # on_dismiss=end_drawer_dismissed,
            on_change=self.drawer_change,
            controls=[
                # ft.NavigationDrawerDestination(
                #     icon=ft.icons.ADD_TO_HOME_SCREEN_SHARP, label="项1"
                # ),
                # ft.NavigationDrawerDestination(icon=ft.icons.ADD_COMMENT, label="项2"),
            ],
        )
        for i in range(len(self.map_list)):
            self.end_drawer.controls.append(
                ft.NavigationDrawerDestination(
                    icon=self.map_list[i].icon, label=self.map_list[i].name
                )
            )
        self.controls = [

        ]
        self.cache = {}
        self.display()

    def drawer_change(self, e):
        print(e.control.selected_index)
        if e.control.selected_index == self.cur_map_index:
            return  # 没有改变
        self.cur_map_index = e.control.selected_index
        self.page.close_end_drawer()
        # 刷新地图
        self.display()
        self.page.update()

    def display(self):
        self.controls = [
            ft.Row([ft.Text(self.map_list[self.cur_map_index].name,),
                    ft.ElevatedButton("more maps", on_click=self.showmaplist)], wrap=True),
            self.get_cur_map_view(),
        ]
        return self

    def showmaplist(self, e):
        # 用右侧滑出的drawer来显示列表
        # print(e)
        self.page.show_end_drawer(self.end_drawer)
        # 此时是否需要调用page的update呢？  todo
        pass

    def get_cur_map_view(self):
        if not self.map_list[self.cur_map_index].url in self.cache:
            self.cache[self.map_list[self.cur_map_index].url] = ft.WebView(  # 浏览器，
                self.map_list[self.cur_map_index].url,
                expand=True,
                on_page_started=lambda _: print("Page started"),
                on_page_ended=lambda _: print("Page ended"),
                on_web_resource_error=lambda e: print("Page error:", e.data),
            )
        return self.cache[self.map_list[self.cur_map_index].url]
