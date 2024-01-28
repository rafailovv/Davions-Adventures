class Location():
    """ Класс для создания уровней """

    def __init__(self, player, location_name):
        self.player = player
        self.location_name = location_name
    
    def start(self, start_text):
        print(start_text + "\n")

    def actions(self, possible_actions, possible_outcomes):
        while True:
            for i in range(len(possible_actions)):
                print(f"{i + 1}. {possible_actions[i]}")
            
            action_index = input()
            if action_index not in "123456789":
                continue
            else:
                action_index = int(action_index) - 1
            
            if 0 <= action_index <= len(possible_outcomes) - 1:
                print(possible_outcomes[action_index])
                return action_index + 1