from src.minesweeper.user_setting import BOARD_MARK_CONFIG


class SquareDisplay:
    def square_mark(self, burst: bool) -> str:
        if self._is_open:
            if not self.is_bomb:
                return str(self.n_bomb)
            else:
                return (
                    BOARD_MARK_CONFIG.burst
                    if burst
                    else BOARD_MARK_CONFIG.bomb
                )
        else:
            return (
                BOARD_MARK_CONFIG.flag
                if self.is_flag
                else BOARD_MARK_CONFIG.close
            )


class BoardDisplay:
    def board_mark(self) -> list[str]:
        # UI表示用の盤面文字を取得
        return [
            [square.square_mark(self._is_burst) for square in line]
            for line in self._board
        ]
