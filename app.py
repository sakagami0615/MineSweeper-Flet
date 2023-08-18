# import os
# import sys

# sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import flet as ft

from src.minesweeper.ui.view import View

if __name__ == "__main__":
    view = View()
    ft.app(target=view.exec)
