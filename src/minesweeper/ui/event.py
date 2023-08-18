from typing import Callable

import flet as ft

from src.minesweeper.user_setting import (
    BOARD_MARK_CONFIG,
    MODE_MARK_CONFIG,
    SQUARE_DRAW_CONFIG,
    VIEW_CONFIG,
)


class Event:
    def click_event(self, click_i: int, click_j: int) -> Callable:
        def callback(e: ft.KeyboardEvent):
            # モードによって、マスを開けるか旗を立てるかを切り替える
            is_flag = (
                False
                if self._containers.mode.value == MODE_MARK_CONFIG.mine
                else True
            )
            board = self._manager.click(click_i, click_j, is_flag)

            for i, line in enumerate(board):
                for j, text in enumerate(line):
                    self._containers.board[i][j].content = ft.Text(value=text)
                    color = (
                        SQUARE_DRAW_CONFIG.close_color
                        if text == BOARD_MARK_CONFIG.close
                        else SQUARE_DRAW_CONFIG.open_color
                    )
                    self._containers.board[i][j].bgcolor = color
            self._page.update()

        return callback

    def keyboard_event(self) -> Callable:
        def callback(e: ft.KeyboardEvent):
            if self._manager.is_gameover():
                return
            if e.key == VIEW_CONFIG.mode_switch_key:
                mode = (
                    MODE_MARK_CONFIG.flag
                    if self._containers.mode.value == MODE_MARK_CONFIG.mine
                    else MODE_MARK_CONFIG.mine
                )
                self._containers.mode.value = mode
            self._page.update()

        return callback
