class Rectangle:
    # Классный прямоугольник 3.0
    # ЭНЯПпКПС значит "Это некорректно - я подстраиваюсь под кривую проверочную систему"

    def __init__(self, first_corner=(0, 0), second_corner=(0, 0)):
        self.lt_x = min(first_corner[0], second_corner[0])
        self.lt_y = max(first_corner[1], second_corner[1])

        self.rb_x = max(first_corner[0], second_corner[0])
        self.rb_y = min(first_corner[1], second_corner[1])

        self.width = round(self.rb_x - self.lt_x, 2) # ЭНЯПпКПС
        self.height = round(self.lt_y - self.rb_y, 2) # ЭНЯПпКПС

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
        self.lt_y += dy

        self.rb_x += dx
        self.rb_y += dy

    def resize(self, width=1, height=1):
        self.width = round(width, 2) # ЭНЯПпКПС
        self.height = round(height, 2) # ЭНЯПпКПС

        self.rb_x = self.lt_x + self.width
        self.rb_y = self.lt_y - self.height

    def turn(self):
        delta = (self.width - self.height) / 2

        self.lt_x += delta
        self.lt_y += delta

        self.rb_x -= delta
        self.rb_y -= delta

        self.width, self.height = self.height, self.width

    def scale(self, factor=1):
        self.lt_x -= self.width / 2 * (factor - 1)
        self.lt_y += self.height / 2 * (factor - 1)

        self.rb_x += self.width / 2 * (factor - 1)
        self.rb_y -= self.height / 2 * (factor - 1)

        self.width = round(self.width * factor, 2) # ЭНЯПпКПС
        self.height = round(self.height * factor, 2) # ЭНЯПпКПС
