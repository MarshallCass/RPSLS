from gestures import Gestures


class Human(Gestures):
    def __init__(self, name):
        self.player = name
        self.points = 0
        super().__init__()
