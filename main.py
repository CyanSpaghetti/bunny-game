from src.game import Game 
if __name__ == "__main__":
    game = Game()
    game.init()
    while game.running:
        game.input()
        game.update()
        game.draw()
    game.quit()