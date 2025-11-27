from controls import Controls
from engine import Engine
from game import Game


def main():
    Engine()
    Controls()
    game = Game()

    game.run()


if __name__ == "__main__":
    main()
