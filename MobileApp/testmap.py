import flet as ft

from flet_map import FletMap


def main(page: ft.Page):
    page.add(
        ft.ListView(
            expand=True,
            controls=[
                FletMap(expand=True, latitude=48.966666,
                        longtitude=110.916668, zoom=7, screenView=[8, 4], )
            ]
        ))

    # page.add(ft.FletMap(expand=True))


if __name__ == '__main__':
    # FletMap()
    ft.app(target=main)