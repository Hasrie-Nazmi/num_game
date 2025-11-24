from controls import Controls
from engine import Engine
from game import Game


def main():
    engine = Engine()
    game_controls = Controls()
    game = Game()

    game.run()

    while True:
        if not engine.end_game():
            engine.generate_next_num()
            next_num = engine.get_next_num()
            rounds = engine.get_rounds()

            if rounds == 1:
                print(
                    f"Starting number: {next_num}     Random Starting Score: {engine.get_score():.2f}     Lives: {engine.get_lives()}")
            else:
                print(f"Next Number: {next_num}")
            control_input = input("W/A/S/D/Q: ")
            control_input.lower()
            game_controls.button_controls(engine, control_input)

            print(
                f"PREVIOUS ACTION: {engine.get_prev_action()}     SCORE: {engine.get_score():.2f}       Lives: {engine.get_lives()}       POWER TOKEN: {engine.get_power_token_count()}       NUMBER POWER: {engine.get_num_power()}      HIGH SCORE: {engine.get_high_scores():.2f}        ROUNDS: {rounds}"
            )

        else:
            print("Game Over!")
            print(
                f"Your highest score: {engine.get_high_scores():.2f} at Rounds: {rounds}")
            return False


if __name__ == "__main__":
    main()
