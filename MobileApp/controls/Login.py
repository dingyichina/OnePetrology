'''

    登录界面及业务逻辑


    dingyi
    20240521

'''
import threading

import flet as ft

from DSpace7RestClient import DspaceRestClient


class Login(ft.Column):

    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        # 设置横竖都居中
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        # 从客户端存储中获取登录状态
        if self.page.client_storage.get("onepetrology.has_login") is None or self.page.client_storage.get(
                "has_login") is False:
            self.has_login = False
            self.cur_person = ""
        else:
            self.has_login = True
            # 此时需要继续读取已登录后的信息
            if self.page.client_storage.get("onepetrology.cur_person") is not None:
                self.cur_person = self.page.client_storage.get("onepetrology.cur_person")
            else:
                self.cur_person = ""

        if self.page.client_storage.get("onepetrology.remember_me") or self.page.client_storage.get(
                "remember") is False:
            self.remember_me = False
            self.user_name = ""
            self.password = ""
        else:
            self.remember_me = True
            # 继续检查是否已记忆用户名和密码
            if self.page.client_storage.get("onepetrology.user_name") is not None:
                self.user_name = self.page.client_storage.get("onepetrology.user_name")
            else:
                self.user_name = ""
            if self.page.client_storage.get("onepetrology.password") is not None:
                self.password = self.page.client_storage.get("onepetrology.password")  # 此处需要解密，密码应该是密钥存储 todo
            else:
                self.password = ""

        # 构造基础界面元素
        self.ui_user_name = ft.TextField(label="User Name", value=self.user_name, icon=ft.icons.ACCOUNT_CIRCLE,keyboard_type=ft.KeyboardType.EMAIL)
        self.ui_password = ft.TextField(label="Password", value=self.password, password=True, can_reveal_password=True,
                                        icon=ft.icons.PASSWORD)
        self.ui_remember = ft.Switch(label="Remember", value=self.remember_me, on_change=self.do_remember)
        # print(self.has_login)
        # self.page.client_storage.set("has_login", False)

        self.width = 300  # 限制宽度

        # 根据读取结果判断该显示什么内容
        if self.has_login and self.cur_person is not None:
            # 下面是登陆后的内容
            self.show_user_info()
        else:
            # 显示登录界面
            self.show_login()

    def did_mount(self):
        print("login mount ")

    def will_unmount(self):
        self.running = False

        print("login unmount ")

    def back_job(self):
        # 读取本地文件，看看是否已登录
        if not self.running:
            return
        self.user_name = self.ui_user_name.value
        self.password = self.ui_password.value  # 此时从界面直接读的，不需要解密
        client = DspaceRestClient()
        try:
            client.getToken()
            client.login(self.user_name, self.password)
            self.cur_person = client.getEPersonByEmail("geowind@126.com").get_full_name()
            # 此时显示登录后的内容
            self.show_user_info()
            self.page.client_storage.set("onepetrology.has_login",True)
            self.page.client_storage.set("onepetrology.cur_person",self.cur_person)
            self.update()
        except Exception as e:
            # 显示错误信息
            self.show_error(e)

    def show_error(self, e):

        self.controls = [
            ft.Text(e, color=ft.colors.RED),
            ft.ElevatedButton("Retry", on_click=self.do_retry),
        ]
        self.update()

    def do_retry(self, e):
        self.show_login()
        self.update()

    def do_remember(self, e):
        print("remember", e.control.value)
        if e.control.value:  # 此时记住
            self.page.client_storage.set("onepetrology.remember_me", True)
            self.page.client_storage.set("onepetrology.user_name", self.ui_user_name.value)
            self.page.client_storage.set("onepetrology.password", self.ui_password.value)  # 此时需要先加密 todo
            print("saved !")
        else:
            self.page.client_storage.set("onepetrology.remember_me", False)
            self.page.client_storage.set("onepetrology.user_name", "")
            self.page.client_storage.set("onepetrology.password", '')
            print("cleared !")

    def open_site(self, e):
        self.page.launch_url("https://petrology.deep-time.org/")
        self.page.update()

    def do_logout(self, e):
        # 清除本地缓存
        self.page.client_storage.set("onepetrology.remember_me", False)
        self.page.client_storage.set("onepetrology.user_name", '')
        self.page.client_storage.set("onepetrology.password", '')
        self.page.client_storage.set("onepetrology.has_login", False)
        self.page.client_storage.set("onepetrology.cur_person", '')
        self.show_login()
        self.update()

    def do_login(self, e):
        print("login")
        if self.ui_user_name.value.strip() == "":
            self.page.banner = ft.Banner(
                bgcolor=ft.colors.AMBER_100,
                leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
                content=ft.Text(
                    "Username is empty,please input it?"
                ),
                actions=[
                    ft.TextButton("Retry", on_click=self.close_banner),

                ],
            )
            self.page.banner.open = True
            self.page.update()
            return
        if self.ui_password.value.strip() == "":
            self.page.banner = ft.Banner(
                bgcolor=ft.colors.AMBER_100,
                leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
                content=ft.Text(
                    "password is empty,please input it?"
                ),
                actions=[
                    ft.TextButton("Retry", on_click=self.close_banner),
                ],
            )
            self.page.banner.open = True
            self.page.update()
            return
        # 检测是否有没有关闭的banner
        if hasattr(self.page, "banner") and self.page.banner is not None:
            self.page.banner.open = False
            self.page.update()
        if self.ui_remember.value:
            # 记录用户名和密码
            self.page.client_storage.set("onepetrology.remember_me", True)
            self.page.client_storage.set("onepetrology.user_name", self.ui_user_name.value)
            self.page.client_storage.set("onepetrology.password", self.ui_password.value)  # 此时需要先加密 todo
        # 执行登录动作，获取返回信息，然后记录到本地
        # 显示进度条，然后启动线程
        self.controls = [
            ft.ProgressRing(),
            ft.Text("Logging to server ..."),

        ]
        self.update()
        self.running = True
        self.th = threading.Thread(target=self.back_job, args=(), daemon=True)
        self.th.start()

    def close_banner(self, e):
        self.page.banner.open = False
        self.page.update()

    def show_login(self):
        self.controls = [self.ui_user_name,
                         self.ui_password,
                         ft.Row(alignment=ft.MainAxisAlignment.END,
                                controls=[ft.Container(
                                    content=self.ui_remember,
                                    padding=ft.padding.only(left=40)),
                                    ft.Container(
                                        content=ft.ElevatedButton("Login", icon=ft.icons.LOGIN, on_click=self.do_login),
                                        padding=ft.padding.only(right=50, left=10))
                                ]),
                         ]

    def show_user_info(self):
        self.controls = [
            ft.Row([ft.Text("Hello,"),
            ft.Text(self.cur_person, color=ft.colors.BLUE_400),
            ft.Text("  ,Welcome to DDE OnePetrology, you can visit our site for full functions ",max_lines=3,width=200),]),
            ft.Chip(
                label=ft.Text("https://petrology.deep-time.org/"),
                leading=ft.Icon(ft.icons.WEB),
                bgcolor=ft.colors.GREEN_200,
                on_click=self.open_site,
            ),
            ft.Row([
                ft.Text("  ,or logout for some reason."), ft.Chip(
                    label=ft.Text("Logout"),
                    leading=ft.Icon(ft.icons.LOGOUT),
                    # bgcolor=ft.colors.GREEN_200,
                    on_click=self.do_logout,
                ),
            ])

        ]


# def main(page: ft.Page):
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.add(
#         Login(page)
#     )
#
#
# ft.app(target=main)
