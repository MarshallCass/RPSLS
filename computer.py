from gestures import Gestures


class Computer(Gestures):
    def __init__(self, name):
        self.computer = name
        super().__init__()

    def create_computer(self):
        computer = "Computer"
        self.computer.append(computer)


# Guesture selection validation
#     def guesture_input(self):
#        random generation
