from hex_game import Game
from hex_random_player import RandomPlayer
import json


class Games:
    def __init__(self, width=7, height=7, red_player=RandomPlayer(), blue_player=RandomPlayer(),
                 dataset_path='dataset.json'):
        self.game = Game(width, height, red_player=red_player, blue_player=blue_player)
        self.path = dataset_path
        self.dict = {}
        with open(dataset_path, 'r') as f:
            try:
                self.dict = json.load(f)
            except json.decoder.JSONDecodeError:
                print("Invalid JSON")

    def run_simulations(self, amount):
        print("Simulating {} games:".format(amount))
        k = 4
        stops = [amount // 4 * (i + 1) for i in range(k)]
        for _ in range(amount):
            self.game.play()
            boards_list = self.game.get_ranked_boards()
            self.update_data(boards_list)

            if _ in stops:
                print(str(_ / amount) + '%')
        print("Finished simulating {} games.".format(amount))
        print("Saving data...")
        self.update_dataset()
        print("Finished saving")

    def run_game(self):
        self.game.play()
        return self.game.get_ranked_boards()

    def update_dataset(self):
        with open(self.path, 'w+') as f:
            json.dump(self.dict, f)

    def update_data(self, boards_list):
        for s, v in boards_list:
            vt, c = self.dict[s] if s in self.dict.keys() else (0, 0)
            self.dict[s] = ((vt + v) / (c + 1), c + 1)
