from tkinter import *


class Game(Canvas):
    __GAME_WINDOW_WIDTH = 800
    __GAME_WINDOW_HEIGHT = 600

    def __init__(self, master):
        super().__init__(master,
                         width=self.__GAME_WINDOW_WIDTH,
                         height=self.__GAME_WINDOW_HEIGHT,
                         bg="darkblue")
        self.pack()

    def start(self):
        print("Game started")
        self.draw_ship()
        self.mainloop()

    def draw_ship(self):
        self.create_polygon(5, 5, 5, 25, 30, 15, fill='green')
        self.create_oval(0, 0, 30, 30, outline='green')


game = Game(Tk())
game.start()
