import flet as ft

from controls.Login import Login


class SettingControl(ft.Column):
    def __init__(self,page:ft.Page):
        super().__init__()
        self.page = page
        self.expand = True
        self.controls = []

        self.display()
    def display(self):
        self.controls = [
            ft.ExpansionTile(
                leading=ft.Icon(ft.icons.INFO_OUTLINE),
                title=ft.Text("General Information"),
                subtitle=ft.Text("introduce dde one petrology"),
                affinity=ft.TileAffinity.PLATFORM,
                maintain_state=True,
                # collapsed_text_color=ft.colors.RED,
                # text_color=ft.colors.RED,
                controls=[ft.ListTile(title=ft.Text("Thank you very much for using the mobile app DDEOnePetrology. It is part of DDE OnePetrology and was developed by the team led by Professor Wang Tao from the Institute of Geology, Chinese Academy of Geological Sciences. We welcome you to use it and provide your valuable suggestions.")),
                          ft.ExpansionTile(
                              # leading=ft.Icon(ft.icons.CALL_MISSED_OUTGOING_ROUNDED),
                              affinity=ft.TileAffinity.LEADING,
                              collapsed_text_color=ft.colors.BLUE,
                              text_color=ft.colors.BLUE,
                              title=ft.Text("Our Mission:"),
                              controls=[ft.ListTile(title=ft.Text("    1.To identify, augment, and network globally distributed petrological and geochemical databases for rocks (magmatic rocks) to be accessed via the DDE as a sharing, service-oriented platform that supports access to in-depth mining and comprehensive analysis tools, with the goal to solve a number of major basic geological problems by using big data analysis.")),
                                    ft.ListTile(title=ft.Text("    2. Elucidating the 3D architecture and evolution (4D) of deep-earth materials from regional, orogenic to global scales through analysis of the evolution of magmatic rocks;")),
                                    ft.ListTile(title=ft.Text("    3.Providing evidence for deep-time plate reconstruction, continental assemblage processes, and paleogeographic reconstruction and revealing the growth and evolution of crust and mantle;")),
                                    ft.ListTile(title=ft.Text("    4. Revealing the deep-earth dynamics and understanding mechanisms how the earth's deep engine works, including fluid and magma movement, material exchange from core to crust and the mechanisms of tectonic plate movement and supercontinent cyclicity.")),
                            ]),



                          ft.Row(controls=[ft.Text(
                              "More information please visit our site. "),ft.Chip(
                                                    label=ft.Text("https://petrology.deep-time.org/"),
                                                    leading=ft.Icon(ft.icons.WEB),
                                                    bgcolor=ft.colors.GREEN_200,
                                                    on_click=self.open_site,
                                                )

                          ]),
                    ]

            ),
            ft.ExpansionTile(
                leading=ft.Icon(ft.icons.LOGIN_OUTLINED),
                title=ft.Text("Login"),
                subtitle=ft.Text("login for OnePetrology"),
                affinity=ft.TileAffinity.PLATFORM,
                maintain_state=True,
                # collapsed_text_color=ft.colors.RED,
                # text_color=ft.colors.RED,
                controls=[ ft.Container(padding=ft.padding.only(top=10),content=Login(self.page))],
            ),
            ft.ExpansionTile(
                leading=ft.Icon(ft.icons.SETTINGS),
                title=ft.Text("Settings"),
                subtitle=ft.Text("Setting for OnePetrology"),
                affinity=ft.TileAffinity.PLATFORM,
                maintain_state=True,
                # collapsed_text_color=ft.colors.RED,
                # text_color=ft.colors.RED,
                controls=[ft.Text("function is coming soon...")],
            ),


        ]

        return self

    def open_site(self,e):
        self.page.launch_url("https://petrology.deep-time.org/")
        self.page.update()

    def handle_expansion_tile_change(self,e):

        print(e.control.title.value)

        # self.page.show_snack_bar(
        #     ft.SnackBar(ft.Text(f"ExpansionTile was {'expanded' if e.data == 'true' else 'collapsed'}"), duration=1000)
        # )
        # if e.control.trailing:
        #     e.control.trailing.name = (
        #         ft.icons.ARROW_DROP_DOWN
        #         if e.control.trailing.name == ft.icons.ARROW_DROP_DOWN_CIRCLE
        #         else ft.icons.ARROW_DROP_DOWN_CIRCLE
        #     )
        # self.page.update()
