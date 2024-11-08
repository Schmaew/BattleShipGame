import tkinter as tk
from random import choice
from board import Board
from ship import Ship

class BattleshipUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Battleship Game")
        self.board = Board(6, 6)  # 6x6 grid
        self.create_board()

        # Dummy ship placement for testing
        ship = Ship(3)  
        self.board.place_ship(ship, 1, 1, horizontal=True)  

    def create_board(self):
        board_frame = tk.Frame(self.root)
        board_frame.grid(row=0, column=0, padx=10, pady=10)

        self.buttons = {} 
        for row in range(6):
            for col in range(6):
                btn = tk.Button(board_frame, text="", width=5, height=2,
                                command=lambda r=row, c=col: self.fire_at(r, c))
                btn.grid(row=row, column=col)
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
