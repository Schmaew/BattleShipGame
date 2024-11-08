from cell import Cell

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]

    def place_ship(self, ship, start_row, start_col, horizontal=True):
        if horizontal:
            for col in range(start_col, start_col + ship.size):
                self.grid[start_row][col].has_ship = True
        else:
            for row in range(start_row, start_row + ship.size):
                self.grid[row][start_col].has_ship = True

    def fire_at(self, row, col):
        cell = self.grid[row][col]
        return cell.fire()
