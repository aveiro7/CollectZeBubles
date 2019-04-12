class BubbleController:

    def __init__(self, canvas, bubbles):
        self.canvas = canvas
        self.bubbles = bubbles

    def move_all(self):
        for bubble in self.bubbles:
            bubble.move(-1, 0)
