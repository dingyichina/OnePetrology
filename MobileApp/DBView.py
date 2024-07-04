'''
    显示单个数据库的界面

    add by dingyi
    -- 20240513
    todo : 把它放在其它目录中，无法访问到assets中的资源。。。原因不明
'''
import flet as ft

from Model import DatabaseModel
# from service import cms


class DBThumbnail(ft.Card):

    def __init__(self,model:DatabaseModel):
        super().__init__()
        self.model = model


    @property
    def display(self):
        self.content = ft.Container(
                content=ft.Column(
                    [
                        ft.Row(
                            controls=[
                                ft.Image(src=self.model.cover, width=300, height=200, fit=ft.ImageFit.SCALE_DOWN)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Row(
                            controls=[

                                    ft.ListTile(
                                        leading=ft.Icon(ft.icons.TITLE),
                                        title=ft.Text(self.model.title,width=340,selectable=True),
                                        subtitle=ft.Text(
                                            self.model.description,max_lines=3,width=340,selectable=True
                                        ),width=340
                                    ),

                                ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            width = 340
                         ),

                        ft.Row(
                            [ft.Icon(ft.icons.MAN), ft.Text(self.model.author,selectable=True,width=340)],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        ft.Row(
                            [ft.Icon(ft.icons.MAIL), ft.Text(self.model.owner,selectable=True,width=340)],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        ft.Row(
                            [ft.Icon(ft.icons.ALL_INBOX), ft.Text("{} records".format(self.model.total_count),selectable=True,color=ft.colors.RED)],
                            alignment=ft.MainAxisAlignment.START,
                        ),
                        ft.Row(
                            [ft.Icon(ft.icons.TEXT_FIELDS),
                             ft.Text(value=','.join(self.model.field_list),max_lines=3,theme_style=ft.TextThemeStyle.BODY_SMALL,selectable=True,width=340)],
                            alignment=ft.MainAxisAlignment.START,
                        width=300),

                    ]
                ),
                width=400,
                padding=10,


            )
        return self

# async def main(page: ft.Page):
#     page.title = "Database View"
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#
#     # model = DatabaseModel("Igneous rock map of the world", "Dingyi", "This is a map of the world", "/images/worldmap.gif", "geowind@126.com")
#     # page.add(DBThumbnail(model).display)
#     grid = ft.GridView(
#         expand=1,
#         runs_count=5,
#         max_extent=500,
#         child_aspect_ratio=0.75,
#         spacing=5,
#         run_spacing=5,
#     )
#
#     page.add(grid)
#     async def getview():
#
#         # 访问cms，罗列所有的专题库
#         list =await cms.get_subject_list()
#         for l in list:
#             model = DatabaseModel("Igneous rock map of the world", "Dingyi", "This is a map of the world", "/images/worldmap.gif", "geowind@126.com").from_json(l)
#             # print(model)
#             await  model.get_info()
#             grid.controls.append(DBThumbnail(model).display)
#     await getview()
#     page.update()
#
#
# ft.app(target=main)
