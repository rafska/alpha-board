import flet as ft
from app_layout import AppLayout


class AlphaBoardApp(AppLayout):
    def __init__(self, page: ft.Page):
        self.page = page
        self.appbar_items = [
            ft.PopupMenuItem(text="Settings"),
            ft.PopupMenuItem(),
            ft.PopupMenuItem(text="Logout"),
        ]
        self.appbar = ft.AppBar(
            leading=ft.Icon(ft.Icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=ft.Text("Alpha Board", size=32, text_align="start"),
            center_title=False,
            toolbar_height=75,
            bgcolor=ft.Colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                ft.Container(
                    content=ft.PopupMenuButton(items=self.appbar_items),
                    margin=ft.margin.only(left=50, right=25),
                )
            ],
        )
        self.page.appbar = self.appbar
        self.page.update()
        super().__init__(
            self,
            self.page,
            tight=True,
            expand=True,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
