from players import Players

class Computer(Players):
    def _init_(self):
        self.computer = "" 
        super().__init__()