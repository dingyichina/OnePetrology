import flet as ft

from controls.DatabaseControl import DatabaseControl
from controls.MapControl import MapControl
from controls.PaperControl import PaperControl
from controls.SettingControl import SettingControl


class OnePetrologyApp(ft.Row):

    def __init__(self,page:ft.Page):
        super().__init__(expand=True)
        self.page = page
        self.controls = [

        ]
        self.mapview = MapControl()
        self.database_view = DatabaseControl(page)
        self.paper_view = PaperControl()
        self.profile_view = SettingControl(page)

        self.page.appbar = ft.AppBar(
            leading=ft.Image(src="/images/DDE-logo.png"),
            leading_width=40,
            title=ft.Text("OnePetrology"),  # ft.Row([ft.Image(src="/images/DDE-logo.png"),ft.Text("OnePetrology")]),
            center_title=True,
            bgcolor=ft.colors.SURFACE_VARIANT,
            actions=[
                ft.IconButton(icon=ft.icons.CROP_ROTATE, on_click=self.crop_rotate),
                ft.IconButton(
                    icon=ft.icons.BRIGHTNESS_2,
                    tooltip="Toggle brightness",
                    on_click=self.theme_changed,
                ),
                # ft.IconButton(icon=ft.icons.MORE_VERT),
            ],
        )
        self.page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.icons.DATASET, label="Database"),
                ft.NavigationDestination(icon=ft.icons.MAP, label="Maps"),
                ft.NavigationDestination(
                    icon=ft.icons.BOOKMARK,
                    label="Papers",
                ),
                ft.NavigationDestination(
                    icon=ft.icons.SETTINGS_APPLICATIONS, label="Profile",
                ),
            ], on_change=self.navi_change
        )
        # 横屏的rail
        self.rail = ft.NavigationRail(
            selected_index=0,
            label_type=ft.NavigationRailLabelType.ALL,
            # extended=True,
            min_width=100,
            min_extended_width=400,
            # leading=ft.Image(src="assets/images/DDE-logo.png",fit=ft.ImageFit.SCALE_DOWN,width=50),
            group_alignment=-0.9,
            destinations=[
                ft.NavigationRailDestination(
                    icon=ft.icons.DATASET, label="Database"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.MAP, label="Maps"
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.BOOKMARK, label="Papers",
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.SETTINGS_APPLICATIONS, label="Profile",
                ),
                ft.NavigationRailDestination(
                    icon=ft.icons.CROP_ROTATE, label="Rotate", padding=ft.padding.only(top=20),
                ),

            ],
            on_change=self.navi_change,
        )
        self.page.on_resize = self.on_resize
        self.cur_view = self.database_view
        self.is_portrait = True
        self.refresh_main_view()

    def theme_changed(self,e):
        if e.control.icon == ft.icons.BRIGHTNESS_2:
            self.page.theme_mode = ft.ThemeMode.DARK
            e.control.icon = ft.icons.BRIGHTNESS_HIGH
        else:
            self.page.theme_mode = ft.ThemeMode.LIGHT
            e.control.icon = ft.icons.BRIGHTNESS_2
        self.page.update()
    def crop_rotate(self,e):
        self.is_portrait = not self.is_portrait
        self.refresh_main_view()

    # 刷新
    def  refresh_main_view(self):
        if not self.is_portrait:
            # 横屏
            # 此时采用左侧导航
            self.controls = [
                self.rail,
                ft.VerticalDivider(width=1),
                self.cur_view,
            ]
            self.page.navigation_bar.visible = False
            self.page.appbar.visible = False
            self.page.update()

        else:
            # 竖屏
            # self.page.controls.clear()
            self.controls = [self.cur_view]
            # self.page.controls.append(self.main_view)
            self.page.navigation_bar.visible = True
            self.page.appbar.visible = True

        self.page.update()
    def navi_change(self,e):
        if e.control.selected_index == 0:
            self.cur_view = self.database_view
            self.refresh_main_view()
        elif e.control.selected_index == 1:
            self.cur_view = self.mapview
            self.refresh_main_view()
        elif e.control.selected_index == 2:
            self.cur_view = self.paper_view
            self.refresh_main_view()
        elif e.control.selected_index == 3:
            self.cur_view = self.profile_view
            self.refresh_main_view()
        if e.control.selected_index == 4:  # 临时处理，非常不妥当，后期再改 todo
            self.crop_rotate(e)



    def on_resize(self,e):
        if self.page.window_width > self.page.window_height:
            self.is_portrait = False
            self.crop_rotate(e)

        else:
           self.is_portrait = True
           self.crop_rotate(e)
    # def audio_recorder(self):
    #     self.controls = [
    #         ft.Text("audio_recorder coming soon"),
    #     ]
