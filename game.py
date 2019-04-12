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
        self.move_ship(self.__GAME_WINDOW_WIDTH / 2, self.__GAME_WINDOW_HEIGHT / 2)
        self.mainloop()

    def draw_ship(self):
        self.create_polygon(5, 5, 5, 25, 30, 15, fill='green', tags="ship")
        self.create_oval(0, 0, 30, 30, outline='green', tags="ship")

    def move_ship(self, x_offset, y_offset):
        self.move("ship", x_offset, y_offset)


game = Game(Tk())
game.start()
