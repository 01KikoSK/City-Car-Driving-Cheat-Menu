class CheatCode:
    def __init__(self, code, action):
        self.code = code
        self.action = action

    def check_code(self, input_code):
        if input_code == self.code:
            self.action()
            return True
        return False

cheat_menu = [
    CheatCode("health", lambda: print("Health increased to 100%")),
    CheatCode("money", lambda: print("Money increased to $999999999")),
    CheatCode("car", lambda: print("Spawned a new car")),
]

def enter_cheat_code():
    code = input("Enter cheat code: ")
    for cheat in cheat_menu:
        if cheat.check_code(code):
            return
    print("Invalid cheat code")

enter_cheat_code()