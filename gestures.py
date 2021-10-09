import random


class Gestures:
    def __init__(self) -> None:
        self.gesture_input = False
        pass

    def player_1_gesture_selection(self):
        self.gesture_input = False
        self.gesture_selection = int(
            input('Player 1 choose: Rock-0, Paper-1, Scissors-2, Lizard-3, Spock-4'))
        while self.gesture_input != True:
            if self.gesture_selection == 0 or self.gesture_selection == 1 or self.gesture_selection == 2 or self.gesture_selection == 3 or self.gesture_selection == 4:
                self.gesture_input = True
                print('this is ok number')
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

    def player_2_gesture_selection(self):
        self.gesture_input = False
        self.gesture_selection = int(
            input('Player 2 choose: Rock-0, Paper-1, Scissors-2, Lizard-3, Spock-4'))
        while self.gesture_input != True:
            if self.gesture_selection == 0 or self.gesture_selection == 1 or self.gesture_selection == 2 or self.gesture_selection == 3 or self.gesture_selection == 4:
                self.gesture_input = True
                print('this is ok number')
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
