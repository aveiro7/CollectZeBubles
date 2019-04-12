from random import randint
from time import sleep
from tkinter import *

from bubble_factory import BubbleFactory
from ship import Ship
from ship_controller import ShipController


class Game(Canvas):
    __GAME_WINDOW_WIDTH = 800
    __GAME_WINDOW_HEIGHT = 600

    def __init__(self, master):
        super().__init__(master,
                         width=self.__GAME_WINDOW_WIDTH,
                         height=self.__GAME_WINDOW_HEIGHT,
                         bg="darkblue")
        self.pack()
        self.focus_set()

    def start(self):
        ship = Ship(self)
        ship.move(self.get_window_center_x(),
                  self.get_window_center_y())
        ShipController(self, ship)
        bubble_factory = BubbleFactory()

        bubbles = list()

        for i in range(50):
            bubble = bubble_factory.create_random(self)
            bubble.move(self.get_random_window_x(), self.get_random_window_y())
            bubbles.append(bubble)

        while 1:
            self.update()
            sleep(0.01)

    def get_window_center_x(self):
        return self.__GAME_WINDOW_WIDTH / 2

    def get_window_center_y(self):
        return self.__GAME_WINDOW_HEIGHT / 2

    def get_random_window_x(self):
        return randint(0, self.__GAME_WINDOW_WIDTH)

    def get_random_window_y(self):
        return randint(0, self.__GAME_WINDOW_HEIGHT)


game = Game(Tk())
game.start()
