
directions = [(-1, 1), (-1, 0), (0, 1), (0, -1), (1, 0), (1, -1)]

# If P is a colored hexagonal, the neighboring cells are marked in X:
#   .   X   X
#   X   P   X
#   X   X   .


class Cell:
    def __init__(self, row, col, board_ref):
        self.row = row
        self.col = col
        self.value = 0
        self.board_ref = board_ref
        self.neighbors = []
        self.border = (((row == 0) << 3) + ((col == 0) << 2) +
                       ((row == self.board_ref.height - 1) << 1) + (col == self.board_ref.width - 1))

    def check_boundaries(self, dx, dy):
        return 0 <= self.row + dy < self.board_ref.height and 0 <= self.col + dx < self.board_ref.width

    def update_neighbors(self):
        self.neighbors = self.get_neighbors()

    def get_neighbors(self):
        return [self.board_ref.cells[self.row + dy][self.col + dx]
                for dy, dx in directions if self.check_boundaries(dx, dy)]
