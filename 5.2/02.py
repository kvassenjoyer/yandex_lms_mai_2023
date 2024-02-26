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


class PatchedPoint(Point):
    # Классная точка 4.0

    def __init__(self, *args):
        if len(args) == 0:
            self.x, self.y = 0, 0
        elif len(args) == 1:
            self.x, self.y = args[0]
        elif len(args) == 2:
            self.x, self.y = args
        else:
            raise Exception("Invalid initialisation")

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"PatchedPoint({self.x}, {self.y})"
