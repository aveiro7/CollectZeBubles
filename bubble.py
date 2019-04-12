class Bubble:
    canvas = None
    outline = None
    radius = 0
    center_x = 0
    center_y = 0

    def __init__(self, canvas, diameter, color="white"):
        self.canvas = canvas
        self.outline = canvas.create_oval(0, 0, diameter, diameter, outline=color)
        self.radius = diameter / 2
        self.center_x = self.radius
        self.center_y = self.radius

    def move(self, offset_x, offset_y):
        self.canvas.move(self.outline, offset_x, offset_y)
        self.center_x += offset_x
        self.center_y += offset_y

    def destroy(self):
        self.canvas.delete(self.outline)
