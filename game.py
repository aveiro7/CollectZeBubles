from tkinter import *


class Game(Canvas):

    def __init__(self, master):
        super().__init__(master)
        self.start_game()

    def start_game(self):
        print("Game started")


root = Tk()
root.geometry("800x600")

game = Game(root)
game.mainloop()
