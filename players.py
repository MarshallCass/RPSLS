from human import Human
from computer import Computer
from gestures import Gestures


class Players(Gestures):
    def __init__(self):
        self.guesture_list = []
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

# Guesture selection validation
#     def guesture_input(self):
#         while not self.guesture_input:
#             self.guesture_selection = int(input('Rock-0, Paper-1, Scissors-2, Lizard-3, Spock-4'))
#         if self.guesture_selection.isdigit(range(0,5)):
#             self.guesture_input = True
#             print('this is ok number')
#         else:
#             print('Your selection was invalid')
