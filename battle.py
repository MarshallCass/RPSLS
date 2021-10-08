from human import Human
from computer import Computer
from players import Players


class Battle:
    def __init__(self):
        self.players_list = []
        self.computers_list = []

    def run_game(self):

        self.players = Players()
        self.players.create_player()
        self.players.create_computer()
        self.player_input()


# Game player selection validation

    # def player_input(self):
    #     player_selection = input(
    #         "Press 1 for Player vs Player or 2 for Player vs Computer")

    #     if player_selection == "1":

    #        # AI Method
    #     elif player_selection == "2":

    #        # human on human
    #     else:
    #         self.player_input()

    #       # run input again
