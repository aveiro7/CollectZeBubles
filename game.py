from tkinter import *

from ship import Ship


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
        ship = Ship(self)
        ship.move(self.get_window_center_x(),
                  self.get_window_center_y())
        self.mainloop()

    def get_window_center_x(self):
        return self.__GAME_WINDOW_HEIGHT / 2

    def get_window_center_y(self):
        return self.__GAME_WINDOW_HEIGHT / 2


game = Game(Tk())
game.start()
