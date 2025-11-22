import flet as ft
from sidebar import Sidebar
from data_store import DataStore


class AppLayout(ft.Row):
    def __init__(self, app, page: ft.Page, store: DataStore, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.page = page
        self.store = store
        self.page.on_resized = self.page_resize
        self.toggle_sidebar_button = ft.IconButton(
            icon=ft.Icons.ARROW_CIRCLE_LEFT,
            icon_color=ft.Colors.BLUE_GREY_400,
            selected=False,
            selected_icon=ft.Icons.ARROW_CIRCLE_RIGHT,
            selected_icon_color=ft.Colors.BLUE_GREY_400,
            on_click=self.toggle_nav_rail,
        )
        self.sidebar = Sidebar(self.app, self, self.store)
        self.controls = [self.sidebar, self.toggle_sidebar_button]

    def toggle_nav_rail(self, e):
        self.sidebar.visible = not self.sidebar.visible
        self.toggle_sidebar_button.selected = not self.toggle_sidebar_button.selected
        self.page.update()

    def page_resize(self, e=None):
        self.page.update()

    def hydrate_all_portfolios_view(self):
        self.sidebar.sync_portfolio_column()

    def portfolio_click(self, e):
        self.sidebar.nav_change(self.store.get_portfolios().index(e.control.data))
