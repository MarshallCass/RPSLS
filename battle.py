from gestures import Gestures
from human import Human
from computer import Computer
from players import Players
from gestures import Gestures


class Battle(Gestures):
    def __init__(self):
        self.players_list = []
        self.computers_list = []
        self.player_1_selection = []
        self.player_2_selection = []
        self.computer_selection = []
    # players_list should pass in one or 2 players
    # computers_list should pass in 0 or 1 computer
    # player_1_selection should pass in rock, paper, scissors, lizard, or spock
    # player_2_selection should pass in rock, paper, scissors, lizard, or spock
    # player_1 _selection should pass in rock, paper, scissors, lizard, or spock

    def display_welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock!")

    def run_game(self):
        self.display_welcome()
        self.players = Players()
        self.players.create_player()
        self.players.create_computer()
        self.player_1_gesture_selection()
        self.display_welcome()
        self.display_welcome()

        # self.player_1_gesture_selction is being called from the parent class in gestures.py. it is giving errors at the moment.
        # once we get player_1_gesture_selction appended to self.player_1_selction above. We can do the same thing for player 2's selection and the computer selction.


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
