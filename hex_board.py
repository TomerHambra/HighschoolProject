from hex_cell import Cell


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[Cell(i, j, self) for j in range(width)] for i in range(height)]
        [cell.update_neighbors() for row in self.cells for cell in row]

    def update_cell(self, row, col, sign):
        self.cells[row][col].value = sign

    def __str__(self):
        #  Blue: 0  |  Empty: 1  |  Red: 2
        s = ''
        for row in self.cells:
            for cell in row:
                s += str((cell.value+1) % 3)
        return s
