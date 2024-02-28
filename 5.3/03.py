# Ломать — не строить 2


class Trash:
    def __repr__(self):
        raise Exception


try:
    trash = Trash()
    func(None, {"один": "два"}, trash)
except Exception:
    print("Ура! Ошибка!")
