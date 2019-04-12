class Bubble:
    canvas = None
    outline = None

    def __init__(self, canvas, diameter, color="white"):
        self.canvas = canvas
        self.outline = canvas.create_oval(0, 0, diameter, diameter, outline=color)

    def move(self, offset_x, offset_y):
        self.canvas.move(self.outline, offset_x, offset_y)
