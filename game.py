from math import sqrt
from random import randint
from time import sleep
from tkinter import *

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

    def calculate_distance(self, point1_x, point1_y, point2_x, point2_y):
        return sqrt((point2_x - point1_x) ** 2 + (point2_y - point1_y) ** 2)

    def detect_collision(self, ship, bubble):
        return ship.radius + bubble.radius >= self.calculate_distance(ship.center_x, ship.center_y, bubble.center_x,
                                                                      bubble.center_y)


game = Game(Tk())
game.start()
