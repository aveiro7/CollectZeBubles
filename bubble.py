class Bubble:
    canvas = None
    outline = None

    def __init__(self, canvas, color="white"):
        self.canvas = canvas
        self.outline = canvas.create_oval(0, 0, 100, 100, outline=color)
