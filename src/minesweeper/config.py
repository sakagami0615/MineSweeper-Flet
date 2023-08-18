from dataclasses import dataclass

import flet as ft


@dataclass
class SquareDrawConfig:
    square_size: int
    border_radius: int
    close_color: ft.colors
    open_color: ft.colors


@dataclass
class ModeMarkConfig:
    mine: str
    flag: str


@dataclass
class BoardMarkConfig:
    close: str
    flag: str
    bomb: str
    burst: str


@dataclass
class ViewConfig:
    caption: str
    mode_switch_key: str
    mode_size: int


@dataclass
class GameConfig:
    board_size: int
    n_bomb: int
