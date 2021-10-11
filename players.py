from human import Human
from computer import Computer
from gestures import Gestures


class Players(Gestures):
    def __init__(self):
        self.players_list = []
        self.computers_list = []

    def create_player(self):
        player_one = Human("Player 1")
        player_two = Human("Player 2")
        self.players_list.append(player_one)
        self.players_list.append(player_two)

    def create_computer(self):
        computer = Computer("Computer")
        self.computers_list.append(computer)


