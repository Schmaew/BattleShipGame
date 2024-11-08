class Cell:
    def __init__(self):
        self.has_ship = False
        self.is_hit = False

    def fire(self):
        if not self.is_hit:
            self.is_hit = True
            return self.has_ship
        return None  # Indicates that the cell was already fired at
