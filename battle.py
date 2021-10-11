from human import Human
from computer import Computer
from players import Players
import random


class Battle:
    def __init__(self):
        self.players_list = []
        self.computers_list = []
        self.human_selection = ()
        self.computer_points = 0
        self.player_one_points = 0
        self.player_two_points = 0

    def run_game(self):
        self.players = Players()
        self.players.create_player()
        self.players.create_computer()
        self.game_selection()

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

    def game_selection(self):
        self.player_selection = input("How many players do you have?")
        
        if self.human_selection=="rock" or "0" : 0
        elif self.human_selection=="Spock" or "1" : 1
        elif self.human_selection=="paper" or "2" : 2
        elif self.human_selection=="lizard" or "3" : 3
        elif self.human_selection=="scissors" or "4" : 4
        else: print("Error on name.")
   

        if self.player_selection == "1":
           while self.computer_points and self.player_one_points < 2:
            print("Please enter your gesture name or number!")
            self.human_selection = input("0 - rock , 1 - spock, 2 - paper, 3 - lizard, 4 - scissors ")
            self.computer_selection = random.randint(0,4)
            self.number_difference = (int(self.computer_selection) - int(self.human_selection)) % 5   
            if self.number_difference == 0:
                   print("Tie try again!")
            elif self.number_difference == 1 or self.number_difference == 2:
                    self.computer_points + 1  
                    print("Computer Wins") 
            elif self.number_difference == 3 or self.number_difference == 4:
                    self.player_one_points + 1
                    print("Human Wins")
        elif self.player_selection == "2":
            print("Please enter your gesture name or number!")
            self.player_one_selection = input("0 - rock , 1 - spock, 2 - paper, 3 - lizard, 4 - scissors ")
            print("Please enter your gesture name or number!")
            self.player_two_selection = input("0 - rock , 1 - spock, 2 - paper, 3 - lizard, 4 - scissors ")
            self.number_difference = (int(self.player_two_selection) - int(self.player_one_selection)) % 5
            if self.number_difference == 0:
                   print("Tie try again!")
            elif self.number_difference == 1 or self.number_difference == 2:
                    self.player_one_points + 1  
                    print("Player 1 Wins") 
            elif self.number_difference == 3 or self.number_difference == 4:
                    self.player_two_points + 1
                    print("Player 2 Wins")