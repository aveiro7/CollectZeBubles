class BubbleController:

    def __init__(self):
        self.bubbles = list()

    def register(self, bubble):
        self.bubbles.append(bubble)

    def deregister(self, bubble):
        self.bubbles.remove(bubble)

    def move_all(self):
        for bubble in self.bubbles:
            bubble.move(-1, 0)
