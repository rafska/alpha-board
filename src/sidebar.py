import flet as ft


class Sidebar(ft.Container):
    def __init__(self, app_layout):
        self.app_layout = app_layout
        self.nav_rail_visible = True
        self.nav_items = []

        self.nav_rail = ft.NavigationRail(
            selected_index=None,
            label_type=ft.NavigationRailLabelType.ALL,
            on_change=self.nav_change,
            destinations=self.nav_items,
            bgcolor=ft.Colors.BLUE_GREY,
            extended=True,
            expand=True,
        )

        self.toggle_nav_rail_button = ft.IconButton(ft.Icons.ARROW_BACK)

        super().__init__(
            content=ft.Column(
                [self.nav_rail],
                tight=True,
                expand=True,
            ),
            padding=ft.padding.all(15),
            margin=ft.margin.all(0),
            width=250,
            bgcolor=ft.Colors.BLUE_GREY,
            visible=self.nav_rail_visible,
        )

    def nav_change(self, e):
        self.nav_rail.selected_index = e.control.selected_index
        self.update()
