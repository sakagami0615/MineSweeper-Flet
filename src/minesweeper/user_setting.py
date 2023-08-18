import flet as ft

from src.minesweeper.config import (
    BoardMarkConfig,
    GameConfig,
    ModeMarkConfig,
    SquareDrawConfig,
    ViewConfig,
)

SQUARE_DRAW_CONFIG = SquareDrawConfig(
    square_size=40,
    border_radius=5,
    close_color=ft.colors.AMBER_500,
    open_color=ft.colors.BLUE_GREY_700,
)

MODE_MARK_CONFIG = ModeMarkConfig(mine="⛏️", flag="🚩")

BOARD_MARK_CONFIG = BoardMarkConfig(close="", flag="🚩", bomb="💣", burst="💥")

VIEW_CONFIG = ViewConfig(
    caption="Mine Sweeper", mode_switch_key="Q", mode_size=25
)

GAME_CONFIG = GameConfig(board_size=10, n_bomb=10)
