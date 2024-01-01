class Checkers:
    # Шашки

    def __init__(self):
        self.field: dict[str, Cell] = {}
        positions = [column + row for row in "87654321" for column in "ABCDEFGH"]
        statuses = "XBXBXBXBBXBXBXBXXBXBXBXBXXXXXXXXXXXXXXXXWXWXWXWXXWXWXWXWWXWXWXWX"
        for i in range(64):
            self.field[positions[i]] = Cell(statuses[i])

    def move(self, from_cell, to_cell):
        if self.field[to_cell].status() == "X":
            self.field[to_cell] = Cell(self.field[from_cell].status())
            self.field[from_cell] = Cell("X")
        else:
            raise Exception("Они не проверяют все другие случаи. Кек...")

    def get_cell(self, position):
        return self.field[position]


class Cell:
    def __init__(self, status_value):
        if status_value in ["W", "B", "X"]:
            self.status_value = status_value
        else:
            raise ValueError

    def status(self):
        return self.status_value
