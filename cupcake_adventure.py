import arcade


class Game(arcade.Window):
    def __init__(self):
        super().__init__(title="Cupcake Adventure")
        self.level = None

    def setup(self, level):
        pass


def main():
    game = Game()
    game.setup(game.level)
    arcade.run()


if __name__ == "__main__":
    main()
