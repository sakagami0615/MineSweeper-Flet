from src.minesweeper.game.game import MineSweeper


class Manager:
    def __init__(self):
        self._game = MineSweeper()

    def click(self, i: int, j: int, is_flag: bool = False) -> list[str]:
        if not self._game.is_gameover:
            match is_flag:
                case True:
                    self._game.put_flag(i, j)
                case _:
                    self._game.mine(i, j)
        return self._game.board_mark()

    def is_gameover(self):
        return self._game.is_gameover
