class User:
    def __init__(self, name, birth, info):
        self.name = name
        self.birth = birth
        self.info = info
        self.confirmed = False
        self.updated = False
        self.staff = None

    def get_staff(self):
        return self.staff

    def confirm(self):
        self.confirmed = True

    def is_confirmed(self):
        return self.confirmed

    def get_login(self):
        return self.name

    def edit_info(self, info):
        self.info = info
        self.updated = True

    def is_updated(self):
        return self.updated

    def __str__(self):
        return f"{self.name} ({self.birth}):\n{self.info}\n"

    def get_birth_date(self):
        return self.birth

    def get_info(self):
        return self.info

    def __repr__(self):
        return f"User({self.name}, {self.birth}, {repr(self.staff)})"

    def __gt__(self, other):
        return self.is_ward_of(other)

    def __lt__(self, other):
        return other.is_ward_of(self)

    def __rshift__(self, other):
        other.add_ward(self)

    def is_ward_of(self, other):
        current = self.get_staff()
        while current:
            if current == other:
                return True
            current = current.get_staff()
        return False


class StaffUser(User):
    # Пользователь 2.0

    def __init__(self, name, birth, staff=None):
        super().__init__(name, birth, staff)
        self.wards = []
        self.confirm()

    def add_ward(self, user):
        user.staff = self
        self.wards.append(user)

    def get_wards(self):
        return self.wards

    def __repr__(self):
        return f"StaffUser({self.name}, {self.birth})"
