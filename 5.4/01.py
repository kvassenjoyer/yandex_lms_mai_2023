class User:
    # Пользователь 1.0

    def __init__(self, login, birth_date, info):
        self.login = login
        self.birth_date = birth_date
        self.info = info

    def get_login(self):
        return self.login

    def get_birth_date(self):
        return self.birth_date

    def get_info(self):
        return self.info
