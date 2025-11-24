
class Controls:
    def button_controls(self, game, control_input):
        controls_dict = {
            "w": game.add,
            "a": game.multi,
            "s": game.sub,
            "d": game.divi,
            "q": game.num_power_activate,
        }

        if control_input in controls_dict:
            controls_dict[control_input]()
        else:
            print("Wrong input")
