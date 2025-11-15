import flet as ft
from alpha_board import AlphaBoardApp


def main(page: ft.Page):
    page.title = "Alpha Board"
    page.padding = 0
    page.bgcolor = ft.Colors.BLUE_GREY_200
    app = AlphaBoardApp(page)
    page.add(app)
    page.update()


if __name__ == "__main__":
    ft.app(main)
