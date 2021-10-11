from typing import Counter
from gestures import Gestures
from human import Human
from computer import Computer
from players import Players


class Battle(Gestures):
    def __init__(self):
        self.players_list = []
        self.computers_list = []
        self.player_1_selection = []
        self.player_2_selection = []
        self.computer_selection = []
        self.computer_points = 0
        self.player_1_points = 0
        self.player_2_points = 0
        self.number_difference = 0


    def run_game(self):
        self.display_welcome()
        self.players = Players()
        self.players.create_player()
        self.players.create_computer()
        self.player_input()

    def display_welcome(self):
        print("Welcome to Rock Paper Scissors Lizard Spock!")

# ### Game play logic
# # # Rock crushes Scissors 
# # # Rock crushes Lizard 
# # # Spock vaporizes Rock 
# # # Spock smashes Scissors 
# # # Paper disproves Spock 
# # # Paper covers Rock 
# # # Lizard eats Paper 
# # # Lizard poisons Spock 
# # # Scissors decapitates Lizard 
# # # Scissors cuts Paper 

    def player_input(self):
        selection = False
        player_selection = ""
        while selection == False:
            player_selection = input(
            "Press 1 for Player vs Player or 2 for Player vs Computer" " ")
            if player_selection == "1":
                selection = True
                self.player_vs_player()
            elif player_selection == "2":
                selection = True
                self.player_vs_computer()    
            else:
                print("not valid input")
               

    def player_vs_player(self):
        counter = 0
        while self.player_1_points <2 and self.player_2_points < 2:
            self.player_1_gesture_selection()
            self.player_2_gesture_selection()
            self.number_difference = (self.player_1_selection[counter] - self.player_2_selection[counter]) % 5   

            if self.number_difference == 0:
                   print("Tie try again!")
                   counter += 1
            elif self.number_difference == 1 or self.number_difference == 2:
                    self.player_1_points += 1  
                    print("Player 1 Wins") 
                    counter += 1
            elif self.number_difference == 3 or self.number_difference == 4:
                    self.player_2_points += 1
                    print("Player 2 Wins")
                    counter += 1
        self.winning_player()

    def player_vs_computer(self):
        counter=0
        while self.computer_points < 2 and self.player_1_points < 2:
            self.player_1_gesture_selection()
            self.computer_gesture_selection()
            self.number_difference = (self.computer_selection[counter] - self.player_1_selection[counter]) % 5   

            if self.number_difference == 0:
                   print("Tie try again!")
                   counter += 1 
            elif self.number_difference == 1 or self.number_difference == 2:
                    self.computer_points += 1  
                    print("Computer Wins")
                    counter += 1
            elif self.number_difference == 3 or self.number_difference == 4:
                    self.player_1_points += 1
                    print("Player 1 wins")
                    counter += 1 
        self.winning_player()

    def winning_player(self):
        if self.player_1_points == 2:
            print("Player 1 Wins Best of 3 Games!!!")
        elif self.player_2_points == 2:
            print("Player 2 Wins Best of 3 Games!!!")
        elif self.computer_points == 2:
            print("Computer Wins Best of 3 Games!!!")
