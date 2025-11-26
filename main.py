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


if __name__ == "__main__":
    main()
