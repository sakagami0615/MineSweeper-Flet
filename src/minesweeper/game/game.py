from collections import deque
from itertools import product
from random import randint

from src.minesweeper.game.display import BoardDisplay
from src.minesweeper.game.square import Square
from src.minesweeper.user_setting import GAME_CONFIG


class MineSweeper(BoardDisplay):
    def __init__(self):
        self._is_init = True
        self._board = [
            [Square() for _ in range(GAME_CONFIG.board_size)]
            for _ in range(GAME_CONFIG.board_size)
        ]
        self._is_gameover = False
        self._is_burst = False

    @property
    def is_gameover(self) -> bool:
        return self._is_gameover

    def _create_board(self, init_i: int, init_j: int) -> None:
        # 初期マスが爆弾にならないように盤面を作成する
        def set_bomb():
            bomb_cnt = 0
            for idx in range(GAME_CONFIG.board_size * GAME_CONFIG.board_size):
                i, j = (
                    idx // GAME_CONFIG.board_size,
                    idx % GAME_CONFIG.board_size,
                )
                if i == init_i and j == init_j:
                    continue
                if bomb_cnt >= GAME_CONFIG.n_bomb:
                    break
                self._board[i][j].n_bomb = -1
                bomb_cnt += 1

        def shuffle_board():
            N_SHUFFLE = 10000
            for _ in range(N_SHUFFLE):
                a_i, a_j = randint(0, GAME_CONFIG.board_size - 1), randint(
                    0, GAME_CONFIG.board_size - 1
                )
                b_i, b_j = randint(0, GAME_CONFIG.board_size - 1), randint(
                    0, GAME_CONFIG.board_size - 1
                )
                if (init_i == a_i and init_j == a_j) or (
                    init_i == b_i and init_j == b_j
                ):
                    continue
                self._board[a_i][a_j], self._board[b_i][b_j] = (
                    self._board[b_i][b_j],
                    self._board[a_i][a_j],
                )

        def set_n_bomb():
            def count_bomb(i, j):
                num = 0
                for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
                    n_i, n_j = i + dy, j + dx
                    if (
                        n_i < 0
                        or n_j < 0
                        or n_i >= GAME_CONFIG.board_size
                        or n_j >= GAME_CONFIG.board_size
                    ):
                        continue
                    if self._board[n_i][n_j].is_bomb:
                        num += 1
                return num

            for idx in range(GAME_CONFIG.board_size * GAME_CONFIG.board_size):
                i, j = (
                    idx // GAME_CONFIG.board_size,
                    idx % GAME_CONFIG.board_size,
                )
                if self._board[i][j].is_bomb:
                    continue
                self._board[i][j].n_bomb = count_bomb(i, j)

        set_bomb()
        shuffle_board()
        set_n_bomb()

    def _count_close(self) -> int:
        num = 0
        for idx in range(GAME_CONFIG.board_size * GAME_CONFIG.board_size):
            i, j = idx // GAME_CONFIG.board_size, idx % GAME_CONFIG.board_size
            num += int(not self._board[i][j].is_open)
        return num - GAME_CONFIG.n_bomb

    def _full_open(self) -> None:
        # ゲーム終了時にすべてのマスを開ける処理
        for idx in range(GAME_CONFIG.board_size * GAME_CONFIG.board_size):
            i, j = idx // GAME_CONFIG.board_size, idx % GAME_CONFIG.board_size
            if self._board[i][j].is_flag:
                # 旗もおろす
                self._board[i][j].switch_flag()
            self._board[i][j].open()

    def put_flag(self, i: int, j: int) -> None:
        self._board[i][j].switch_flag()

    def mine(self, i: int, j: int) -> None:
        if self._board[i][j].is_flag:
            return None

        if self._is_init:
            self._create_board(i, j)
            self._is_init = False

        if self._board[i][j].is_bomb:
            self._full_open()
            self._is_gameover = True
            self._is_burst = True
        else:
            self._board[i][j].open()
            que = deque()
            if self._board[i][j].n_bomb == 0:
                que.append((i, j))
            # 周囲の爆弾が0個の場合は、一括で開ける
            while que:
                c_i, c_j = que.popleft()
                for dx, dy in product([-1, 0, 1], [-1, 0, 1]):
                    n_i, n_j = c_i + dy, c_j + dx
                    if (
                        n_i < 0
                        or n_j < 0
                        or n_i >= GAME_CONFIG.board_size
                        or n_j >= GAME_CONFIG.board_size
                    ):
                        continue
                    if self._board[n_i][n_j].is_open:
                        continue
                    self._board[n_i][n_j].open()
                    if self._board[n_i][n_j].n_bomb == 0:
                        que.append((n_i, n_j))

            if self._count_close() == 0:
                self._full_open()
                self._is_gameover = True
