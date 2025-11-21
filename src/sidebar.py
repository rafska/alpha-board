import flet as ft


class Sidebar(ft.Container):
    def __init__(self, app, app_layout, store):
        self.app = app
        self.app_layout = app_layout
        self.store = store
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
                    self.nav_rail,
                ],
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

    def sync_portfolio_destinations(self):
        portfolios = self.store.get_portfolios()
        self.nav_rail.destinations = []
        for i in range(len(portfolios)):
            b = portfolios[i]
            self.nav_rail.destinations.append(
                ft.NavigationRailDestination(
                    label_content=ft.TextField(
                        value=b.name,
                        hint_text=b.name,
                        text_size=12,
                        read_only=True,
                        on_focus=self.portfolio_name_focus,
                        on_blur=self.portfolio_name_blur,
                        border=ft.InputBorder.NONE,
                        height=50,
                        width=150,
                        text_align=ft.TextAlign.START,
                        data=i,
                    ),
                    label=b.name,
                    selected_icon=ft.Icons.CHEVRON_RIGHT_ROUNDED,
                    icon=ft.Icons.CHEVRON_RIGHT_OUTLINED,
                )
            )

    def portfolio_name_focus(self, e):
        e.control.read_only = False
        e.control.border = ft.InputBorder.OUTLINE
        self.page.update()

    def portfolio_name_blur(self, e):
        self.store.update_portfolio(
            self.store.get_portfolios()[e.control.data], {"name": e.control.value}
        )
        self.app_layout.hydrate_all_portfolios_view()
        e.control.read_only = True
        e.control.border = ft.InputBorder.NONE
        self.page.update()
