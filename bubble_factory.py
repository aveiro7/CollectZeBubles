from random import choice

from bubble import Bubble
from bubble_type import BubbleType


class BubbleFactory:
    bubble_types = list(BubbleType)

    def create_random(self, canvas):
        return self.create(canvas, choice(self.bubble_types).value)

    def create(self, canvas, diameter):
        return Bubble(canvas, diameter)
