class User:
    # Пользователь 1.1

    def __init__(self, login, birth_date, info):
        self.login = login
        self.birth_date = birth_date
        self.info = info
        self.confirmed_flag = False
        self.updated_flag = False

    def get_login(self):
        return self.login

    def get_birth_date(self):
        return self.birth_date

    def get_info(self):
        return self.info

    def confirm(self):
        self.confirmed_flag = True

    def is_confirmed(self):
        return self.confirmed_flag

    def is_updated(self):
        return self.updated_flag

    def edit_info(self, info):
        self.info = info
        self.updated_flag = True

    def __repr__(self):
        return f"{self.login} ({self.birth_date}):\n{self.info}\n"
