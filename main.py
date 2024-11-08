import tkinter as tk
import random
from random import choice
from board import Board
from ship import Ship

class BattleshipUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Battleship Game")
        self.board = Board(6, 6)  
        self.create_board()

        for _ in range(3):
            self.place_random_ship()

    def place_random_ship(self):
        ship_size = random.randint(2, 5)  
        orientation = random.choice(["horizontal", "vertical"])  # Random orientation

        while True:
            if orientation == "horizontal":
                start_row = random.randint(0, 5)
                start_col = random.randint(0, 5 - ship_size)
                if all(self.board.is_empty(start_row, start_col + i) for i in range(ship_size)):
                    ship = Ship(ship_size)
                    self.board.place_ship(ship, start_row, start_col, horizontal=True)
                    break

            else:  # Vertical orientation
                start_row = random.randint(0, 5 - ship_size)
                start_col = random.randint(0, 5)
                if all(self.board.is_empty(start_row + i, start_col) for i in range(ship_size)):
                    ship = Ship(ship_size)
                    self.board.place_ship(ship, start_row, start_col, horizontal=False)
                    break

    def create_board(self):
        board_frame = tk.Frame(self.root)
        board_frame.grid(row=0, column=0, padx=10, pady=10)

        self.buttons = {}

        for col in range(6):
            col_label = tk.Label(board_frame, text=str(col + 1), width=5, height=2)
            col_label.grid(row=0, column=col + 1)  

        for row in range(6):
            row_label = tk.Label(board_frame, text=str(row + 1), width=5, height=2)
            row_label.grid(row=row + 1, column=0)  

        for row in range(6):
            for col in range(6):
                btn = tk.Button(board_frame, text="", width=5, height=2,
                                command=lambda r=row, c=col: self.fire_at(r, c))
                btn.grid(row=row + 1, column=col + 1)  
                self.buttons[(row, col)] = btn

        self.test_button = tk.Button(self.root, text="Test Firing", command=self.test_fire)
        self.test_button.grid(row=1, column=0, pady=10)

    def fire_at(self, row, col):
        result = self.board.fire_at(row, col)
        if result is None:
            self.display_message("Already fired at this cell!")
        elif result:
            self.buttons[(row, col)].config(text="O", bg="red")
            self.display_message(f"Hit at {row + 1}, {col + 1}!")
        else:
            self.buttons[(row, col)].config(text="X", bg="blue")
            self.display_message(f"Miss at {row + 1}, {col + 1}!")

    def test_fire(self):
        row, col = choice(range(6)), choice(range(6))
        self.fire_at(row, col)

    def display_message(self, message):
        print(message)

if __name__ == "__main__":
    root = tk.Tk()
    game = BattleshipUI(root)
    root.mainloop()
