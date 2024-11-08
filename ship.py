class Ship:
    def __init__(self, size):
        self.size = size
        self.hits = 0

    def hit(self):
        self.hits += 1
        return self.hits >= self.size
