class Point:
    # Классная точка 2.0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, move_x=0, move_y=0):
        self.x += move_x
        self.y += move_y

    def length(self, other=None):
        if other is None:
            other = Point(0, 0)
        result = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return round(result, 2)
