from math import sqrt


class CollisionDetector:

    @staticmethod
    def calculate_distance(point1_x, point1_y, point2_x, point2_y):
        return sqrt((point2_x - point1_x) ** 2 + (point2_y - point1_y) ** 2)

    def are_colliding(self, ship, bubble):
        return ship.radius + bubble.radius >= self.calculate_distance(ship.center_x, ship.center_y, bubble.center_x,
                                                                      bubble.center_y)
