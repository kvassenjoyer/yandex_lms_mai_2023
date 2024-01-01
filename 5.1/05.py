class Rectangle:
    # Классный прямоугольник
    
    def __init__(self, first_corner=(0, 0), second_corner=(0, 0)):
        self.lt_x = min(first_corner[0], second_corner[0])
        self.rb_x = max(first_corner[0], second_corner[0])
        self.width = self.rb_x - self.lt_x
        
        self.lt_y = max(first_corner[1], second_corner[1])
        self.rb_y = min(first_corner[1], second_corner[1])
        self.height = self.lt_y - self.rb_y

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)

    def area(self):
        return round(self.width * self.height, 2)
