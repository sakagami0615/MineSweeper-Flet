from src.minesweeper.game.display import SquareDisplay


class Square(SquareDisplay):
    def __init__(self):
        self._n_bomb = 0
        self._is_open = False
        self._is_flag = False

    def open(self) -> bool:
        if self._is_open or self._is_flag:
            return True
        else:
            self._is_open = True
            return not self.is_bomb

    def switch_flag(self) -> None:
        self._is_flag = not self._is_flag

    @property
    def n_bomb(self) -> int:
        return self._n_bomb

    @n_bomb.setter
    def n_bomb(self, value: int) -> None:
        self._n_bomb = value

    @property
    def is_bomb(self) -> bool:
        return self._n_bomb == -1

    @property
    def is_open(self) -> bool:
        return self._is_open

    @property
    def is_flag(self) -> bool:
        return self._is_flag
