import random


class Gestures:
    def __init__(self):
        self.gesture_to_number = 0
        self.number_to_gesture = ""

    # def number_to_guesture(self):
    #     if self.number_to_gesture==0: return "rock"
    #     elif self.number_to_gesture==1: return "Spock"
    #     elif self.number_to_gesture==2: return "paper"
    #     elif self.number_to_gesture==3: return "lizard"
    #     elif self.number_to_gesture==4: return "scissors"
    #     else: print("Error on number." )

    def player_1_gesture_selection(self):
        # print("Please enter your gesture name or number!")
        # self.player_1_selection = input("0 - rock , 1 - spock, 2 - paper, 3 - lizard, 4 - scissors ")
        self.gesture_input = False
        self.gesture_selection = int(
            input('Player 1 choose: Rock-0, Paper-1, Scissors-2, Lizard-3, Spock-4'))
        while self.gesture_input != True:
            if self.gesture_selection == 0 or self.gesture_selection == 1 or self.gesture_selection == 2 or self.gesture_selection == 3 or self.gesture_selection == 4:
                self.gesture_input = True
            else:
                print('Your selection was invalid')
        if self.gesture_selection == 0:
            self.player_1_selection.append("Rock")
        elif self.gesture_selection == 1:
            self.player_1_selection.append("Paper")
        elif self.gesture_selection == 2:
            self.player_1_selection.append("Scissors")
        elif self.gesture_selection == 3:
            self.player_1_selection.append("Lizard")
        elif self.gesture_selection == 4:
            self.player_1_selection.append("Spock")

        # if self.player_1_gesture_selection =="rock" or "0" : 0
        # elif self.player_1_gesture_selection =="Spock" or "1" : 1
        # elif self.player_1_gesture_selection =="paper" or "2" : 2
        # elif self.player_1_gesture_selection =="lizard" or "3" : 3
        # elif self.player_1_gesture_selection =="scissors" or "4" : 4
        # else: print("Error on name.")

        # if self.computer_gesture_selection =="rock" or "0" : 0
        # elif self.computer_gesture_selection =="Spock" or "1" : 1
        # elif self.computer_gesture_selection =="paper" or "2" : 2
        # elif self.computer_gesture_selection =="lizard" or "3" : 3
        # elif self.computer_gesture_selection =="scissors" or "4" : 4
        # else: print("Error on name.")
         
            self.computer_selection = random.randint(0,4)

    def player_2_gesture_selection(self):
        # print("Player 2 enter your gesture name or number!")
        # self.player_two_selection = input("0 - rock , 1 - spock, 2 - paper, 3 - lizard, 4 - scissors ")
        self.gesture_input = False
        self.gesture_selection = int(
            input('Player 2 choose: Rock-0, Paper-1, Scissors-2, Lizard-3, Spock-4'))
        while self.gesture_input != True:
            if self.gesture_selection == 0 or self.gesture_selection == 1 or self.gesture_selection == 2 or self.gesture_selection == 3 or self.gesture_selection == 4:
                self.gesture_input = True
            else:
                print('Your selection was invalid')
        if self.gesture_selection == 0:
            self.player_2_selection.append("Rock")
        elif self.gesture_selection == 1:
            self.player_2_selection.append("Paper")
        elif self.gesture_selection == 2:
            self.player_2_selection.append("Scissors")
        elif self.gesture_selection == 3:
            self.player_2_selection.append("Lizard")
        elif self.gesture_selection == 4:
            self.player_2_selection.append("Spock")

        # if self.player_1_gesture_selection =="rock" or "0" : 0
        # elif self.player_1_gesture_selection =="Spock" or "1" : 1
        # elif self.player_1_gesture_selection =="paper" or "2" : 2
        # elif self.player_1_gesture_selection =="lizard" or "3" : 3
        # elif self.player_1_gesture_selection =="scissors" or "4" : 4
        # else: print("Error on name.")

        # if self.player_2_gesture_selection =="rock" or "0" : 0
        # elif self.player_2_gesture_selection =="Spock" or "1" : 1
        # elif self.player_2_gesture_selection =="paper" or "2" : 2
        # elif self.player_2_gesture_selection =="lizard" or "3" : 3
        # elif self.player_2_gesture_selection =="scissors" or "4" : 4
        # else: print("Error on name.")

    def computer_gesture_selection(self):
        self.gesture_input = False
        self.gesture_selection = random.randint(0, 4)
        while self.gesture_input != True:
            if self.gesture_selection == 0 or self.gesture_selection == 1 or self.gesture_selection == 2 or self.gesture_selection == 3 or self.gesture_selection == 4:
                self.gesture_input = True
                print('this is ok number')
            else:
                print('Your selection was invalid')
        if self.gesture_selection == 0:
            self.computer_selection.append("Rock")
        elif self.gesture_selection == 1:
            self.computer_selection.append("Paper")
        elif self.gesture_selection == 2:
            self.computer_selection.append("Scissors")
        elif self.gesture_selection == 3:
            self.computer_selection.append("Lizard")
        elif self.gesture_selection == 4:
            self.computer_selection.append("Spock")
