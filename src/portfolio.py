import itertools
import flet as ft


class Portfolio(ft.Container):
    id_counter = itertools.count()

    def __init__(self, app, name: str, page: ft.Page):
        self.app = app
        self.name = name
        self.portfolio_id = next(Portfolio.id_counter)
        self.page = page

        super().__init__(
            content=None,
            data=self,
            margin=ft.margin.all(0),
            padding=ft.padding.only(top=10, right=0),
            height=self.app.page.height,
        )
