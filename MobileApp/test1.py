import time
from math import pi

import flet
from flet import Column, Icon, Page, Text, icons

from controls.collapsible import Collapsible
from controls.menu_button import MenuButton


def main(page: Page):

    page.scroll = "auto"
    page.add(
        Column(
            [
                flet.Text('2222'),
                Collapsible(
                    "Buttons",
                    icon=Icon(icons.SMART_BUTTON),
                    content=Column(
                        [
                            MenuButton("Basic buttons"),
                            MenuButton("Floating action button"),
                            MenuButton("Popup menu button", selected=True),
                        ],
                        spacing=3,
                    ),
                ),
                Collapsible(
                    "Simple apps",
                    icon=Icon(icons.NEW_RELEASES),
                    content=Column(
                        [
                            MenuButton("Basic buttons"),
                            MenuButton("Floating action button"),
                            MenuButton("Popup menu button", selected=True),
                        ],
                        spacing=3,
                    ),
                ),
                Collapsible(
                    "Forms",
                    icon=Icon(icons.DYNAMIC_FORM),
                    content=Column(
                        [
                            MenuButton("Basic buttons"),
                            MenuButton("Floating action button"),
                            MenuButton("Popup menu button", selected=True),
                        ],
                        spacing=3,
                    ),
                ),
            ],
            spacing=3,
            width=1230,
            expand=True,
        )
    )
    page.update()


flet.app( target=main, view=flet.FLET_APP)  #