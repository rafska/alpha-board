import flet as ft


class Sidebar(ft.Container):
    def __init__(self, app, app_layout, store):
        self.app = app
        self.app_layout = app_layout
        self.store = store
        self.nav_items = []
        self.selected_index = -1

        self.portfolio_column = ft.Column([], expand=True)

        self.toggle_nav_rail_button = ft.IconButton(ft.Icons.ARROW_BACK)

        super().__init__(
            content=ft.Column(
                [
                    ft.Container(
                        ft.TextButton(
                            "Add new portfolio",
                            icon=ft.Icons.ADD,
                            on_click=self.app.add_portfolio,
                            style=ft.ButtonStyle(
                                color=ft.Colors.WHITE,
                                bgcolor={
                                    ft.ControlState.DEFAULT: ft.Colors.BLUE_200,
                                    ft.ControlState.HOVERED: ft.Colors.BLUE_400,
                                },
                                shape={
                                    ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(
                                        radius=3
                                    )
                                },
                            ),
                        ),
                        alignment=ft.alignment.center,
                    ),
                    self.portfolio_column,
                ],
                tight=True,
                expand=True,
            ),
            padding=ft.padding.all(15),
            margin=ft.margin.all(0),
            width=250,
            bgcolor=ft.Colors.BLUE_GREY,
        )

    def portfolio_select(self, e):
        self.portfolio_column.controls[self.selected_index].selected = False
        self.selected_index = e.control.data
        self.portfolio_column.controls[self.selected_index].selected = True
        self.update()

    def sync_portfolio_column(self):
        portfolios = self.store.get_portfolios()
        self.portfolio_column.controls = []
        for i in range(len(portfolios)):
            p = portfolios[i]
            self.portfolio_column.controls.append(
                ft.ListTile(
                    leading=ft.IconButton(
                        ft.Icons.CHEVRON_RIGHT_OUTLINED,
                        on_click=self.portfolio_select,
                        data=i,
                    ),
                    title=ft.Text(p.name),
                    trailing=ft.IconButton(
                        ft.Icons.DELETE, on_click=self.app.delete_portfolio, data=p
                    ),
                )
            )
