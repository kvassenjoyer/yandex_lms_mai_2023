class Rectangle:
    # Классный прямоугольник 2.0
    
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

    def get_pos(self):
        return (round(self.lt_x, 2), round(self.lt_y, 2))
    
    def get_size(self):
        return (round(self.width, 2), round(self.height, 2))
    
    def move(self, dx=0, dy=0):
        self.lt_x += dx
        self.rb_x += dx
        
        self.lt_y += dy
        self.rb_y += dy
        
    def resize(self, width=1, height=1):
        self.width = width
        self.height = height
        
        self.rb_x = self.lt_x + self.width
        self.rb_y = self.lt_y - self.height
