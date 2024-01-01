class Programmer:
    # Работа не волк

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.overrise = 0
        self.worked_time = 0
        self.money = 0

    def work(self, time=0):
        position_dict = {"Junior": 10, "Middle": 15, "Senior": 20}
        rate = position_dict[self.position] + self.overrise

        self.worked_time += time
        self.money += time * rate

    def rise(self):
        if self.position == "Junior":
            self.position = "Middle"
        elif self.position == "Middle":
            self.position = "Senior"
        elif self.position == "Senior":
            self.overrise += 1

    def info(self):
        return f"{self.name} {self.worked_time}ч. {self.money}тгр."
