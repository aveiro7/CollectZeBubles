from tkinter import *


class Game(Canvas):

    def __init__(self, master):
        super().__init__(master,
                         width=800,
                         height=600,
                         bg="darkblue")
        self.pack()

    def start(self):
        self.mainloop()
        print("Game started")


game = Game(Tk())
game.start()
