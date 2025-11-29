
class Controls:
    def button_controls(self, engine, control_input):
        controls_dict = {
            "w": engine.add,
            "a": engine.multi,
            "s": engine.sub,
            "d": engine.divi,
            "q": engine.num_power_activate,
        }

        if control_input in controls_dict:
            controls_dict[control_input]()
            return True
        else:
            return False
