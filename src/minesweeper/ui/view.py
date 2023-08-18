from collections import namedtuple

import flet as ft

from src.minesweeper.game.manage import Manager
from src.minesweeper.ui.event import Event
from src.minesweeper.user_setting import (
    GAME_CONFIG,
    MODE_MARK_CONFIG,
    SQUARE_DRAW_CONFIG,
    VIEW_CONFIG,
)

Container = namedtuple("Container", ["mode", "board"])


class View(Event):
    def __init__(self):
        self._manager = Manager()
        self._containers = self._generate_containers()

    def _generate_containers(self) -> Container:
        mode = self._generate_mode()
        board = []
        for i in range(GAME_CONFIG.board_size):
            board.append(
                [
                    self._generate_block(i, j)
                    for j in range(GAME_CONFIG.board_size)
                ]
            )
        return Container(mode, board)

    def _generate_mode(self):
        return ft.Text(MODE_MARK_CONFIG.mine, size=VIEW_CONFIG.mode_size)

    def _generate_block(self, i: int, j: int) -> ft.Container:
        return ft.Container(
            alignment=ft.alignment.center,
            width=SQUARE_DRAW_CONFIG.square_size,
            height=SQUARE_DRAW_CONFIG.square_size,
            bgcolor=SQUARE_DRAW_CONFIG.close_color,
            border_radius=ft.border_radius.all(
                SQUARE_DRAW_CONFIG.border_radius
            ),
            on_click=self.click_event(i, j),
        )

    def _create_page(self) -> None:
        self._page.title = VIEW_CONFIG.caption
        self._page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self._page.on_keyboard_event = self.keyboard_event()

    def _create_layout(self) -> None:
        self._page.add(
            ft.Row(
                [self._containers.mode], alignment=ft.MainAxisAlignment.CENTER
            )
        )
        for items in self._containers.board:
            self._page.add(
                ft.Row(items, alignment=ft.MainAxisAlignment.CENTER)
            )

    def exec(self, page: ft.Page):
        self._page = page
        self._create_page()
        self._create_layout()
