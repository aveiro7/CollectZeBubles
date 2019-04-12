class ShipController:
    __SHIP_SPEED = 20

    def __init__(self, canvas, ship, move_up_key="<Up>", move_down_key="<Down>", move_left_key="<Left>",
                 move_right_key="<Right>"):
        self.ship = ship
        canvas.bind(move_up_key, self.move_up)
        canvas.bind(move_down_key, self.move_down)
        canvas.bind(move_left_key, self.move_left)
        canvas.bind(move_right_key, self.move_right)

    def move_up(self, event):
        self.ship.move(0, -self.__SHIP_SPEED)

    def move_down(self, event):
        self.ship.move(0, self.__SHIP_SPEED)

    def move_left(self, event):
        self.ship.move(-self.__SHIP_SPEED, 0)

    def move_right(self, event):
        self.ship.move(self.__SHIP_SPEED, 0)
