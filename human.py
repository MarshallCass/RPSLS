from players import Players

class Human(Players):
    def _init_(self):
        self.person = []
        super().__init__()

    