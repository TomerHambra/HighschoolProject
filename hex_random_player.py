from hex_client import Client
import random


class RandomPlayer(Client):
    def __init__(self):
        super().__init__()
        self.empty_cells_list = []

    def choose_move(self, game_state):
        self.update_empty_cells(game_state)
        return tuple(random.choice(self.empty_cells_list)) if len(self.empty_cells_list) else (-1, -1)

    def update_empty_cells(self, game_state):
        self.empty_cells_list = [(cell.row, cell.col) for row in game_state.cells for cell in row if not cell.value]

