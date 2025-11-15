import flet as ft
from sidebar import Sidebar


class AppLayout(ft.Row):
    def __init__(self, app, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.page = page
        self.page.on_resized = self.page_resize
        self.toggle_nav_rail_button = ft.IconButton(
            icon=ft.Icons.ARROW_CIRCLE_LEFT,
            icon_color=ft.Colors.BLUE_GREY_400,
            selected=False,
            selected_icon=ft.Icons.ARROW_CIRCLE_RIGHT,
            selected_icon_color=ft.Colors.BLUE_GREY_400,
            on_click=self.toggle_nav_rail,
        )
        self.sidebar = Sidebar(self)
        self.controls = [self.sidebar, self.toggle_nav_rail_button]

    def toggle_nav_rail(self, e):
        self.sidebar.visible = not self.sidebar.visible
        self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
        self.page.update()

    def page_resize(self, e=None):
        self.page.update()
