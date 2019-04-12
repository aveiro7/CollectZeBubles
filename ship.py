class Ship:
    canvas = None
    center_hull = None
    outer_hull = None

    def __init__(self, canvas, color="green"):
        self.canvas = canvas
        self.center_hull = canvas.create_polygon(5, 5, 5, 25, 30, 15, fill=color)
        self.outer_hull = canvas.create_oval(0, 0, 30, 30, outline=color)

    def move(self, x_offset, y_offset):
        self.canvas.move(self.center_hull, x_offset, y_offset)
        self.canvas.move(self.outer_hull, x_offset, y_offset)
