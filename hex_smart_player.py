from typing import List
from hex_random_player import RandomPlayer

INF = 100000


def return_max(a, b):
    return b if a[2] < b[2] else a


class SmartPlayer(RandomPlayer):
    def __init__(self, file_paths: List[str]):
        super().__init__()
        paths_list = file_paths

    def choose_move(self, game_state, sign):
        self.update_empty_cells(game_state)
        res = [-1, -1, -INF]
        for i, j in self.empty_cells_list:
            game_state.update_cell(i, j, sign)
            score, count = self.query(str(game_state))
            res = return_max(res, [i, j, score])

    def query(self):
        pass

