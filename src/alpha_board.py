import flet as ft
from app_layout import AppLayout
from data_store import DataStore
from portfolio import Portfolio


class AlphaBoardApp(AppLayout):
    def __init__(self, page: ft.Page, store: DataStore):
        self.page = page
        self.store = store
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
        self.page.on_route_change = self.route_change
        super().__init__(
            self,
            self.page,
            self.store,
            tight=True,
            expand=True,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
        self.page.go("/")

    def route_change(self, e):
        troute = ft.TemplateRoute(self.page.route)
        if troute.match("/"):
            self.set_welcome_view()
        elif troute.match("/portfolio/:id"):
            if int(troute.id) > len(self.store.get_portfolios()):
                self.page.go("/")
                return
            self.set_portfolio_view(int(troute.id))

    def add_portfolio(self, e):
        def close_dlg(e):
            if (hasattr(e.control, "text") and not e.control.text == "Cancel") or (
                type(e.control) is ft.TextField and e.control.value != ""
            ):
                self.create_new_portfolio(dialog_text.value)
            self.page.close(dialog)
            self.page.update()

        def textfield_change(e):
            if dialog_text.value == "":
                create_button.disabled = True
            else:
                create_button.disabled = False
            self.page.update()

        dialog_text = ft.TextField(
            label="New Portfolio Name", on_submit=close_dlg, on_change=textfield_change
        )
        create_button = ft.ElevatedButton(
            text="Create",
            color=ft.Colors.WHITE,
            bgcolor={
                ft.ControlState.DEFAULT: ft.Colors.BLUE_200,
                ft.ControlState.HOVERED: ft.Colors.BLUE_400,
            },
            on_click=close_dlg,
            disabled=True,
        )
        dialog = ft.AlertDialog(
            title=ft.Text("Name your new portfolio"),
            content=ft.Column(
                [
                    dialog_text,
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                text="Cancel", color=ft.Colors.WHITE, on_click=close_dlg
                            ),
                            create_button,
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                ],
                tight=True,
            ),
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.page.open(dialog)
        dialog.open = True
        self.page.update()
        dialog_text.focus()

    def create_new_portfolio(self, portfolio_name):
        new_portfolio = Portfolio(self, portfolio_name, self.page)
        self.store.add_portfolio(new_portfolio)
        self.hydrate_all_portfolios_view()

    def delete_portfolio(self, e):
        self.store.remove_portfolio(e.control.data)
        self.set_welcome_view()
