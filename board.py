class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = [[None for _ in range(cols)] for _ in range(rows)]  

    def is_empty(self, row, col):
        return self.board[row][col] is None  

    def place_ship(self, ship, start_row, start_col, horizontal=True):
        if horizontal:
            for i in range(ship.size):
                self.board[start_row][start_col + i] = ship
        else:
            for i in range(ship.size):
                self.board[start_row + i][start_col] = ship

    def fire_at(self, row, col):
        if self.board[row][col] is None:
            return False  
        else:
            ship = self.board[row][col]
            hit = ship.hit()
            if hit:  
                self.board[row][col] = None  
            return True  
