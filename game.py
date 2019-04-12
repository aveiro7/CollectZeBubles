from random import randint
from time import sleep
from tkinter import *

from bubble_controller import BubbleController
from bubble_factory import BubbleFactory
from collision_detector import CollisionDetector
from ship import Ship
from ship_controller import ShipController


class Game(Canvas):
    __GAME_WINDOW_WIDTH = 800
    __GAME_WINDOW_HEIGHT = 600
    bubble_factory = BubbleFactory()
    bubble_controller = BubbleController()

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
        collision_detector = CollisionDetector()

        for _ in range(50):
            bubble = self.bubble_factory.create_random(self)
            bubble.move(self.get_random_window_x(), self.get_random_window_y())
            self.bubble_controller.register(bubble)

        while 1:
            for bubble in self.bubble_controller.bubbles:
                if collision_detector.are_colliding(ship, bubble):
                    self.delete_bubble(bubble)
                self.remove_if_outside(bubble)

            self.bubble_controller.move_all()

            self.update()
            sleep(0.01)

    def delete_bubble(self, bubble):
        bubble.destroy()
        self.bubble_controller.deregister(bubble)
        new_bubble = self.bubble_factory.create_random(self)
        new_bubble.move(self.get_random_window_x(), self.get_random_window_y())
        self.bubble_controller.register(new_bubble)

    def remove_if_outside(self, bubble):
        if bubble.center_x + bubble.radius < 0:
            self.delete_bubble(bubble)

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
