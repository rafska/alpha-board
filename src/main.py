import flet as ft
from alpha_board import AlphaBoardApp
from data_store import DataStore


def main(page: ft.Page):
    page.title = "Alpha Board"
    page.padding = 0
    page.bgcolor = ft.Colors.BLUE_GREY_200
    app = AlphaBoardApp(page, DataStore())
    page.add(app)
    page.update()


if __name__ == "__main__":
    ft.app(main)
