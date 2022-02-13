class Cell:
    def __init__(self, letter, visited = False):
        self.letter = letter
        self.visited = visited


    def __str__(self):
        return self.letter + "|" + str(self.visited)


    def __repr__(self):
        return self.letter + "|" + str(self.visited)


    def get_letter(self):
        return self.letter


    def get_visited(self):
        return self.visited


    def set_visited(self, visit):
        self.visited = visit