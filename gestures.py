class Gestures:
    def __init__(self):
        self.gesture_to_number = 0
        self.number_to_gesture = ""

##    def picking_gesture(self):


    # def gesture_to_num(self, human_selection):
        # self.gesture_to_number = self.human_selection()
        # if self.gesture_to_number=="rock" or "0": return 0
        # elif self.gesture_to_number=="Spock" or "1": return 1
        # elif self.gesture_to_number=="paper" or "2": return 2
        # elif self.gesture_to_number=="lizard" or "3": return 3
        # elif self.gesture_to_number=="scissors" or "4": return 4
        # else: print("Error on name.")


    def number_to_guesture(self):
        if self.number_to_gesture==0: return "rock"
        elif self.number_to_gesture==1: return "Spock"
        elif self.number_to_gesture==2: return "paper"
        elif self.number_to_gesture==3: return "lizard"
        elif self.number_to_gesture==4: return "scissors"
        else: print("Error on number." )