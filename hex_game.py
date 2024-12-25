from hex_board import Board
from hex_random_player import RandomPlayer
from collections import deque


class Game:
    def __init__(self, width=7, height=7, red_player=RandomPlayer(), blue_player=RandomPlayer()):
        self.board = Board(width, height)
        self.width = width
        self.height = height
        self.red = red_player       #  1    |  row
        self.blue = blue_player     # -1    |  col
        self.last_move = (-1, -1)
        self.boards_list = []
        self.ranked_boards_list = []
        self.alpha = 0.9
        self.beta = 100

    def reset_game(self):  # garbage collection <3
        self.board = Board(self.width, self.height)
        self.last_move = (-1, -1)
        self.boards_list = []
        self.ranked_boards_list = []

    # Old Version (BFS)
    def check_win(self, sign):
        q = deque()
        q.append(self.last_move)
        border_check = 0
        vis = [[0 for i in range(self.width)] for j in range(self.height)]
        vis[self.last_move[0]][self.last_move[1]] = 1
        while len(q):
            u, v = q.popleft()
            for cell in self.board.cells[u][v].get_neighbors():
                if vis[cell.row][cell.col] == 0 and cell.value == sign:
                    q.append((cell.row, cell.col))
                    vis[cell.row][cell.col] = 1
                    border_check |= cell.border
        if sign == -1:
            return (border_check & 10) == 10
        else:
            return (border_check & 5) == 5

    def save_board_to_list(self):
        self.boards_list.append(str(self.board))

    def do_move(self, sign):  # DONE
        player = self.red if (sign+1) else self.blue
        y, x = player.choose_move(self.board)
        if y == -1:
            return 2  # tie
        self.last_move = (y, x)
        self.board.update_cell(y, x, sign)
        self.save_board_to_list()
        if self.check_win(sign):
            return sign
        return 0  # no endgame yet...

    def play(self):
        sign = 1
        self.reset_game()
        state = self.do_move(sign)
        while not state:
            sign *= -1
            state = self.do_move(sign)
        self.rank_boards(state)

    def rank_boards(self, state):
        if state == 2:
            state = 0
        mu = self.beta * state
        boards = reversed(self.boards_list)
        for s in boards:
            self.ranked_boards_list.append((s, mu))
            mu *= self.alpha

    def get_ranked_boards(self):
        return self.ranked_boards_list


