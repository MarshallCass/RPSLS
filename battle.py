from human import Human
from computer import Computer

class Battle:
        def __init__(self):
            self.players_list = []
            self.computers_list = []







## Game player selection validation
   def player_input(self):
        while not self.player_input:
              self.player_selection = int(input(range(1,2)))
        if self.player_selection == 1:
              self.player_input = True
             # AI Method
        elif self.player_selection == 2:
             # human on human
        else:
            # run input again