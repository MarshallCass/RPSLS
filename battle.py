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

    def display_welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock!")

    def run_game(self):
        self.display_welcome()
        self.players = Players()
        self.players.create_player()
        self.players.create_computer()
        self.player_input()
        self.display_welcome()

    def player_input(self):
        selection = False
        player_selection = input(
            "Press 1 for Player vs Player or 2 for Player vs Computer")
        while selection == False:
            if player_selection == "1":
                self.player_vs_player()
                selection = True
            elif player_selection == "2":
                self.player_vs_computer()
                selection = True
            else:
                print("not valid input")

          # run input again

    def player_vs_player(self):
        self.player_1_gesture_selection()
        self.player_2_gesture_selection()

        pass

    def player_vs_computer(self):
        self.player_1_gesture_selection()
        self.computer_gesture_selection()

        pass
