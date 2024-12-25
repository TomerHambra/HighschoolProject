from hex_games import Games
from hex_collections import print_boards_list


def main():
    engine = Games()
    # engine.run_simulations(1_000_000)
    print_boards_list(reversed(engine.run_game()))


if __name__ == "__main__":
    main()
