import random


class Gestures:
    def __init__(self):
        self.gesture_to_number = 0
        self.number_to_gesture = ""


    def player_1_gesture_selection(self):

        self.gesture_input = False
        self.gesture_selection = int(
            input('Player 1 choose: Rock-0, Spock-1, Paper-2, Lizard-3, Scissors-4' " "))
        while self.gesture_input != True:
            if self.gesture_selection == 0 or self.gesture_selection == 1 or self.gesture_selection == 2 or self.gesture_selection == 3 or self.gesture_selection == 4:
                self.gesture_input = True
                print('this is ok number')
            else:
                print('Your selection was invalid')
            
        if self.gesture_selection == 0:
            self.player_1_selection.append(int(0))
        elif self.gesture_selection == 1:
            self.player_1_selection.append(int(1))
        elif self.gesture_selection == 2:
            self.player_1_selection.append(int(2))
        elif self.gesture_selection == 3:
            self.player_1_selection.append(int(3))
        elif self.gesture_selection == 4:
            self.player_1_selection.append(int(4))

    def player_2_gesture_selection(self):
        self.gesture_input = False
        self.gesture_selection = int(
            input('Player 2 choose: Rock-0, Spock-1, Paper-2, Lizard-3, Scissors-4' " "))
        while self.gesture_input != True:
            if self.gesture_selection == 0 or self.gesture_selection == 1 or self.gesture_selection == 2 or self.gesture_selection == 3 or self.gesture_selection == 4:
                self.gesture_input = True
                print('this is ok number')
            else:
                print('Your selection was invalid')
        if self.gesture_selection == 0:
            self.player_2_selection.append(int(0))
        elif self.gesture_selection == 1:
            self.player_2_selection.append(int(1))
        elif self.gesture_selection == 2:
            self.player_2_selection.append(int(2))
        elif self.gesture_selection == 3:
            self.player_2_selection.append(int(3))
        elif self.gesture_selection == 4:
            self.player_2_selection.append(int(4))

    def computer_gesture_selection(self):

        self.gesture_input = False
        self.gesture_selection = random.randint(0,4)
        while self.gesture_input != True:
            if self.gesture_selection == 0 or self.gesture_selection == 1 or self.gesture_selection == 2 or self.gesture_selection == 3 or self.gesture_selection == 4:
                self.gesture_input = True
                self.number_to_gesture()
            else:
                print('Your selection was invalid')
        if self.gesture_selection == 0:
            self.computer_selection.append(int(0))
        elif self.gesture_selection == 1:
            self.computer_selection.append(int(1))
        elif self.gesture_selection == 2:
            self.computer_selection.append(int(2))
        elif self.gesture_selection == 3:
            self.computer_selection.append(int(3))
        elif self.gesture_selection == 4:
            self.computer_selection.append(int(4))

    def number_to_gesture(self):
        number_to_name = self.gesture_selection
        if number_to_name==0: print(" The computer has chosen Rock!")
        elif number_to_name==1: print(" The computer has chosen Spock!")
        elif number_to_name==2: print(" The computer has chosen Paper!")
        elif number_to_name==3: print(" The computer has chosen Lizard!")
        elif number_to_name==4: print(" The computer has chosen Scissors!")
        else: print("Error on number." )