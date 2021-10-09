class Gestures:
    def __init__(self) -> None:
        self.gesture_input = False
        pass

    def player_1_gesture_selection(self):
        self.gesture_selection = int(
            input('Player 1 choose: Rock-0, Paper-1, Scissors-2, Lizard-3, Spock-4'))
        while self.gesture_input != True:
            if self.gesture_selection.isdigit(range(0, 4)):
                self.gesture_input = True
                print('this is ok number')
            else:
                print('Your selection was invalid')
        if self.gesture_selection == 0:
            self.player_1_selection.appead("Rock")
        elif self.gesture_selection == 1:
            self.player_1_selection.appead("Paper")
        elif self.gesture_selection == 2:
            self.player_1_selection.appead("Scissors")
        elif self.gesture_selection == 3:
            self.player_1_selection.appead("Lizard")
        elif self.gesture_selection == 4:
            self.player_1_selection.appead("Spock")
